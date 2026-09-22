# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-22 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,257 | +65.14% | +611.31% | +10977.56% | 24.43% | +4.35 | +4.34 | +25.02 | 38.9d | $+7,480.41 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,991 | -22.96% | -254.93% | -94.48% | 69.24% | -0.30 | -0.30 | -3.68 | 32.9d | $-1,379.85 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +454.22% | +3894.87% | 43.59% | +2.93 | +3.54 | +10.42 | 39.9d | $+1,849.89 |
| 4 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,852 | -6.57% | -109.69% | -67.85% | 13.68% | +0.21 | +0.32 | -8.02 | 21.9d | $-348.31 |
| 5 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,752 | -4.35% | -41.92% | -34.86% | 6.01% | -2.07 | -1.88 | -6.97 | 37.9d | $-53.38 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,685 | +33.65% | +410.80% | +3350.25% | 10.24% | +6.56 | +6.95 | +40.12 | 29.9d | $+1,164.72 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,231 | -0.28% | -3.20% | -3.16% | 13.79% | +0.34 | +0.31 | -0.23 | 31.9d | $-224.44 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,986 | +7.34% | +70.75% | +97.93% | 2.90% | +3.99 | +4.24 | +24.38 | 37.9d | $+172.49 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,539 | +5.23% | +83.33% | +125.31% | 1.18% | +8.06 | +13.17 | +70.67 | 22.9d | $+167.19 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,198 | +24.99% | +190.57% | +447.98% | 10.23% | +2.83 | +4.93 | +18.63 | 47.9d | $+309.80 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
