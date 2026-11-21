# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-21 01:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,256 | +6.16% | +23.18% | +25.22% | 7.55% | +0.96 | +0.93 | +3.07 | 97.1d | $+466.87 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,075 | -18.86% | -70.91% | -54.43% | 30.27% | -2.28 | -1.82 | -2.34 | 97.1d | $-945.25 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,770 | -16.67% | -74.11% | -55.55% | 25.86% | -1.74 | -1.40 | -2.87 | 82.1d | $-568.43 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,765 | -7.72% | -46.92% | -38.63% | 8.32% | -5.68 | -4.30 | -5.64 | 60.1d | $-233.46 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,453 | -5.52% | -232.91% | -90.89% | 6.02% | -13.39 | -10.48 | -38.71 | 8.7d | $-143.38 |
| 6 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,992 | +35.87% | +140.70% | +232.80% | 14.86% | +2.98 | +3.31 | +9.47 | 93.1d | $+525.17 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $1,737 | -6.34% | -21.61% | -20.01% | 38.25% | -0.26 | -0.26 | -0.57 | 107.0d | $-370.46 |
| 8 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,340 | -10.75% | -64.81% | -49.62% | 12.11% | -4.46 | -4.00 | -5.35 | 60.6d | $-161.29 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,331 | -64.88% | -265.81% | -98.63% | 73.78% | -1.46 | -1.37 | -3.60 | 89.1d | $-2,341.36 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,297 | -13.48% | -84.69% | -59.74% | 13.81% | -7.66 | -6.05 | -6.13 | 58.1d | $-202.18 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
