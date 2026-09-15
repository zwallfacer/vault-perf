# ML Yield Hunter — performance

_Generated 2026-09-15 20:30 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+11.44%** |
| APR (simple) | +167.9% |
| APY (compounded) | +390.1% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.39 |
| Sortino (target=0) | +2.18 |
| Calmar (APR/maxDD) | +15.65 |

Window: **24.9 days**, 132 samples, median gap 2.33h.

> ⚠️ **25-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +2.58% → APR +135.7%.

> ⚠️ **24 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
