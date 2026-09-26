# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-26 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,891 | +60.01% | +510.61% | +5358.28% | 24.43% | +3.92 | +3.97 | +20.90 | 42.9d | $+6,841.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,541 | -50.09% | -495.80% | -99.90% | 69.24% | -2.02 | -1.91 | -7.16 | 36.9d | $-4,364.62 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,220 | +49.68% | +412.85% | +2755.28% | 43.59% | +2.79 | +3.67 | +9.47 | 43.9d | $+1,849.88 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,740 | +8.46% | +73.75% | +102.99% | 2.90% | +4.23 | +4.66 | +25.41 | 41.9d | $+214.59 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,714 | +32.90% | +354.21% | +2037.64% | 10.24% | +5.78 | +6.35 | +34.59 | 33.9d | $+1,159.31 |
| 6 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,663 | -5.82% | -50.66% | -40.66% | 7.55% | -2.03 | -1.82 | -6.71 | 41.9d | $-125.75 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,542 | -12.16% | -171.70% | -83.97% | 13.68% | -1.23 | -1.75 | -12.55 | 25.9d | $-638.27 |
| 8 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,194 | +0.52% | +5.30% | +5.43% | 16.00% | +0.44 | +0.41 | +0.33 | 35.9d | $-191.05 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,503 | +4.19% | +56.81% | +74.46% | 2.12% | +5.32 | +6.85 | +26.79 | 26.9d | $+132.14 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,278 | +29.61% | +208.39% | +520.50% | 10.23% | +3.12 | +5.15 | +20.37 | 51.9d | $+391.02 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
