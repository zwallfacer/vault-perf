# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-24 14:16 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,347 | +7.91% | +28.68% | +31.78% | 7.55% | +1.19 | +1.14 | +3.80 | 100.6d | $+553.22 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,091 | -18.45% | -66.92% | -52.28% | 30.27% | -2.18 | -1.76 | -2.21 | 100.6d | $-929.73 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,859 | -14.18% | -60.41% | -47.87% | 30.76% | -1.39 | -1.10 | -1.96 | 85.7d | $-485.41 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,787 | -7.01% | -40.23% | -34.11% | 9.66% | -4.75 | -3.70 | -4.16 | 63.6d | $-212.22 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,505 | +1.73% | +5.73% | +5.84% | 43.98% | +0.21 | +0.22 | +0.13 | 110.6d | $-108.26 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,481 | -4.48% | -133.93% | -74.59% | 6.02% | -7.23 | -6.55 | -22.26 | 12.2d | $-116.31 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,995 | +36.23% | +136.89% | +221.61% | 14.86% | +2.96 | +3.28 | +9.21 | 96.6d | $+530.46 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,428 | -60.12% | -236.88% | -97.33% | 75.60% | -1.13 | -1.06 | -3.13 | 92.6d | $-2,171.00 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,354 | -9.75% | -55.51% | -44.24% | 14.23% | -3.80 | -3.41 | -3.90 | 64.1d | $-146.25 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,321 | -11.93% | -70.60% | -52.85% | 14.76% | -5.98 | -5.08 | -4.78 | 61.7d | $-178.85 |
| 44 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
