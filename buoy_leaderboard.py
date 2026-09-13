#!/usr/bin/env python3
"""Daily leaderboard: the top buoy.finance vaults by TVL, with time-weighted performance.

Ranks by TVL (the one figure buoy publishes directly) and reports, for each vault, the
same time-weighted metrics vault_perf_github.py produces for a single account -- chained
per-period returns over Hyperliquid's pnlHistory, which already excludes deposits and
withdrawals. Equity growth is NOT return on a funded vault, and a TVL ranking says
nothing about whether a vault makes money; these columns are the part that does.

WHAT IS PUBLISHED
    Address, TVL, and rolled-up ratios. Vault NAMES are deliberately not published -- the
    table identifies a vault by the only thing that is unambiguous and self-verifiable,
    its address. One address carries a label, passed via --pin-label, so the operator's
    own vault is identifiable in its own report.

    No fills, prices, sizes, positions or account balances appear anywhere.

VALIDITY IS PER VAULT
    A vault whose chain contains an impossible period return (a deposit landing between
    two samples) is marked invalid and its annualised columns are suppressed rather than
    printed with a caveat. A vault too young to annualise honestly is flagged thin. Both
    are shown as such in the table instead of being silently dropped, because a missing
    row and a suppressed figure mean very different things.
"""
import argparse, datetime as dt, html, json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vault_perf_github as V

BUOY_API = os.environ.get(
    "BUOY_API", "https://europe-west1-buoy-loan.cloudfunctions.net/app/api/vaults")
REQ_GAP_S = 0.35          # be a polite client of a public API


# ---------------------------------------------------------------- source data
def fetch_vaults(timeout=30):
    """Every buoy vault, paginated. TVL is an integer in asset base units."""
    import requests
    items, off = [], 0
    while True:
        r = requests.get(BUOY_API, params={"offset": off, "limit": 100},
                         headers={"accept": "application/json"}, timeout=timeout)
        r.raise_for_status()
        d = r.json()
        items += d.get("items", [])
        page = d.get("page") or {}
        if not page.get("hasMore"):
            break
        off += page.get("limit", 100)
    out = []
    for x in items:
        try:
            dec = int(x.get("assetDecimals") or 6)
            out.append({"address": x["address"], "tvl": float(x.get("tvl") or 0) / 10 ** dec})
        except (KeyError, TypeError, ValueError):
            continue
    out.sort(key=lambda v: v["tvl"], reverse=True)
    for i, v in enumerate(out, 1):
        v["rank"] = i
    return out


def select(vaults, top, pin):
    """Top N by TVL, plus the pinned vault appended if it has fallen out of the top N."""
    rows = vaults[:top]
    if pin:
        p = pin.lower()
        if not any(v["address"].lower() == p for v in rows):
            extra = next((v for v in vaults if v["address"].lower() == p), None)
            # Unlisted (delisted, or not a buoy vault): still report it, rank unknown.
            rows = rows + [extra or {"address": pin, "tvl": None, "rank": None}]
    return rows


def metrics_for(addr, do_harvest):
    """Metrics for one address. Never raises: a dead vault must not kill the table."""
    try:
        if do_harvest:
            try:
                V.harvest(addr, color=False)
            except Exception as e:
                print(f"  harvest skipped for {addr}: {type(e).__name__}: {e}", file=sys.stderr)
        pts = V.load_archive(addr)
        src = "merged" if pts else "api"
        pts = pts + V.to_points(V.fetch_portfolio(addr))
        if not pts:
            return {"error": "no history"}
        res = V.chain(pts, src)
        if res.get("valid"):
            return res
        # One impossible period -- almost always a deposit inside a coarse allTime gap --
        # otherwise blanks an entire vault, which on a comparison table reads as "no data"
        # rather than "one bad early sample". Re-chain the clean trailing window instead
        # and say so. The Window column already shows the reader it is shorter. We do NOT
        # drop interior bad periods: only a contiguous suffix with none is trusted.
        cut = max(k["t1"] for k in res.get("extreme") or [{"t1": 0}])
        tail = [q for q in V.merge(pts) if q["t"] >= cut]
        if len(tail) >= 10:
            try:
                alt = V.chain(tail, src + ":trimmed")
            except SystemExit:
                return res
            if alt.get("valid") and alt["days"] >= 7.0:
                alt["trimmed"] = True
                alt["trimmed_from_days"] = res["days"]
                return alt
        return res
    except SystemExit as e:                 # chain() refuses rather than guesses
        return {"error": str(e).lstrip("! ").strip() or "refused"}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


