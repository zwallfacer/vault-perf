# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-13 13:49 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` † | $13,459 | +7.14% | +88.02% | +134.01% | 21.13% | +1.18 | +1.07 | +4.17 | 29.6d |
| 2 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,982 | -14.13% | -409.92% | -98.80% | 9.05% | -5.10 | -5.47 | -45.29 | 12.6d |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` † | $4,929 | +12.53% | +159.74% | +350.40% | 4.89% | +3.66 | +7.09 | +32.63 | 28.6d |
| 4 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $4,870 | -37.85% | -585.51% | -99.94% | 52.89% | -4.80 | -3.39 | -11.07 | 23.6d |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,682 | +12.37% | +199.80% | +557.79% | 10.73% | +2.67 | +2.36 | +18.63 | 22.6d |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,876 | -10.56% | -156.77% | -80.93% | 35.61% | -2.96 | -2.18 | -4.40 | 24.6d |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $3,749 | +6.65% | +117.72% | +212.59% | 10.24% | +2.86 | +2.30 | +11.50 | 20.6d |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,403 | +1.29% | +34.64% | +41.08% | 0.84% | +4.19 | +8.36 | +41.07 | 13.6d |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` † | $2,870 | +5.34% | +68.19% | +94.32% | 1.80% | +4.48 | +4.18 | +37.92 | 28.6d |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,273 | +18.16% | +171.80% | +384.83% | 10.23% | +2.38 | +4.56 | +16.80 | 38.6d |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
