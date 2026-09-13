# ML Yield Hunter — performance

_Generated 2026-09-13 13:49 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+12.38%** |
| APR (simple) | +200.0% |
| APY (compounded) | +558.7% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.67 |
| Sortino (target=0) | +2.36 |
| Calmar (APR/maxDD) | +18.64 |

Window: **22.6 days**, 83 samples, median gap 2.33h.

> ⚠️ **23-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +3.95% → APR +206.7%.

> ⚠️ **22 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