# ---------------------------------------------------------------- presentation
COLS = [
    # key            label        kind    better
    ("tvl",         "TVL",        "usd",  None),
    ("twr",         "TWR",        "pct",  "hi"),
    ("apr",         "APR",        "pct",  "hi"),
    ("apy",         "APY",        "pct",  "hi"),
    ("max_dd",      "Max DD",     "pct",  "lo"),
    ("sharpe",      "Sharpe",     "num",  "hi"),
    ("sortino",     "Sortino",    "num",  "hi"),
    ("calmar",      "Calmar",     "num",  "hi"),
    ("days",        "Window",     "days", None),
]


def cell(row, key, kind):
    """(display string, sort value or None). Annualised columns are suppressed when the
    chain is invalid -- a figure derived from an impossible return is not a figure."""
    m = row["m"]
    if key == "tvl":                       # TVL comes from buoy, not from the return chain,
        v = row.get("tvl")                 # so it survives a vault whose metrics failed.
        return ("—", None) if v is None else (f"${v:,.0f}", v)
    if "error" in m:
        return "—", None
    if key in ("apr", "apy", "sharpe", "sortino", "calmar") and not m.get("valid", False):
        return "—", None
    v = m.get(key)
    if v is None:
        return "—", None
    if kind == "usd":
        return f"${v:,.0f}", v
    if kind == "pct":
        return f"{v * 100:+.2f}%" if key != "max_dd" else f"{v * 100:.2f}%", v
    if kind == "days":
        return f"{v:.1f}d", v
    return f"{v:+.2f}", v


def rows_payload(rows, pin, pin_label):
    p = (pin or "").lower()
    out = []
    for r in rows:
        m = r["m"]
        out.append({
            "rank": r.get("rank"),
            "address": r["address"],
            "label": pin_label if r["address"].lower() == p else None,
            "tvl": r.get("tvl"),
            "valid": m.get("valid") if "error" not in m else None,
            "thin": m.get("thin") if "error" not in m else None,
            "trimmed": m.get("trimmed", False) if "error" not in m else None,
            "trimmed_from_days": m.get("trimmed_from_days"),
            "error": m.get("error"),
            **{k: (None if "error" in m else m.get(k))
               for k in ("twr", "apr", "apy", "max_dd", "sharpe", "sortino", "calmar",
                         "days", "n_points", "n_daily")},
        })
    return out


def render_markdown(rows, pin, pin_label, stamp):
    L = [f"# buoy.finance — top {len([r for r in rows if r.get('rank')])} vaults by TVL",
         "",
         f"_Generated {stamp} UTC. Time-weighted, net of fees and funding._",
         "",
         "Ranked by TVL. Vaults are identified by address only.",
         "",
         "| # | Address | " + " | ".join(lbl for _, lbl, _, _ in COLS) + " |",
         "|---:|---|" + "---:|" * len(COLS)]
    for r in rows:
        a = r["address"]
        tag = f" **{pin_label}**" if pin and a.lower() == pin.lower() else ""
        flag = ""
        if "error" in r["m"] or not r["m"].get("valid", True):
            flag = " ⚠"
        elif r["m"].get("trimmed"):
            flag = " ✂"
        elif r["m"].get("thin"):
            flag = " †"
        rank = str(r["rank"]) if r.get("rank") else "—"
        cells = [cell(r, k, kind)[0] for k, _, kind, _ in COLS]
        L.append(f"| {rank} | `{a}`{tag}{flag} | " + " | ".join(cells) + " |")
    L += ["",
          "† window shorter than 30 days — annualised figures are fragile at that length.",
          "",
          "✂ earlier history contained an impossible period return, so the figures are "
          "computed on the clean trailing window only; the Window column shows its length.",
          "",
          "⚠ chain invalid or unavailable — annualised columns suppressed rather than "
          "printed from an impossible period return (usually a deposit landing between "
          "two API samples).",
          "",
          "Returns are time-weighted: per-period returns chained over Hyperliquid's "
          "`pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing "
          "about performance — that is what the other columns are for.",
          "",
          "A sortable version of this table is published at "
          "[the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).",
          ""]
    return "\n".join(L)


