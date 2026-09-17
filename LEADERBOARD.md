# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-17 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $14,203 | +10.15% | +109.31% | +183.25% | 24.43% | +1.69 | +1.55 | +4.47 | 33.9d | $+1,291.89 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $8,754 | -28.77% | -376.74% | -98.82% | 69.24% | -0.89 | -0.83 | -5.44 | 27.9d | $-2,502.09 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $4,903 | +15.61% | +197.33% | +525.66% | 43.59% | +1.05 | +1.05 | +4.53 | 28.9d | $+296.50 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,794 | -1.56% | -17.36% | -16.05% | 4.89% | -1.14 | -0.94 | -3.55 | 32.9d | $+26.62 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,748 | +13.92% | +189.01% | +486.85% | 10.73% | +2.67 | +2.52 | +17.62 | 26.9d | $+367.32 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,350 | +24.49% | +359.06% | +2382.09% | 10.24% | +5.44 | +6.29 | +35.07 | 24.9d | $+844.99 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,302 | -17.15% | -371.26% | -98.30% | 13.68% | -5.60 | -5.57 | -27.14 | 16.9d | $-896.53 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,447 | +2.49% | +50.69% | +64.98% | 1.18% | +5.14 | +8.17 | +42.98 | 17.9d | $+74.93 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,852 | +4.76% | +52.80% | +67.50% | 2.51% | +3.46 | +3.20 | +21.02 | 32.9d | $+52.96 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,031 | +18.56% | +158.07% | +326.31% | 10.23% | +2.29 | +4.36 | +15.45 | 42.9d | $+201.29 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
