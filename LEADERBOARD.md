# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-16 08:50 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,607 | +0.23% | +2.54% | +2.57% | 24.37% | +0.96 | +0.86 | +0.10 | 32.4d | $-39.27 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $7,791 | -39.96% | -552.73% | -99.91% | 69.24% | -2.12 | -1.90 | -7.98 | 26.4d | $-3,878.23 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,963 | +13.07% | +151.88% | +316.79% | 4.89% | +3.61 | +6.93 | +31.03 | 31.4d | $+192.94 |
| 4 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,772 | -18.46% | -438.18% | -99.21% | 13.04% | -6.99 | -6.87 | -33.61 | 15.4d | $-961.65 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,681 | +11.94% | +171.63% | +405.97% | 10.73% | +2.42 | +2.16 | +16.00 | 25.4d | $+284.86 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $3,950 | +14.99% | +233.68% | +782.38% | 10.24% | +4.25 | +4.00 | +22.82 | 23.4d | $+513.15 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,647 | -13.06% | -174.06% | -84.51% | 43.59% | -1.92 | -1.52 | -3.99 | 27.4d | $-913.34 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,399 | +0.86% | +19.20% | +21.07% | 1.18% | +2.13 | +3.14 | +16.29 | 16.4d | $+20.35 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,831 | +3.90% | +45.32% | +55.98% | 2.37% | +2.99 | +2.78 | +19.14 | 31.4d | $+30.89 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,167 | +19.28% | +170.14% | +373.87% | 10.23% | +2.42 | +4.54 | +16.63 | 41.4d | $+216.70 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