HTML_HEAD = """<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>buoy vaults — performance</title>
<style>
  :root {
    --bg:#fbfbfa; --panel:#fff; --ink:#1a1a18; --ink2:#5c5c56; --ink3:#8a8a82;
    --line:#e4e4df; --accent:#1f6f53; --accent-bg:#e8f2ee; --warn:#8a5a1f;
    --pos:#1f6f53; --neg:#a33a2a;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg:#15161a; --panel:#1c1e23; --ink:#e9e9e4; --ink2:#a8a89f; --ink3:#7b7b73;
      --line:#2c2f36; --accent:#5fbf99; --accent-bg:#1d3630; --warn:#d0a05a;
      --pos:#5fbf99; --neg:#e08472;
    }
  }
  html { -webkit-text-size-adjust:100%; }
  body { margin:0; background:var(--bg); color:var(--ink);
         font:14px/1.5 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif; }
  .wrap { max-width:1180px; margin:0 auto; padding:32px 20px 64px; }
  h1 { font-size:22px; letter-spacing:-.01em; margin:0 0 4px; font-weight:650; }
  .sub { color:var(--ink2); margin:0 0 22px; font-size:13px; }
  .scroll { overflow-x:auto; background:var(--panel); border:1px solid var(--line);
            border-radius:10px; }
  table { border-collapse:separate; border-spacing:0; width:100%; font-variant-numeric:tabular-nums; }
  th,td { padding:10px 12px; text-align:right; white-space:nowrap;
          border-bottom:1px solid var(--line); }
  th:first-child,td:first-child { text-align:right; color:var(--ink3); width:1%; }
  th:nth-child(2),td:nth-child(2) { text-align:left; }
  thead th { position:sticky; top:0; background:var(--panel); z-index:1;
             font-size:11px; letter-spacing:.06em; text-transform:uppercase;
             color:var(--ink2); font-weight:600; cursor:pointer; user-select:none; }
  thead th:hover { color:var(--ink); }
  thead th[aria-sort] { color:var(--accent); }
  thead th .ar { opacity:.5; font-size:10px; margin-left:4px; }
  tbody tr:last-child td { border-bottom:0; }
  tbody tr:hover td { background:color-mix(in srgb, var(--accent) 5%, transparent); }
  .addr { font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12.5px; }
  .tag { display:inline-block; margin-left:8px; padding:1px 7px; border-radius:999px;
         background:var(--accent-bg); color:var(--accent); font-size:11px; font-weight:600; }
  .flag { color:var(--warn); margin-left:6px; cursor:help; }
  .pos { color:var(--pos); } .neg { color:var(--neg); } .na { color:var(--ink3); }
  .notes { margin-top:20px; color:var(--ink2); font-size:12.5px; max-width:78ch; }
  .notes p { margin:.55em 0; }
  code { font-family:ui-monospace,Menlo,monospace; font-size:12px; }
  a { color:var(--accent); }
  @media (max-width:640px) { .wrap{padding:20px 12px 48px;} .addr{font-size:11px;} }
</style>
"""

