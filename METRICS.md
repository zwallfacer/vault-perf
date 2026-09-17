# ML Yield Hunter — performance

_Generated 2026-09-17 20:30 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+13.92%** |
| APR (simple) | +189.0% |
| APY (compounded) | +486.9% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.67 |
| Sortino (target=0) | +2.52 |
| Calmar (APR/maxDD) | +17.62 |

Window: **26.9 days**, 171 samples, median gap 2.33h.

> ⚠️ **27-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +8.83% → APR +461.2%.

> ⚠️ **26 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
