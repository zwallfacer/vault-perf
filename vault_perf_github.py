#!/usr/bin/env python3
"""Time-weighted return, APR/APY and risk ratios for any Hyperliquid account.

    ./vault_perf_github.py 0x<address>              live, from the public API
    ./vault_perf_github.py 0x<address> --harvest    append to a local archive
    ./vault_perf_github.py 0x<address> --json       machine-readable

Read-only. Hits Hyperliquid's public /info endpoint with a PUBLIC address. No keys,
no signing, no orders — the script has no code path that could place a trade.

WHY NOT JUST LOOK AT THE BALANCE
--------------------------------
Equity growth is not return. An account that doubles may have done so entirely
through deposits. Comparing start and end equity on a funded account routinely
overstates performance by an order of magnitude.

The fix is a time-weighted return: chain each period's return on the capital that
was actually at work during it.

    r_i = (pnl[i] - pnl[i-1]) / accountValue[i-1]      TWR = prod(1 + r_i) - 1

Hyperliquid's `pnlHistory` already excludes deposits and withdrawals, so the
numerator is trading P&L alone. That is what makes this time-weighted rather than
money-weighted, and it is why the result can be far below — or above — the change
in account value.

WHY AN ARCHIVE
--------------
The API is not a viable long-term source, because its resolution DECAYS. The
`allTime` window is a fixed budget of roughly 45-70 samples stretched across the
account's entire life, so the gap between samples grows as the account ages:

    a 24-day-old account   allTime   ~44 pts / 23.7d    median gap   8.7h
    a 428-day-old account  allTime   ~67 pts / 427.7d   median gap 167.7h  (7 DAYS)
    any account            week      ~62 pts /  7.0d    median gap   2.3h

Coarse sampling does not merely blur the result — it INVALIDATES it. A deposit that
lands and trades between two samples puts the wrong denominator under the P&L. On a
7-day-gapped series we measured sub-periods of -222% (a $292 loss against a $131
sample). A return past -100% is impossible; it is a sampling artifact, not a loss.

So `--harvest` copies the fine `week` window (2.3h, never degrades) into an
append-only local archive. Run it daily and the archive keeps 2.3h resolution
indefinitely, long after the API would only offer 7-day gaps for the same period.

WHAT IS ARCHIVED
----------------
One ABSOLUTE point per line: {"t": ms, "av": accountValue, "pnl": cumulative pnl}.

The subtlety worth knowing: `pnlHistory` is WINDOW-RELATIVE — every window restarts
at 0 — while `accountValue` is absolute. So each finer window is shifted onto the
`allTime` window's absolute scale using the constant offset measured at their shared
timestamps (verified constant to 1e-6 across every shared point). Once stored
absolute, points dedup by timestamp, cannot overlap, and a larger time step is
simply a larger step. No reconciliation logic is needed.

WHAT IT REFUSES TO DO
---------------------
Three guards, because a confident wrong number is worse than no number:

  * a period whose starting equity is below MIN_EQUITY is excluded (near-zero
    divisor), and the count and P&L of what was excluded is REPORTED, never silent;
  * if any period exceeds +/-EXTREME_RET the whole chain is declared invalid and no
    TWR/APR/APY/ratio is printed — that pattern means the equity sample does not
    represent the capital at risk, and every figure built on it would be noise;
  * annualising a window under THIN_DAYS prints a warning and the trailing-7d figure
    alongside, because a few early days on a small balance can dominate the result.

METHOD NOTES ON THE RATIOS
--------------------------
  * Drawdown is computed on the TWR curve, never on account value — a drawdown
    measured on a funded account's balance is meaningless.
  * Sharpe and Sortino resample to DAILY first. Sampling is irregular, and a 9h
    period carries ~4x the variance of a 2.3h one; feeding that heterogeneous series
    to a standard deviation would mis-state volatility. Daily closes make the
    observations comparable and the sqrt(365) scaling honest.
  * Risk-free rate is taken as zero and Sortino's target is zero. On a short window
    the risk-free term is noise next to sampling error.
"""
import argparse
import datetime as dt
import json
import math
import os
import re
import sys

