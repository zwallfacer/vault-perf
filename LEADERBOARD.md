# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-19 12:09 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,220 | +5.37% | +20.50% | +22.10% | 7.55% | +0.86 | +0.85 | +2.72 | 95.6d | $+427.31 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,188 | -4.73% | -21.41% | -19.70% | 18.94% | -0.41 | -0.35 | -1.13 | 80.6d | $-170.63 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,906 | -23.33% | -89.13% | -63.75% | 30.27% | -3.04 | -2.41 | -2.94 | 95.5d | $-1,114.61 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,840 | -5.41% | -33.75% | -29.32% | 6.31% | -4.32 | -3.42 | -5.35 | 58.5d | $-164.23 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,704 | +17.24% | +59.65% | +73.39% | 26.04% | +1.04 | +1.18 | +2.29 | 105.5d | $+60.59 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,552 | -1.73% | -88.81% | -59.18% | 2.43% | -6.62 | -6.59 | -36.53 | 7.1d | $-44.97 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,368 | -34.45% | -143.64% | -82.81% | 66.51% | -0.19 | -0.20 | -2.16 | 87.5d | $-1,251.54 |
| 8 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,988 | +36.06% | +143.81% | +241.45% | 14.86% | +3.03 | +3.30 | +9.68 | 91.5d | $+527.92 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $1,441 | -43.15% | -161.40% | -87.90% | 77.96% | +0.11 | +0.12 | -2.07 | 97.6d | $-721.65 |
| 10 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,401 | -6.74% | -41.71% | -35.07% | 10.89% | -2.96 | -2.81 | -3.83 | 59.0d | $-101.18 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
