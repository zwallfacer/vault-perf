# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-21 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,260 | +47.96% | +461.95% | +4253.38% | 24.43% | +3.70 | +3.64 | +18.91 | 37.9d | $+5,475.49 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $10,939 | -10.53% | -120.57% | -72.03% | 69.24% | +0.42 | +0.39 | -1.74 | 31.9d | $-258.70 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +465.89% | +4291.87% | 43.59% | +2.97 | +3.77 | +10.69 | 38.9d | $+1,849.89 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,858 | -2.24% | -22.12% | -20.04% | 6.01% | -1.19 | -1.11 | -3.68 | 36.9d | $+51.30 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,774 | -4.76% | -83.31% | -57.41% | 13.68% | +0.73 | +1.13 | -6.09 | 20.9d | $-254.62 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,591 | +32.44% | +409.77% | +3377.68% | 10.24% | +6.48 | +6.97 | +40.02 | 28.9d | $+1,122.57 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,531 | +8.41% | +99.39% | +159.68% | 10.73% | +1.65 | +1.59 | +9.27 | 30.9d | $+137.64 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,927 | +5.72% | +56.56% | +73.33% | 2.90% | +3.26 | +3.42 | +19.49 | 36.9d | $+112.03 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,523 | +4.97% | +82.76% | +124.28% | 1.18% | +7.89 | +13.12 | +70.19 | 21.9d | $+158.36 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,272 | +29.33% | +228.50% | +641.67% | 10.23% | +3.35 | +6.01 | +22.34 | 46.9d | $+386.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