import requests

BASE = "https://api.hyperliquid.xyz"
ROOT = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.environ.get("VAULT_ARCHIVE_DIR", os.path.join(ROOT, "vault_equity"))

# allTime is the absolute reference; the others are finer and get shifted onto it.
HARVEST_WINDOWS = ["allTime", "month", "week"]
WINDOWS = ["day", "week", "month", "allTime",
           "perpDay", "perpWeek", "perpMonth", "perpAllTime"]

MIN_EQUITY = 1.0      # below this a period return is meaningless (near-zero divisor)
THIN_DAYS = 30.0      # annualising a shorter window is fragile -- say so
EXTREME_RET = 0.50    # any period past this => the chain is a sampling artifact

ADDR_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")

C = {"red": "\033[31m", "yellow": "\033[33m", "green": "\033[32m",
     "dim": "\033[2m", "bold": "\033[1m", "off": "\033[0m"}


def paint(s, *names, on=True):
    return "".join(C[n] for n in names) + s + C["off"] if on else s


def fetch_portfolio(addr, timeout=20):
    r = requests.post(f"{BASE}/info", json={"type": "portfolio", "user": addr}, timeout=timeout)
    r.raise_for_status()
    return dict(r.json())


def _window_series(pf, w):
    win = pf.get(w) or {}
    avh, ph = win.get("accountValueHistory", []), win.get("pnlHistory", [])
    if len(avh) != len(ph):
        return {}
    return {t: (float(av), float(p)) for (t, av), (_, p) in zip(avh, ph)}