HTML_JS = """<script>
(function () {
  var tb = document.querySelector("tbody"), ths = document.querySelectorAll("thead th");
  function sortBy(i, dir) {
    var rows = Array.prototype.slice.call(tb.rows);
    rows.sort(function (a, b) {
      var x = a.cells[i].dataset.v, y = b.cells[i].dataset.v;
      // A suppressed or missing figure is not a small figure: park it at the bottom
      // in BOTH directions rather than letting it win an ascending sort.
      var nx = (x === "" || x === undefined), ny = (y === "" || y === undefined);
      if (nx && ny) return 0;
      if (nx) return 1;
      if (ny) return -1;
      return (parseFloat(x) - parseFloat(y)) * dir;
    });
    rows.forEach(function (r) { tb.appendChild(r); });
  }
  ths.forEach(function (th, i) {
    if (th.dataset.nosort !== undefined) return;
    th.addEventListener("click", function () {
      var cur = th.getAttribute("aria-sort");
      var dir = cur === "descending" ? 1 : -1;
      ths.forEach(function (o) { o.removeAttribute("aria-sort");
                                 var s = o.querySelector(".ar"); if (s) s.remove(); });
      th.setAttribute("aria-sort", dir === -1 ? "descending" : "ascending");
      var s = document.createElement("span");
      s.className = "ar"; s.textContent = dir === -1 ? "\\u25bc" : "\\u25b2";
      th.appendChild(s);
      sortBy(i, dir);
    });
  });
})();
</script>
"""


