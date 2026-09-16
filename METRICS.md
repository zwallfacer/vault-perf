# ML Yield Hunter — performance

_Generated 2026-09-16 08:50 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+11.94%** |
| APR (simple) | +171.6% |
| APY (compounded) | +406.0% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.42 |
| Sortino (target=0) | +2.16 |
| Calmar (APR/maxDD) | +16.00 |

Window: **25.4 days**, 142 samples, median gap 2.33h.

> ⚠️ **25-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +2.52% → APR +133.1%.

> ⚠️ **25 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
