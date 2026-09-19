# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-19 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $15,938 | +33.07% | +336.29% | +1727.14% | 24.43% | +3.04 | +3.04 | +13.76 | 35.9d | $+3,876.14 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $9,655 | -20.66% | -252.44% | -94.09% | 69.24% | -0.24 | -0.22 | -3.65 | 29.9d | $-1,504.78 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $6,621 | +50.83% | +502.45% | +5712.55% | 43.59% | +3.09 | +3.90 | +11.53 | 36.9d | $+1,899.46 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,787 | -1.84% | -19.21% | -17.62% | 5.83% | -1.06 | -0.94 | -3.29 | 34.9d | $+40.85 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,664 | +11.54% | +145.84% | +297.58% | 10.73% | +2.20 | +2.10 | +13.60 | 28.9d | $+268.14 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,664 | -10.24% | -198.17% | -87.64% | 13.68% | -1.05 | -1.42 | -14.49 | 18.9d | $-538.50 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,563 | +30.39% | +412.43% | +3564.30% | 10.24% | +6.32 | +7.08 | +40.28 | 26.9d | $+1,051.01 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,887 | +4.68% | +48.97% | +61.38% | 2.55% | +2.86 | +2.91 | +19.21 | 34.9d | $+73.59 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,507 | +4.22% | +77.37% | +113.35% | 1.18% | +7.08 | +12.36 | +65.61 | 19.9d | $+133.21 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,136 | +23.97% | +195.01% | +474.40% | 10.23% | +2.87 | +5.20 | +19.07 | 44.9d | $+293.96 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
