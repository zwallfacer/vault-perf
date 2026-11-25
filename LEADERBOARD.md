# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-25 13:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,377 | +8.46% | +30.41% | +33.89% | 7.55% | +1.26 | +1.20 | +4.03 | 101.6d | $+580.82 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,097 | -18.22% | -65.45% | -51.45% | 30.27% | -2.14 | -1.71 | -2.16 | 101.6d | $-920.94 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,792 | -16.39% | -69.06% | -52.96% | 30.76% | -1.64 | -1.30 | -2.24 | 86.6d | $-559.09 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,761 | -8.09% | -45.70% | -37.91% | 9.66% | -5.29 | -4.09 | -4.73 | 64.6d | $-244.41 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,453 | -5.58% | -154.68% | -79.64% | 6.02% | -8.55 | -7.56 | -25.71 | 13.2d | $-144.98 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,369 | -4.50% | -14.74% | -14.00% | 43.98% | -0.12 | -0.12 | -0.34 | 111.6d | $-261.82 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,991 | +36.05% | +134.85% | +216.32% | 14.86% | +2.93 | +3.27 | +9.07 | 97.6d | $+527.79 |
| 8 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,313 | -12.49% | -70.02% | -52.67% | 14.23% | -4.69 | -4.11 | -4.92 | 65.1d | $-187.26 |
| 9 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,305 | -13.14% | -76.58% | -56.00% | 14.76% | -6.50 | -5.49 | -5.19 | 62.6d | $-197.02 |
| 10 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,250 | -64.84% | -252.82% | -98.30% | 75.60% | -1.38 | -1.29 | -3.34 | 93.6d | $-2,340.00 |
| 51 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
