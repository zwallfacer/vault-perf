# ML Yield Hunter — performance

_Generated 2026-09-19 20:30 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+11.54%** |
| APR (simple) | +145.8% |
| APY (compounded) | +297.6% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.20 |
| Sortino (target=0) | +2.10 |
| Calmar (APR/maxDD) | +13.60 |

Window: **28.9 days**, 202 samples, median gap 2.33h.

> ⚠️ **29-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR -0.67% → APR -35.3%.

> ⚠️ **28 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 4 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
