# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-04 11:34 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,056 | +6.03% | +26.98% | +29.95% | 57.56% | +1.07 | +0.93 | +0.47 | 81.5d | $+82.78 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $5,679 | -86.79% | — | — | — | — | — | — | 75.5d | $-14,709.33 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,334 | +7.82% | +35.43% | +40.66% | 7.55% | +1.36 | +1.36 | +4.70 | 80.5d | $+548.53 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,771 | -3.11% | -14.11% | -13.35% | 17.18% | -0.38 | -0.32 | -0.82 | 80.5d | $-347.16 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,544 | +6.47% | +36.02% | +41.77% | 4.68% | +2.60 | +2.33 | +7.69 | 65.5d | $+202.24 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,378 | +30.92% | +136.72% | +229.13% | 47.44% | +1.52 | +1.89 | +2.88 | 82.6d | $+1,164.14 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,264 | -8.65% | -43.52% | -36.57% | 60.35% | +0.41 | +0.46 | -0.72 | 72.5d | $-321.36 |
| 8 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,977 | -0.68% | -5.73% | -5.58% | 1.43% | -1.52 | -1.31 | -4.00 | 43.5d | $-22.43 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,929 | +43.63% | +176.02% | +330.89% | 10.23% | +2.96 | +4.58 | +17.21 | 90.5d | $+624.54 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -64.13% | -49.37% | 22.12% | -1.22 | -1.51 | -2.90 | 64.5d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
