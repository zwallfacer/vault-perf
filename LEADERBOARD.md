# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-17 08:54 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,972 | +0.88% | +9.60% | +10.03% | 24.43% | +1.01 | +0.88 | +0.39 | 33.4d | $+97.30 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $8,372 | -31.80% | -423.76% | -99.39% | 69.24% | -1.19 | -1.09 | -6.12 | 27.4d | $-2,874.76 |
| 3 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,814 | +15.52% | +214.64% | +635.38% | 10.73% | +2.92 | +2.58 | +20.01 | 26.4d | $+434.13 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,799 | -1.64% | -18.44% | -16.96% | 4.89% | -1.17 | -0.96 | -3.77 | 32.4d | $+23.09 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,429 | +26.81% | +400.74% | +3382.61% | 10.24% | +5.80 | +6.85 | +39.14 | 24.4d | $+925.74 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,256 | -17.77% | -396.13% | -98.72% | 13.68% | -6.10 | -5.94 | -28.96 | 16.4d | $-928.89 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $4,218 | +0.26% | +3.30% | +3.35% | 43.59% | -0.35 | -0.29 | +0.08 | 28.4d | $-351.36 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,423 | +1.85% | +38.73% | +46.77% | 1.18% | +4.31 | +6.06 | +32.84 | 17.4d | $+53.47 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,872 | +5.49% | +61.83% | +82.57% | 2.51% | +3.85 | +3.67 | +24.61 | 32.4d | $+72.89 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,270 | +20.20% | +174.04% | +388.02% | 10.23% | +2.50 | +4.63 | +17.01 | 42.4d | $+232.38 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
