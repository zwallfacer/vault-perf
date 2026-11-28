# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-28 12:22 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,281 | +6.49% | +22.67% | +24.56% | 7.55% | +0.96 | +0.93 | +3.00 | 104.6d | $+483.16 |
| 2 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $4,878 | -3.59% | -81.30% | -56.31% | 6.32% | -4.72 | -4.12 | -12.87 | 16.1d | $-94.76 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,114 | -17.83% | -62.26% | -49.63% | 30.27% | -2.04 | -1.65 | -2.06 | 104.5d | $-906.29 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,870 | -13.82% | -56.30% | -45.44% | 30.76% | -1.30 | -1.04 | -1.83 | 89.6d | $-473.43 |
| 5 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,770 | -7.64% | -41.28% | -34.91% | 9.66% | -4.92 | -3.81 | -4.27 | 67.5d | $-230.99 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,548 | +3.52% | +11.22% | +11.66% | 43.98% | +0.30 | +0.31 | +0.26 | 114.5d | $-64.33 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,988 | +35.71% | +129.65% | +203.03% | 14.86% | +2.85 | +3.21 | +8.72 | 100.5d | $+522.80 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,781 | -50.52% | -190.96% | -93.00% | 76.93% | -0.57 | -0.55 | -2.48 | 96.6d | $-1,826.98 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,356 | -9.50% | -50.95% | -41.45% | 14.33% | -3.35 | -2.94 | -3.56 | 68.0d | $-142.45 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,305 | -12.98% | -72.25% | -53.88% | 14.76% | -6.14 | -5.12 | -4.89 | 65.6d | $-194.65 |
| 57 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
