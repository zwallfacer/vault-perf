# ML Yield Hunter — performance

_Generated 2026-09-18 20:30 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+11.31%** |
| APR (simple) | +148.1% |
| APY (compounded) | +306.8% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.20 |
| Sortino (target=0) | +2.15 |
| Calmar (APR/maxDD) | +13.81 |

Window: **27.9 days**, 187 samples, median gap 2.33h.

> ⚠️ **28-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR -1.05% → APR -55.9%.

> ⚠️ **27 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 4 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
