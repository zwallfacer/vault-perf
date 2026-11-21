# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-21 11:47 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,264 | +6.23% | +23.30% | +25.36% | 7.55% | +0.97 | +0.94 | +3.09 | 97.5d | $+469.88 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,087 | -18.56% | -69.47% | -53.63% | 30.27% | -2.23 | -1.78 | -2.30 | 97.5d | $-933.98 |
| 3 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,754 | -8.14% | -49.11% | -40.09% | 9.66% | -5.99 | -4.57 | -5.08 | 60.5d | $-246.10 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,682 | -19.47% | -86.11% | -61.62% | 30.76% | -2.06 | -1.64 | -2.80 | 82.5d | $-661.86 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,455 | -5.45% | -218.65% | -89.44% | 6.02% | -13.11 | -10.35 | -36.34 | 9.1d | $-141.60 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,208 | -10.31% | -35.01% | -30.89% | 43.98% | -0.49 | -0.50 | -0.80 | 107.5d | $-404.75 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,993 | +36.18% | +141.25% | +233.87% | 14.86% | +3.01 | +3.29 | +9.50 | 93.5d | $+529.76 |
| 8 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,327 | -11.48% | -68.67% | -51.78% | 14.23% | -4.74 | -4.21 | -4.83 | 61.0d | $-172.16 |
| 9 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,308 | -12.81% | -79.82% | -57.43% | 14.76% | -7.09 | -5.72 | -5.41 | 58.6d | $-192.02 |
| 10 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,270 | -64.52% | -263.02% | -98.54% | 75.15% | -1.44 | -1.35 | -3.50 | 89.5d | $-2,328.55 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
