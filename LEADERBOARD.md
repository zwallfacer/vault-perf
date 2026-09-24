# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-24 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,641 | +60.01% | +535.58% | +6537.53% | 24.43% | +4.02 | +4.03 | +21.92 | 40.9d | $+6,841.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,805 | -43.10% | -451.05% | -99.73% | 69.24% | -1.46 | -1.36 | -6.51 | 34.9d | $-3,788.31 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +432.55% | +3250.44% | 43.59% | +2.86 | +3.49 | +9.92 | 41.9d | $+1,849.89 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,917 | +40.70% | +465.75% | +4877.21% | 10.24% | +7.43 | +7.69 | +45.49 | 31.9d | $+1,410.98 |
| 5 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,772 | -3.46% | -31.62% | -27.52% | 6.64% | -1.36 | -1.28 | -4.77 | 39.9d | $-9.07 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,627 | -10.50% | -160.62% | -81.68% | 13.68% | -0.85 | -1.22 | -11.74 | 23.9d | $-551.97 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,269 | +2.46% | +26.47% | +29.88% | 14.68% | +0.72 | +0.66 | +1.80 | 33.9d | $-110.39 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,031 | +8.57% | +78.44% | +112.24% | 2.90% | +4.38 | +4.81 | +27.03 | 39.9d | $+218.05 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,493 | +3.84% | +56.28% | +73.72% | 2.12% | +5.15 | +7.05 | +26.54 | 24.9d | $+120.46 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,304 | +31.24% | +228.74% | +631.92% | 10.23% | +3.38 | +5.72 | +22.36 | 49.9d | $+419.81 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
