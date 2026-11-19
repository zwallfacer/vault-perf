# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-19 23:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,234 | +5.66% | +21.51% | +23.27% | 7.55% | +0.90 | +0.88 | +2.85 | 96.0d | $+441.69 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,075 | -7.76% | -34.95% | -30.50% | 18.94% | -0.81 | -0.68 | -1.84 | 81.0d | $-271.58 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,974 | -21.52% | -81.84% | -60.21% | 30.27% | -2.77 | -2.18 | -2.70 | 96.0d | $-1,046.12 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,815 | -6.17% | -38.18% | -32.57% | 6.43% | -5.13 | -3.98 | -5.94 | 59.0d | $-186.95 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,502 | -3.69% | -177.75% | -83.65% | 3.84% | -12.36 | -10.86 | -46.29 | 7.6d | $-95.72 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,059 | +11.67% | +40.20% | +46.25% | 26.04% | +0.75 | +0.83 | +1.54 | 106.0d | $-58.35 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,052 | -42.39% | -175.80% | -89.84% | 66.51% | -0.58 | -0.58 | -2.64 | 88.0d | $-1,535.69 |
| 8 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,992 | +36.13% | +143.40% | +240.14% | 14.86% | +3.04 | +3.31 | +9.65 | 92.0d | $+529.02 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,389 | -7.40% | -45.40% | -37.61% | 10.89% | -3.33 | -3.10 | -4.17 | 59.5d | $-110.98 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,342 | -10.58% | -67.69% | -51.10% | 10.73% | -7.06 | -5.83 | -6.31 | 57.0d | $-158.58 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
