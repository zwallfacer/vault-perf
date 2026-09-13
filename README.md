# vault-perf

Time-weighted return, APR/APY and risk ratios for any **Hyperliquid** account.

```bash
./vault_perf_github.py 0x<address>
```

Read-only. It calls Hyperliquid's public `/info` endpoint with a **public address**.
No keys, no signing, no orders — there is no code path in this script that could
place a trade.

---

## Why not just look at the balance?

**Equity growth is not return.** An account that doubles may have done so entirely
through deposits. On one funded account we measured, naive equity growth read
**+444%** where the actual trading return was **+12%**.

The fix is a time-weighted return — chain each period's return on the capital that
was actually at work during it:

```
r_i = (pnl[i] - pnl[i-1]) / accountValue[i-1]      TWR = prod(1 + r_i) - 1
```

Hyperliquid's `pnlHistory` already excludes deposits and withdrawals, so the
numerator is trading P&L alone. That is what makes the result time-weighted rather
than money-weighted — and it is net of **fees and funding**, since those reduce
equity and are not external flows.

## Why an archive?

The API is not a viable long-term source, because **its resolution decays**. The
`allTime` window is a fixed budget of ~45-70 samples stretched over the account's
whole life, so the gap between samples grows as the account ages:

| account age | window | samples | median gap |
|---|---|---|---|
| 24 days | `allTime` | ~44 | 8.7 h |
| 428 days | `allTime` | ~67 | **167.7 h (7 days)** |
| any | `week` | ~62 | **2.3 h** |

Coarse sampling does not merely blur the answer, it **invalidates** it. A deposit
that lands and trades between two samples puts the wrong denominator under the P&L.
On a 7-day-gapped series we measured sub-periods of **−222%** — a $292 loss against
a $131 equity sample. A return past −100% is impossible; it is a sampling artifact.

So `--harvest` copies the fine `week` window into an append-only local archive:

```bash
./vault_perf_github.py 0x<address> --harvest     # run daily (cron / CI)
```

`week` covers 7 days, so a daily harvest overlaps ~7× and cannot gap. Miss a day and
the next run backfills it. Run it for a month and you have 2.3 h resolution over a
period where the API would only offer 7-day gaps.

## What it refuses to do

A confident wrong number is worse than no number, so there are three guards:

- **Near-zero divisors are excluded, and said so.** A period starting below
  `MIN_EQUITY` is dropped — but the count and the P&L it carried are always printed.
- **An impossible chain is refused outright.** If any period exceeds ±50%, no TWR,
  APR, APY or ratio is reported. That pattern means the equity sample does not
  represent the capital at risk, and everything built on it would be noise. The
  offending periods are listed so you can see why.
- **Thin windows are flagged.** Annualising under 30 days prints a warning and the
  trailing-7-day figure alongside, because a few early days on a small balance can
  dominate the compounding.

## The ratios

| metric | how |
|---|---|
| max drawdown | on the **TWR curve**, never on account value — a drawdown measured on a funded balance is meaningless |
| Sharpe | daily-resampled returns, `mean/sd × √365`, risk-free = 0 |
| Sortino | same, against downside deviation with target 0; `n/a` rather than ∞ when there are no losing days |
| Calmar | APR ÷ max drawdown |

Sharpe and Sortino **resample to daily first**. Sampling is irregular, and a 9 h
period carries ~4× the variance of a 2.3 h one — feeding that heterogeneous series
straight to a standard deviation would mis-state volatility.

## Output

```
0x...   source=api
  equity   $861.97 -> $4,789.66   (this change includes DEPOSITS; it is not return)
  P&L      $+303.07   over 20.66 days from 104 points, median gap 2.33h (max 25.00h)

  date        equity@start       PnL     return
  2026-08-25        867.97    -93.10   -10.727%
  2026-08-26        774.86   +104.47   +13.482%
  ...

  time-weighted return   +12.011%
  APR (simple)           +212.2%
  APY (compounded)       +641.8%

  max drawdown           10.73%   (on the TWR curve, not account value)
  Sharpe  (rf=0)         +2.73
  Sortino (target=0)     +2.31
  Calmar  (APR / maxDD)  +19.78
  !! 20 daily observations - these ratios are indicative only.
```

