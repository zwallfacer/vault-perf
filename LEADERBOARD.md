# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-18 23:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,205 | +5.41% | +20.77% | +22.41% | 7.55% | +0.87 | +0.85 | +2.75 | 95.0d | $+429.22 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,107 | -7.77% | -35.43% | -30.85% | 18.94% | -0.82 | -0.69 | -1.87 | 80.0d | $-271.94 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,954 | -22.09% | -84.88% | -61.68% | 30.27% | -2.88 | -2.27 | -2.80 | 95.0d | $-1,067.64 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,817 | -6.08% | -38.27% | -32.62% | 6.31% | -5.09 | -3.93 | -6.07 | 58.0d | $-184.24 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,553 | +10.71% | +37.26% | +42.47% | 26.04% | +0.70 | +0.78 | +1.43 | 105.0d | $-89.05 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,537 | -2.27% | -126.41% | -72.16% | 2.43% | -9.62 | -9.48 | -51.99 | 6.6d | $-59.08 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,991 | +35.92% | +144.13% | +242.61% | 14.86% | +3.04 | +3.33 | +9.70 | 91.0d | $+525.93 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,947 | -47.92% | -201.05% | -93.52% | 66.51% | -0.85 | -0.85 | -3.02 | 87.0d | $-1,734.04 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,385 | -7.96% | -49.70% | -40.42% | 10.89% | -3.68 | -3.44 | -4.56 | 58.5d | $-119.44 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,343 | -10.56% | -68.82% | -51.68% | 10.73% | -7.17 | -5.85 | -6.41 | 56.0d | $-158.39 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
