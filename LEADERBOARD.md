# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-22 08:48 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,052 | +46.45% | +441.44% | +3655.16% | 24.43% | +3.57 | +3.60 | +18.07 | 38.4d | $+5,299.34 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,984 | -25.31% | -285.28% | -96.27% | 69.24% | -0.44 | -0.43 | -4.12 | 32.4d | $-1,687.38 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +459.83% | +4081.15% | 43.59% | +2.93 | +3.54 | +10.55 | 39.4d | $+1,849.89 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,827 | -3.74% | -36.51% | -31.07% | 6.01% | -1.84 | -1.70 | -6.07 | 37.4d | $-23.18 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,712 | -7.01% | -119.67% | -71.08% | 13.68% | +0.09 | +0.13 | -8.75 | 21.4d | $-371.01 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,637 | +32.95% | +408.96% | +3328.80% | 10.24% | +6.45 | +6.82 | +39.94 | 29.4d | $+1,140.38 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,534 | +10.16% | +118.12% | +208.02% | 10.73% | +1.87 | +1.77 | +11.01 | 31.4d | $+210.62 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,970 | +6.92% | +67.58% | +92.21% | 2.90% | +3.83 | +4.01 | +23.29 | 37.4d | $+156.91 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,531 | +5.16% | +83.93% | +126.69% | 1.18% | +7.93 | +12.99 | +71.18 | 22.4d | $+164.69 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,226 | +27.96% | +215.47% | +568.54% | 10.23% | +3.18 | +5.75 | +21.06 | 47.4d | $+362.13 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
