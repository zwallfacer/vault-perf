# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-26 13:09 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,313 | +7.22% | +25.68% | +28.14% | 7.55% | +1.08 | +1.05 | +3.40 | 102.6d | $+519.05 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,038 | -19.84% | -70.60% | -54.47% | 30.27% | -2.35 | -1.91 | -2.33 | 102.6d | $-982.41 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,904 | -12.83% | -53.46% | -43.57% | 30.76% | -1.21 | -0.95 | -1.74 | 87.6d | $-440.60 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,797 | -6.71% | -37.36% | -32.07% | 9.66% | -4.37 | -3.38 | -3.87 | 65.6d | $-203.22 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,545 | +3.41% | +11.05% | +11.47% | 43.98% | +0.30 | +0.30 | +0.25 | 112.5d | $-67.13 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,488 | -4.19% | -108.10% | -66.85% | 6.32% | -6.12 | -5.21 | -17.11 | 14.2d | $-108.90 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,990 | +35.96% | +133.17% | +211.92% | 14.86% | +2.90 | +3.22 | +8.96 | 98.6d | $+526.46 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,541 | -57.03% | -220.04% | -96.16% | 76.93% | -0.94 | -0.88 | -2.86 | 94.6d | $-2,060.14 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,342 | -10.53% | -58.20% | -45.94% | 14.33% | -3.89 | -3.44 | -4.06 | 66.1d | $-158.01 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,325 | -11.64% | -66.79% | -50.84% | 14.76% | -5.59 | -4.66 | -4.52 | 63.6d | $-174.55 |
| 54 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
