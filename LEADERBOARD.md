# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-23 13:40 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,294 | +6.88% | +25.20% | +27.60% | 7.55% | +1.05 | +1.01 | +3.34 | 99.6d | $+502.23 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,096 | -18.27% | -66.96% | -52.26% | 30.27% | -2.17 | -1.73 | -2.21 | 99.6d | $-922.95 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,890 | -13.17% | -56.79% | -45.61% | 30.76% | -1.28 | -1.01 | -1.85 | 84.6d | $-451.81 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,803 | -6.47% | -37.71% | -32.28% | 9.66% | -4.43 | -3.45 | -3.90 | 62.6d | $-195.83 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,526 | +2.97% | +9.90% | +10.25% | 43.98% | +0.28 | +0.28 | +0.23 | 109.6d | $-77.81 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,477 | -4.64% | -151.43% | -78.79% | 6.02% | -8.94 | -7.15 | -25.17 | 11.2d | $-120.45 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,995 | +36.20% | +138.25% | +225.41% | 14.86% | +2.97 | +3.26 | +9.30 | 95.6d | $+530.04 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,489 | -58.30% | -232.26% | -96.93% | 75.60% | -1.02 | -0.96 | -3.07 | 91.6d | $-2,105.66 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,366 | -8.87% | -51.31% | -41.57% | 14.23% | -3.46 | -3.11 | -3.61 | 63.1d | $-133.03 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,330 | -11.22% | -67.52% | -51.14% | 14.76% | -5.66 | -4.69 | -4.57 | 60.6d | $-168.19 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