`--json` emits the same figures machine-readably, including `valid`, `n_extreme` and
`skipped_n` so a caller cannot accidentally consume a refused result.

## Options

| flag | meaning |
|---|---|
| `--harvest` | append the current fine window to the local archive, then exit |
| `--source archive\|api\|merged` | default: archive if one exists for this address, else api |
| `-w, --window` | restrict the API side to one window (default: `allTime`+`month`+`week` normalised together, which is finer) |
| `--json` | machine-readable |
| `--no-color` | plain text (automatic when piped) |

Archive location defaults to `./vault_equity/<address>.jsonl`; override with
`VAULT_ARCHIVE_DIR`.

## Implementation note: why points, not deltas

`pnlHistory` is **window-relative** — every window restarts at 0 — while
`accountValue` is absolute. Each finer window is therefore shifted onto the
`allTime` window's absolute scale using the constant offset measured at their shared
timestamps (verified constant to 1e-6 across every shared point).

Once stored absolute, archive points dedup by timestamp, cannot overlap, and a
larger time step is simply a larger step. An earlier design stored `(t0 → t1)`
segments instead and needed a dynamic-programming tiling pass to avoid double
counting; storing absolute points removes that problem rather than solving it.

## The buoy leaderboard

`buoy_leaderboard.py` ranks the top buoy.finance vaults by TVL and reports the same
time-weighted metrics for each, so a TVL ranking can be re-sorted into a performance
ranking.

```
./buoy_leaderboard.py --top 10 --pin 0xYOUR_VAULT --pin-label "Your vault" \
    --html docs/index.html --markdown LEADERBOARD.md --json docs/leaderboard.json
```

- **Vaults are identified by address only.** Names are not published — the address is
  the one identifier that is unambiguous and self-verifiable. `--pin` guarantees one
  address is always in the table even if it falls out of the top N, and labels it.
- **TVL rank is not a performance rank.** It leads because it is what buoy publishes
  directly; the HTML table sorts on any column.
- **Validity is per vault.** A chain containing an impossible period return — nearly
  always a deposit landing inside one of the API's coarse `allTime` gaps — is re-chained
  on the clean trailing window and marked `✂`, with the Window column showing how much
  survived. If no clean window of at least 7 days remains, the annualised columns are
  suppressed (`⚠`) rather than printed from a figure that cannot be true. A window under
  30 days is marked `†`.

Published outputs: `LEADERBOARD.md` (static, renders on GitHub), `docs/index.html`
(sortable, served by GitHub Pages) and `docs/leaderboard.json`.

To serve the sortable table: Settings → Pages → Source **Deploy from a branch** →
branch `main`, folder `/docs`.

## Daily metrics via GitHub Actions

`.github/workflows/daily-metrics.yml` harvests once a day and publishes **only the
rolled-up figures** — `METRICS.md` and `metrics.json`.

What is and is not published:

| | |
|---|---|
| published | TWR, APR, APY, max drawdown, Sharpe, Sortino, Calmar, window length, sample counts |
| **not** published | the equity series itself, any account value, any P&L total, the address |

The series lives in the **Actions cache**, which is not publicly downloadable, and
stays `.gitignore`d. Absolute-dollar fields are stripped from `metrics.json` before
commit — committed daily, an equity figure becomes a balance history in `git log`,
which is exactly the granular disclosure a metrics report should avoid. A `grep`
guard fails the run if an address ever reaches a published file.

No fills, prices, sizes or positions are involved anywhere in this repository.

Setup:

1. Repository secret `VAULT_ADDRESS` — the public address to report on.
2. Repository variable `VAULT_NAME` — the display name for the report.
3. Settings → Actions → General → Workflow permissions → **Read and write**.

Caches evict after 7 days without access, so a daily run keeps the archive warm. If
the workflow breaks for longer the archive rebuilds from the API's current window —
costing historical resolution, not correctness: the tool refuses to report rather
than publish a figure it cannot stand behind.

## Requirements

Python 3.11+ and `requests`. Nothing else.

```bash
pip install requests
```

## Licence

MIT.
