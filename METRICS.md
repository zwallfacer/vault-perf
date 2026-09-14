# ML Yield Hunter — performance

_Generated 2026-09-14 09:13 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+12.33%** |
| APR (simple) | +192.2% |
| APY (compounded) | +512.7% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.60 |
| Sortino (target=0) | +2.43 |
| Calmar (APR/maxDD) | +17.92 |

Window: **23.4 days**, 104 samples, median gap 2.33h.

> ⚠️ **23-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +3.78% → APR +198.9%.

> ⚠️ **23 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