def to_points(pf, windows=HARVEST_WINDOWS):
    """Absolute (t, av, pnl) points, every window shifted onto allTime's pnl scale.

    A window sharing no timestamp with allTime is SKIPPED rather than guessed at: an
    unanchored window would silently contribute a wrong cumulative level.
    """
    ref = _window_series(pf, "allTime")
    if not ref:
        return []
    out = dict(ref)
    for w in windows:
        if w == "allTime":
            continue
        s = _window_series(pf, w)
        shared = sorted(set(s) & set(ref))
        if not shared:
            continue
        offs = sorted(ref[t][1] - s[t][1] for t in shared)
        off = offs[len(offs) // 2]      # median: they agree; this shrugs off an outlier
        for t, (av, p) in s.items():
            out[t] = (av, p + off)      # finer window supersedes, same value on overlap
    return [{"t": t, "av": v[0], "pnl": v[1]} for t, v in sorted(out.items())]


def archive_path(addr):
    return os.path.join(ARCHIVE_DIR, f"{addr.lower()}.jsonl")


def load_archive(addr):
    p = archive_path(addr)
    if not os.path.exists(p):
        return []
    out = []
    with open(p) as fh:
        for ln in fh:
            ln = ln.strip()
            if not ln:
                continue
            try:
                out.append(json.loads(ln))
            except json.JSONDecodeError:
                continue
    return out


def merge(points):
    """Dedup by timestamp, sorted. Absolute points need nothing cleverer."""
    by_t = {p["t"]: p for p in points}
    return [by_t[t] for t in sorted(by_t)]


def harvest(addr, color=True):
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    fresh = to_points(fetch_portfolio(addr))
    if not fresh:
        print(paint("harvest: allTime window empty -- nothing anchored, nothing written",
                    "red", on=color))
        return 0
    existing = load_archive(addr)
    have = {p["t"] for p in existing}
    new = [p for p in fresh if p["t"] not in have]
    with open(archive_path(addr), "a") as fh:
        for p in new:
            fh.write(json.dumps({"t": p["t"], "av": round(p["av"], 6),
                                 "pnl": round(p["pnl"], 6)}, separators=(",", ":")) + "\n")
    merged = merge(existing + fresh)
    span = (merged[-1]["t"] - merged[0]["t"]) / 1000 / 86400 if len(merged) > 1 else 0.0
    print(paint(f"harvest: +{len(new)} new point(s), archive now {len(merged)} points "
                f"covering {span:.2f} days", "bold", on=color))
    print(f"  -> {archive_path(addr)}")
    return len(new)


def risk_metrics(curve, apr):
    """Sharpe / Sortino / Calmar / maxDD from the chained time-weighted curve."""
    out = {}
    if not curve:
        return out
    peak, mdd = curve[0][1], 0.0
    for _, v in curve:
        peak = max(peak, v)
        if peak > 0:
            mdd = max(mdd, (peak - v) / peak)
    out["max_dd"] = mdd

    daily = {}
    for ts, v in curve:
        daily[dt.datetime.fromtimestamp(ts / 1000, dt.UTC).strftime("%Y-%m-%d")] = v
    idx = [daily[d] for d in sorted(daily)]
    out["n_daily"] = len(idx)
    if len(idx) >= 3:
        r = [idx[i] / idx[i - 1] - 1.0 for i in range(1, len(idx))]
        n = len(r)
        mean = sum(r) / n
        sd = math.sqrt(sum((x - mean) ** 2 for x in r) / (n - 1))
        out.update(n_daily_returns=n, daily_mean=mean, daily_sd=sd)
        out["sharpe"] = (mean / sd * math.sqrt(365.0)) if sd > 0 else None
        dn = [x for x in r if x < 0.0]
        out["n_down_days"] = len(dn)
        if dn:
            dsd = math.sqrt(sum(x * x for x in dn) / len(dn))   # downside dev vs target 0
            out["sortino"] = (mean / dsd * math.sqrt(365.0)) if dsd > 0 else None
        else:
            out["sortino"] = None       # no losing day yet -> undefined, not infinite
    out["calmar"] = (apr / mdd) if (apr is not None and mdd > 1e-12) else None
    return out


def chain(points, source_label):
    """Chain consecutive point-to-point returns. Never silently drops data."""
    pts = merge(points)
    if len(pts) < 2:
        raise SystemExit("!! fewer than 2 points -- try --source api, or --harvest first")

    kept, skipped_n, skipped_pnl = [], 0, 0.0
    c, curve = 1.0, []
    for a, b in zip(pts, pts[1:]):
        d = b["pnl"] - a["pnl"]
        if a["av"] < MIN_EQUITY:
            if abs(d) > 1e-9:
                skipped_n += 1
                skipped_pnl += d
            continue
        r = d / a["av"]
        c *= (1.0 + r)
        kept.append({"t0": a["t"], "t1": b["t"], "eq0": a["av"], "dpnl": d, "ret": r})
        curve.append((b["t"], c))
    if not kept:
        raise SystemExit(f"!! no period had >= ${MIN_EQUITY:.2f} starting equity")

    twr = c - 1.0
    days = (kept[-1]["t1"] - kept[0]["t0"]) / 1000.0 / 86400.0
    extreme = [k for k in kept if abs(k["ret"]) > EXTREME_RET]
    valid = not extreme
    gaps = sorted((k["t1"] - k["t0"]) / 1000 / 3600 for k in kept)

    out = {
        "source": source_label, "twr": twr, "days": days, "valid": valid,
        "n_points": len(pts), "n_periods": len(kept),
        "skipped_n": skipped_n, "skipped_pnl": skipped_pnl,
        "equity_first": kept[0]["eq0"], "equity_last": pts[-1]["av"],
        "sum_pnl": sum(k["dpnl"] for k in kept),
        "n_extreme": len(extreme),
        "extreme": sorted(extreme, key=lambda k: abs(k["ret"]), reverse=True)[:5],
        "thin": days < THIN_DAYS,
        "apr": (twr * 365.0 / days) if (valid and days > 0) else None,
        "apy": ((1.0 + twr) ** (365.0 / days) - 1.0) if (valid and days > 0 and twr > -1) else None,
        "median_gap_h": gaps[len(gaps) // 2],
        "max_gap_h": gaps[-1],
        "periods": kept,
    }

    cut = kept[-1]["t1"] - 7 * 86400 * 1000
    tail = [k for k in kept if k["t0"] >= cut]
    if valid and len(tail) >= 2:
        c7 = 1.0
        for k in tail:
            c7 *= (1.0 + k["ret"])
        d7 = (tail[-1]["t1"] - tail[0]["t0"]) / 1000.0 / 86400.0
        out.update(twr_7d=c7 - 1.0, days_7d=d7,
                   apr_7d=((c7 - 1.0) * 365.0 / d7) if d7 > 0 else None)

    # Ratios share the validity gate: if the chain is a sampling artifact, so are they.
    out.update(risk_metrics(curve, out["apr"]) if valid else {"n_daily": 0})
    return out


def render(res, addr, color=True):
    fmt = lambda ms: dt.datetime.fromtimestamp(ms / 1000, dt.UTC).strftime("%Y-%m-%d %H:%M")
    print(paint(f"\n{addr}   source={res['source']}", "bold", on=color))
    print(f"  equity   ${res['equity_first']:,.2f} -> ${res['equity_last']:,.2f}"
          f"   (this change includes DEPOSITS; it is not return)")
    print(f"  P&L      ${res['sum_pnl']:+,.2f}   over {res['days']:.2f} days from"
          f" {res['n_points']} points, median gap {res['median_gap_h']:.2f}h"
          f" (max {res['max_gap_h']:.2f}h)")

    by_day = {}
    for k in res["periods"]:
        d = dt.datetime.fromtimestamp(k["t1"] / 1000, dt.UTC).strftime("%Y-%m-%d")
        a = by_day.setdefault(d, [k["eq0"], 0.0, 1.0])
        a[1] += k["dpnl"]
        a[2] *= (1.0 + k["ret"])
    print(f"\n  {'date':10s} {'equity@start':>13s} {'PnL':>9s} {'return':>10s}")
    for d, (eq0, pnl, cc) in by_day.items():
        r = (cc - 1.0) * 100.0
        col = "green" if r > 0 else ("red" if r < 0 else "dim")
        print(f"  {d:10s} {eq0:13,.2f} {pnl:+9.2f} " + paint(f"{r:+9.3f}%", col, on=color))

    if res["valid"]:
        print(paint(f"\n  time-weighted return   {res['twr'] * 100:+.3f}%", "bold", on=color))
        print(f"  APR (simple)           {res['apr'] * 100:+.1f}%")
        if res["apy"] is not None:
            print(f"  APY (compounded)       {res['apy'] * 100:+.1f}%")
        print(paint("  (net of fees AND funding: pnlHistory is equity change minus external", "dim", on=color))
        print(paint("   flows, so everything else is already inside it)", "dim", on=color))

        f_ = lambda v: f"{v:+.2f}" if v is not None else "n/a"
        print(f"\n  max drawdown           {res.get('max_dd', 0.0) * 100:.2f}%"
              + paint("   (on the TWR curve, not account value)", "dim", on=color))
        print(f"  Sharpe  (rf=0)         {f_(res.get('sharpe'))}")
        print(f"  Sortino (target=0)     {f_(res.get('sortino'))}"
              + ("" if res.get("n_down_days") else paint("   - no losing day yet, so undefined", "dim", on=color)))
        print(f"  Calmar  (APR / maxDD)  {f_(res.get('calmar'))}")
        nd = res.get("n_daily_returns", 0)
        if nd and nd < 30:
            print(paint(f"  !! {nd} daily observations - these ratios are indicative only.", "yellow", on=color))
            print(paint("     Sharpe/Sortino need ~30+ to mean much; one outlier day moves them a lot.", "yellow", on=color))
    else:
        print(paint("\n  time-weighted return   INVALID -- not reported", "red", "bold", on=color))
        print(paint("  APR / APY / ratios     INVALID -- not reported", "red", "bold", on=color))

    if res["skipped_n"]:
        print(paint(f"\n  !! {res['skipped_n']} period(s) carrying ${res['skipped_pnl']:+,.2f} EXCLUDED:"
                    f" starting equity < ${MIN_EQUITY:.2f}.", "yellow", on=color))
        print(paint("     The return above does not represent that P&L.", "yellow", on=color))

    if not res["valid"]:
        print(paint(f"\n  !! TWR IS NOT VALID HERE: {res['n_extreme']} of {res['n_periods']} periods"
                    f" exceed +/-{EXTREME_RET * 100:.0f}%.", "red", "bold", on=color))
        print(paint("     A return past +/-100% is impossible; it means the equity SAMPLE at the", "red", on=color))
        print(paint("     period start is not the capital that was at risk during it -- a deposit", "red", on=color))
        print(paint("     landed and traded between two samples. Chaining across that is noise.", "red", on=color))
        for k in res["extreme"]:
            print(paint(f"       {fmt(k['t1'])}  ${k['dpnl']:+10,.2f} on ${k['eq0']:>10,.2f}"
                        f" = {k['ret'] * 100:+,.1f}%  (gap {(k['t1'] - k['t0']) / 3.6e6:.1f}h)", "red", on=color))
        print(paint("     Use cumulative P&L for this account, or harvest a finer series.", "red", on=color))

    if res["thin"] and res["valid"]:
        print(paint(f"\n  !! THIN WINDOW: {res['days']:.1f} days. Annualising is fragile -- a few"
                    f" early days", "yellow", on=color))
        print(paint("     on a small balance can dominate the compounding.", "yellow", on=color))
        if res.get("apr_7d") is not None:
            print(paint(f"     trailing 7d: TWR {res['twr_7d'] * 100:+.3f}% over {res['days_7d']:.2f}d"
                        f"  ->  APR {res['apr_7d'] * 100:+.1f}%", "yellow", on=color))


def main():
    ap = argparse.ArgumentParser(
        description="Time-weighted return / APR / APY / risk ratios for a Hyperliquid account.")
    ap.add_argument("address", help="PUBLIC account address, 0x + 40 hex")
    ap.add_argument("--harvest", action="store_true",
                    help="append the current fine window to the local archive, then exit")
    ap.add_argument("--source", default=None, choices=["merged", "archive", "api"],
                    help="archive = local only; api = live only; merged = both. "
                         "Default: archive if one exists for this address, else api.")
    ap.add_argument("-w", "--window", default=None, choices=WINDOWS,
                    help="restrict the API side to ONE window. Default: allTime+month+week "
                         "normalised onto one scale, which is finer.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--no-color", action="store_true", help="disable ANSI color")
    a = ap.parse_args()

    addr = a.address
    if not ADDR_RE.match(addr):
        raise SystemExit(f"!! '{addr}' is not a valid address (expected 0x + 40 hex = 42 chars). "
                         f"A PRIVATE key is 0x + 64 hex -- never pass one to this or any script.")

    color = not a.no_color and sys.stdout.isatty()

    if a.harvest:
        harvest(addr, color=color)
        return

    archived = load_archive(addr)
    if a.source is None:
        # An archive beats the API: it is local, and it holds fine resolution the API
        # has already coarsened away. Without one there is nothing to read but live.
        a.source = "archive" if archived else "api"

    pts, src = [], a.source
    if a.source in ("merged", "archive"):
        pts += archived
        if a.source == "archive" and not archived:
            raise SystemExit(f"!! no local archive for {addr}. Either run:\n"
                             f"     ./vault_perf_github.py {addr} --harvest\n"
                             f"   or read it live:  ./vault_perf_github.py {addr} --source api")
    if a.source in ("merged", "api"):
        try:
            pf = fetch_portfolio(addr)
        except Exception as e:
            raise SystemExit(f"!! portfolio fetch failed: {type(e).__name__}: {e}")
        if a.window:
            s = _window_series(pf, a.window)
            pts += [{"t": t, "av": v[0], "pnl": v[1]} for t, v in sorted(s.items())]
            src = f"{a.source}:{a.window}"
        else:
            pts += to_points(pf)
    if not pts:
        raise SystemExit(f"!! nothing to chain for {addr} -- the account may have no history.")

    res = chain(pts, src)

    if a.json:
        out = {k: v for k, v in res.items() if k not in ("periods", "extreme")}
        out["address"] = addr
        json.dump(out, sys.stdout, indent=2, default=float)
        print()
    else:
        render(res, addr, color=color)


if __name__ == "__main__":
    main()
