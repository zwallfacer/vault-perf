# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-25 01:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,360 | +8.24% | +29.77% | +33.12% | 7.55% | +1.23 | +1.18 | +3.95 | 101.1d | $+569.93 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,078 | -18.80% | -67.88% | -52.86% | 30.27% | -2.22 | -1.80 | -2.24 | 101.1d | $-942.88 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,842 | -14.74% | -62.47% | -49.13% | 30.76% | -1.44 | -1.15 | -2.03 | 86.1d | $-504.05 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,775 | -7.43% | -42.32% | -35.58% | 9.66% | -4.96 | -3.87 | -4.38 | 64.1d | $-224.68 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,476 | -4.68% | -135.16% | -74.95% | 6.02% | -7.27 | -6.67 | -22.46 | 12.7d | $-121.67 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,426 | -1.62% | -5.32% | -5.23% | 43.98% | +0.03 | +0.03 | -0.12 | 111.0d | $-190.83 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,995 | +36.22% | +136.23% | +219.80% | 14.86% | +2.94 | +3.29 | +9.17 | 97.1d | $+530.32 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,355 | -62.48% | -245.00% | -97.86% | 75.60% | -1.26 | -1.18 | -3.24 | 93.1d | $-2,255.57 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,325 | -11.75% | -66.42% | -50.66% | 14.23% | -4.45 | -3.93 | -4.67 | 64.6d | $-176.20 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,312 | -12.49% | -73.38% | -54.33% | 14.76% | -6.18 | -5.25 | -4.97 | 62.1d | $-187.22 |
| 50 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
