# ML Yield Hunter — performance

_Generated 2026-09-16 14:27 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+15.23%** |
| APR (simple) | +216.9% |
| APY (compounded) | +652.8% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.93 |
| Sortino (target=0) | +2.64 |
| Calmar (APR/maxDD) | +20.22 |

Window: **25.6 days**, 149 samples, median gap 2.33h.

> ⚠️ **26-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +5.55% → APR +295.2%.

> ⚠️ **25 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
