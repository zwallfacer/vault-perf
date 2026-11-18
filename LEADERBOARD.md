# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-18 12:15 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,200 | +5.08% | +19.62% | +21.10% | 7.55% | +0.82 | +0.80 | +2.60 | 94.6d | $+413.33 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,179 | -4.21% | -19.31% | -17.91% | 18.94% | -0.40 | -0.34 | -1.02 | 79.6d | $-153.45 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,948 | -22.21% | -85.77% | -62.09% | 30.27% | -2.90 | -2.29 | -2.83 | 94.5d | $-1,072.40 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,843 | -5.20% | -32.99% | -28.73% | 5.86% | -4.66 | -3.66 | -5.63 | 57.5d | $-157.87 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,622 | +14.83% | +51.80% | +62.09% | 26.04% | +0.93 | +1.07 | +1.99 | 104.5d | $+5.31 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,550 | -1.81% | -108.12% | -66.42% | 1.98% | -8.30 | -8.74 | -54.53 | 6.1d | $-47.09 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -52.68% | -42.83% | 22.12% | -1.11 | -1.39 | -2.38 | 78.5d | $-464.92 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,148 | -40.15% | -169.31% | -88.52% | 66.51% | -0.54 | -0.55 | -2.55 | 86.6d | $-1,455.52 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,989 | +35.80% | +144.35% | +243.47% | 14.86% | +3.03 | +3.32 | +9.71 | 90.5d | $+524.15 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $1,407 | -42.22% | -159.56% | -87.42% | 77.96% | +0.06 | +0.07 | -2.05 | 96.6d | $-698.57 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
