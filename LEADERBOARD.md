# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-26 01:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,310 | +7.17% | +25.63% | +28.09% | 7.55% | +1.07 | +1.04 | +3.40 | 102.1d | $+516.66 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,046 | -19.60% | -70.08% | -54.16% | 30.27% | -2.32 | -1.88 | -2.32 | 102.1d | $-973.26 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,879 | -13.61% | -57.04% | -45.83% | 30.76% | -1.30 | -1.02 | -1.85 | 87.1d | $-466.57 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,791 | -6.93% | -38.87% | -33.16% | 9.66% | -4.55 | -3.50 | -4.02 | 65.1d | $-209.71 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,567 | +4.14% | +13.48% | +14.12% | 43.98% | +0.34 | +0.34 | +0.31 | 112.0d | $-49.13 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,490 | -4.14% | -110.66% | -67.70% | 6.32% | -6.03 | -5.14 | -17.52 | 13.7d | $-107.50 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,989 | +35.75% | +133.06% | +211.94% | 14.86% | +2.88 | +3.24 | +8.95 | 98.1d | $+523.35 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,450 | -59.55% | -231.04% | -97.02% | 76.93% | -1.09 | -1.01 | -3.00 | 94.1d | $-2,150.75 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,347 | -10.24% | -57.00% | -45.19% | 14.33% | -3.76 | -3.27 | -3.98 | 65.6d | $-153.56 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,320 | -11.95% | -69.12% | -52.11% | 14.76% | -5.78 | -4.80 | -4.68 | 63.1d | $-179.21 |
| 52 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
