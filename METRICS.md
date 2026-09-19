# ML Yield Hunter — performance

_Generated 2026-09-19 08:18 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+11.80%** |
| APR (simple) | +151.8% |
| APY (compounded) | +320.0% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.24 |
| Sortino (target=0) | +2.14 |
| Calmar (APR/maxDD) | +14.15 |

Window: **28.4 days**, 194 samples, median gap 2.33h.

> ⚠️ **28-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +0.02% → APR +1.2%.

> ⚠️ **28 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 4 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
