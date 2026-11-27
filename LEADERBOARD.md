# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-27 13:07 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,248 | +5.91% | +20.81% | +22.40% | 7.55% | +0.89 | +0.86 | +2.76 | 103.6d | $+454.03 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,037 | -19.85% | -69.96% | -54.15% | 30.27% | -2.34 | -1.91 | -2.31 | 103.6d | $-982.84 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,953 | -11.41% | -46.99% | -39.29% | 30.76% | -1.03 | -0.81 | -1.53 | 88.6d | $-393.19 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,811 | -6.31% | -34.62% | -30.07% | 9.66% | -4.02 | -3.12 | -3.58 | 66.6d | $-191.29 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,723 | +10.43% | +33.54% | +37.58% | 43.98% | +0.65 | +0.66 | +0.76 | 113.5d | $+105.85 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,509 | -3.40% | -81.98% | -56.57% | 6.32% | -4.55 | -3.92 | -12.98 | 15.2d | $-88.41 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,985 | +35.87% | +131.50% | +207.63% | 14.86% | +2.88 | +3.22 | +8.85 | 99.6d | $+525.14 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,940 | -45.99% | -175.59% | -90.48% | 76.93% | -0.35 | -0.34 | -2.28 | 95.6d | $-1,664.65 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,383 | -7.82% | -42.59% | -35.82% | 14.33% | -2.63 | -2.39 | -2.97 | 67.1d | $-117.38 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,330 | -11.34% | -64.04% | -49.32% | 14.76% | -5.34 | -4.42 | -4.34 | 64.6d | $-169.99 |
| 57 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
