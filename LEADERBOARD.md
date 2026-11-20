# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-20 12:11 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,258 | +6.10% | +23.06% | +25.08% | 7.55% | +0.96 | +0.93 | +3.06 | 96.6d | $+463.63 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,026 | -20.19% | -76.32% | -57.36% | 30.27% | -2.53 | -2.00 | -2.52 | 96.5d | $-995.52 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,956 | -11.70% | -52.35% | -42.69% | 18.94% | -1.28 | -1.06 | -2.76 | 81.6d | $-402.88 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,808 | -6.55% | -40.15% | -33.98% | 6.78% | -5.39 | -4.19 | -5.92 | 59.5d | $-198.30 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,478 | -4.58% | -205.81% | -87.84% | 4.73% | -14.34 | -11.88 | -43.51 | 8.1d | $-118.88 |
| 6 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,994 | +36.07% | +142.29% | +237.04% | 14.86% | +3.01 | +3.32 | +9.57 | 92.5d | $+528.06 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $1,931 | +4.31% | +14.78% | +15.57% | 29.05% | +0.32 | +0.36 | +0.51 | 106.5d | $-193.62 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,718 | -52.31% | -215.60% | -95.27% | 66.51% | -1.00 | -0.99 | -3.24 | 88.6d | $-1,891.10 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,370 | -9.50% | -57.75% | -45.49% | 10.89% | -4.14 | -3.76 | -5.30 | 60.0d | $-142.46 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,338 | -11.10% | -70.35% | -52.56% | 11.17% | -7.33 | -6.07 | -6.30 | 57.6d | $-166.39 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