def render_html(rows, pin, pin_label, stamp):
    esc = html.escape
    n_ranked = len([r for r in rows if r.get("rank")])
    out = [HTML_HEAD, '<div class="wrap">',
           f"<h1>buoy.finance — top {n_ranked} vaults by TVL</h1>",
           f'<p class="sub">Generated {esc(stamp)} UTC · time-weighted, net of fees and '
           f'funding · click any column to sort</p>',
           '<div class="scroll"><table><thead><tr>',
           '<th data-nosort title="Rank by TVL">#</th>',
           '<th data-nosort>Address</th>']
    for _, lbl, _, better in COLS:
        hint = {"hi": "higher is better", "lo": "lower is better"}.get(better, "")
        out.append(f'<th title="{esc(hint)}">{esc(lbl)}</th>')
    out.append("</tr></thead><tbody>")

    for r in rows:
        a = r["address"]
        pinned = bool(pin) and a.lower() == pin.lower()
        tag = f'<span class="tag">{esc(pin_label)}</span>' if pinned else ""
        m = r["m"]
        if "error" in m:
            flag = f'<span class="flag" title="{esc(m["error"])}">⚠</span>'
        elif not m.get("valid", True):
            flag = ('<span class="flag" title="chain contains an impossible period return '
                    '— annualised columns suppressed">⚠</span>')
        elif m.get("trimmed"):
            flag = (f'<span class="flag" title="earlier data contained an impossible period '
                    f'return (a deposit inside a coarse API gap); figures are computed on the '
                    f'clean {m["days"]:.1f}-day trailing window out of '
                    f'{m["trimmed_from_days"]:.1f} days of history">✂</span>')
        elif m.get("thin"):
            flag = ('<span class="flag" title="window under 30 days — annualised figures '
                    'are fragile">†</span>')
        else:
            flag = ""
        rank = str(r["rank"]) if r.get("rank") else "—"
        out.append(f'<tr><td>{rank}</td><td><span class="addr">{esc(a)}</span>{tag}{flag}</td>')
        for key, _, kind, better in COLS:
            txt, sv = cell(r, key, kind)
            cls = ""
            if sv is None:
                cls = "na"
            elif better == "hi":
                cls = "pos" if sv > 0 else ("neg" if sv < 0 else "")
            out.append(f'<td data-v="{"" if sv is None else sv}"'
                       f'{f" class={cls}" if cls else ""}>{esc(txt)}</td>')
        out.append("</tr>")

    out += ["</tbody></table></div>",
            '<div class="notes">',
            "<p><strong>Returns are time-weighted.</strong> Per-period returns are chained "
            "over Hyperliquid's <code>pnlHistory</code>, which already excludes deposits and "
            "withdrawals. Naive equity growth is not return — on a funded vault it can read "
            "several hundred percent while the trading return is a few percent.</p>",
            "<p><strong>TVL rank is not a performance rank.</strong> The table is ordered by "
            "TVL because that is what buoy publishes directly; sort by any other column to "
            "rank on performance instead.</p>",
            "<p><strong>†</strong> window shorter than 30 days — annualising that is fragile, "
            "since a few early days on a small balance dominate the compounding. "
            "<strong>✂</strong> earlier history contained an impossible period return, so the "
            "figures come from the clean trailing window only — the Window column shows how "
            "much survived. "
            "<strong>⚠</strong> the chain is invalid or unavailable, so annualised columns are "
            "suppressed rather than printed from an impossible period return (usually a "
            "deposit landing between two API samples). Hover either mark for the reason.</p>",
            "<p>Vaults are identified by address only. Source: "
            '<a href="https://buoy.finance">buoy.finance</a> for the vault list and TVL, '
            "Hyperliquid's public portfolio endpoint for returns. Method and code: "
            '<a href="https://github.com/zwallfacer/vault-perf">zwallfacer/vault-perf</a>.</p>',
            "</div></div>", HTML_JS]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--top", type=int, default=10, help="how many vaults by TVL (default 10)")
    ap.add_argument("--pin", default=os.environ.get("VAULT_ADDRESS"),
                    help="address always included and labelled (default $VAULT_ADDRESS)")
    ap.add_argument("--pin-label", default=os.environ.get("VAULT_NAME", "yours"),
                    help="label shown beside the pinned address (default $VAULT_NAME)")
    ap.add_argument("--harvest", action="store_true",
                    help="also append each vault's fine window to the local archive")
    ap.add_argument("--html", metavar="PATH", help="write the sortable HTML table here")
    ap.add_argument("--markdown", metavar="PATH", help="write the static Markdown table here")
    ap.add_argument("--json", metavar="PATH", help="write the machine-readable table here")
    a = ap.parse_args()

    if a.pin and not V.ADDR_RE.match(a.pin):
        raise SystemExit(f"!! --pin '{a.pin}' is not a valid address (expected 0x + 40 hex). "
                         f"A PRIVATE key is 0x + 64 hex -- never pass one to this or any script.")

    vaults = fetch_vaults()
    print(f"buoy: {len(vaults)} vaults listed", file=sys.stderr)
    rows = select(vaults, a.top, a.pin)

    for i, r in enumerate(rows):
        if i:
            time.sleep(REQ_GAP_S)
        r["m"] = metrics_for(r["address"], a.harvest)
        m = r["m"]
        note = m.get("error") or (f"{m['days']:.1f}d twr={m['twr'] * 100:+.2f}%"
                                  + ("" if m.get("valid") else " INVALID"))
        print(f"  {r.get('rank') or '-':>3}  {r['address']}  {note}", file=sys.stderr)

    stamp = dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M")
    ok = sum(1 for r in rows if "error" not in r["m"])
    if ok == 0:
        raise SystemExit("!! every vault failed -- refusing to publish an empty table")

    if a.html:
        os.makedirs(os.path.dirname(os.path.abspath(a.html)), exist_ok=True)
        open(a.html, "w").write(render_html(rows, a.pin, a.pin_label, stamp))
        print(f"wrote {a.html}", file=sys.stderr)
    if a.markdown:
        open(a.markdown, "w").write(render_markdown(rows, a.pin, a.pin_label, stamp))
        print(f"wrote {a.markdown}", file=sys.stderr)
    if a.json:
        os.makedirs(os.path.dirname(os.path.abspath(a.json)), exist_ok=True)
        json.dump({"generated": stamp, "source": "buoy.finance",
                   "rows": rows_payload(rows, a.pin, a.pin_label)},
                  open(a.json, "w"), indent=2, default=float)
        print(f"wrote {a.json}", file=sys.stderr)
    if not (a.html or a.markdown or a.json):
        sys.stdout.write(render_markdown(rows, a.pin, a.pin_label, stamp))
    print(f"{ok}/{len(rows)} vaults reported", file=sys.stderr)


if __name__ == "__main__":
    main()
