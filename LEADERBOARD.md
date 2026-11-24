# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-24 01:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,308 | +7.12% | +25.96% | +28.50% | 7.55% | +1.08 | +1.04 | +3.44 | 100.1d | $+514.08 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,073 | -18.94% | -69.07% | -53.50% | 30.27% | -2.25 | -1.81 | -2.28 | 100.1d | $-948.15 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,908 | -12.66% | -54.31% | -44.05% | 30.76% | -1.21 | -0.95 | -1.77 | 85.1d | $-435.00 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,804 | -6.45% | -37.33% | -32.01% | 9.66% | -4.38 | -3.39 | -3.86 | 63.1d | $-195.33 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,573 | +4.81% | +15.95% | +16.85% | 43.98% | +0.37 | +0.38 | +0.36 | 110.0d | $-32.64 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,503 | -3.62% | -113.49% | -68.52% | 6.02% | -5.79 | -5.07 | -18.86 | 11.7d | $-94.09 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,991 | +36.05% | +136.97% | +222.11% | 14.86% | +2.94 | +3.30 | +9.22 | 96.1d | $+527.74 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,413 | -60.04% | -237.99% | -97.36% | 75.60% | -1.13 | -1.06 | -3.15 | 92.1d | $-2,168.16 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,364 | -8.94% | -51.32% | -41.58% | 14.23% | -3.46 | -3.07 | -3.61 | 63.6d | $-134.05 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,326 | -11.55% | -69.01% | -51.97% | 14.76% | -5.78 | -4.92 | -4.68 | 61.1d | $-173.25 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
