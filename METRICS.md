# ML Yield Hunter — performance

_Generated 2026-09-16 20:30 UTC by [vault-perf](../../). Time-weighted, net of fees and funding._

| metric | value |
|---|---|
| Time-weighted return | **+15.20%** |
| APR (simple) | +214.4% |
| APY (compounded) | +635.8% |
| Max drawdown | 10.73% |
| Sharpe (rf=0) | +2.92 |
| Sortino (target=0) | +2.64 |
| Calmar (APR/maxDD) | +19.99 |

Window: **25.9 days**, 156 samples, median gap 2.33h.

> ⚠️ **26-day window.** Annualised figures are fragile at this
> length — a few early days on a small balance can dominate the compounding.
> Trailing 7d for comparison: TWR +5.23% → APR +275.9%.

> ⚠️ **25 daily observations.** Sharpe and Sortino need ~30+ to carry meaning;
> a single outlier day moves them materially.

> ⚠️ 2 period(s) carrying $+0.03 were excluded
> (starting equity below $1.00). The figures above do not represent that P&L.

Drawdown is measured on the time-weighted curve, not on account value — a
drawdown measured on a funded balance is meaningless. Sharpe and Sortino
resample to daily before annualising, because the raw sampling is irregular.
