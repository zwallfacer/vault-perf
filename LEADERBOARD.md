# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-25 09:06 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,891 | +60.01% | +528.80% | +6193.98% | 24.43% | +3.97 | +3.94 | +21.64 | 41.4d | $+6,841.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,661 | -49.32% | -508.59% | -99.91% | 69.24% | -1.98 | -1.91 | -7.35 | 35.4d | $-4,249.34 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +427.21% | +3108.11% | 43.59% | +2.82 | +3.53 | +9.80 | 42.4d | $+1,849.89 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,814 | +38.07% | +428.63% | +3678.89% | 10.24% | +6.86 | +7.43 | +41.86 | 32.4d | $+1,319.24 |
| 5 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,737 | -4.23% | -38.18% | -32.30% | 6.64% | -1.63 | -1.54 | -5.75 | 40.4d | $-47.24 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,567 | -11.46% | -171.51% | -83.82% | 13.68% | -1.06 | -1.51 | -12.54 | 24.4d | $-601.63 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,052 | -2.92% | -30.97% | -26.97% | 16.00% | -0.01 | -0.01 | -1.94 | 34.4d | $-334.43 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,033 | +8.61% | +77.77% | +110.87% | 2.90% | +4.36 | +4.71 | +26.80 | 40.4d | $+219.52 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,500 | +4.14% | +59.40% | +78.96% | 2.12% | +5.36 | +7.04 | +28.01 | 25.4d | $+130.48 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,294 | +30.24% | +219.11% | +578.23% | 10.23% | +3.24 | +5.54 | +21.42 | 50.4d | $+402.22 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
