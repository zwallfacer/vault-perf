# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-17 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,233 | +5.65% | +21.96% | +23.82% | 7.55% | +0.91 | +0.89 | +2.91 | 93.9d | $+441.45 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,187 | -3.17% | -14.68% | -13.86% | 18.94% | -0.27 | -0.23 | -0.77 | 79.0d | $-118.95 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,946 | -22.33% | -86.77% | -62.54% | 30.27% | -2.94 | -2.33 | -2.87 | 93.9d | $-1,076.74 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,840 | -5.05% | -32.38% | -28.27% | 5.86% | -4.58 | -3.63 | -5.53 | 56.9d | $-153.38 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,611 | +16.59% | +58.30% | +71.49% | 26.04% | +1.03 | +1.20 | +2.24 | 103.9d | $+45.71 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,558 | -1.43% | -94.75% | -61.49% | 1.78% | -7.13 | -7.79 | -53.23 | 5.5d | $-37.12 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -53.10% | -43.08% | 22.12% | -1.11 | -1.39 | -2.40 | 77.9d | $-464.92 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,095 | -39.25% | -166.69% | -87.96% | 66.51% | -0.50 | -0.51 | -2.51 | 85.9d | $-1,423.22 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,984 | +35.43% | +143.82% | +242.51% | 14.86% | +3.01 | +3.37 | +9.68 | 89.9d | $+518.66 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $1,397 | -39.55% | -150.43% | -85.26% | 77.96% | +0.14 | +0.16 | -1.93 | 96.0d | $-632.08 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
