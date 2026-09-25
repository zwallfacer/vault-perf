# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-25 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,891 | +60.01% | +522.80% | +5905.06% | 24.43% | +3.97 | +4.06 | +21.40 | 41.9d | $+6,841.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,478 | -50.48% | -513.64% | -99.92% | 69.24% | -2.08 | -1.99 | -7.42 | 35.9d | $-4,424.22 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,220 | +49.68% | +422.47% | +2987.18% | 43.59% | +2.82 | +3.65 | +9.69 | 42.9d | $+1,849.88 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,738 | +33.45% | +371.09% | +2356.25% | 10.24% | +5.95 | +6.22 | +36.24 | 32.9d | $+1,178.85 |
| 5 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,643 | -6.15% | -54.87% | -43.24% | 6.78% | -2.24 | -2.04 | -8.09 | 40.9d | $-142.22 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,589 | -11.62% | -170.65% | -83.70% | 13.68% | -1.11 | -1.57 | -12.48 | 24.9d | $-610.19 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,213 | +0.99% | +10.35% | +10.85% | 16.00% | +0.51 | +0.48 | +0.65 | 34.9d | $-171.56 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,033 | +8.61% | +76.89% | +109.08% | 2.90% | +4.36 | +4.71 | +26.49 | 40.9d | $+219.59 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,512 | +4.40% | +62.03% | +83.49% | 2.12% | +5.64 | +7.48 | +29.25 | 25.9d | $+139.36 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,241 | +27.21% | +195.31% | +462.64% | 10.23% | +2.90 | +4.75 | +19.09 | 50.9d | $+348.95 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
