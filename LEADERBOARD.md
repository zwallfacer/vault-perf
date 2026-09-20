# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-20 08:49 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $15,922 | +36.38% | +364.73% | +2143.64% | 24.43% | +3.16 | +3.26 | +14.93 | 36.4d | $+4,124.37 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,595 | -22.64% | -271.93% | -95.42% | 69.24% | -0.37 | -0.35 | -3.93 | 30.4d | $-1,748.00 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $6,476 | +49.68% | +484.39% | +5003.65% | 43.59% | +3.01 | +3.73 | +11.11 | 37.4d | $+1,849.89 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,851 | -0.03% | -0.27% | -0.27% | 5.83% | -0.13 | -0.12 | -0.05 | 35.4d | $+129.69 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,669 | +12.12% | +150.48% | +313.86% | 10.73% | +2.25 | +2.11 | +14.03 | 29.4d | $+292.24 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,668 | -9.75% | -183.72% | -85.53% | 13.68% | -0.85 | -1.17 | -13.43 | 19.4d | $-513.18 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,504 | +27.50% | +366.20% | +2440.93% | 10.24% | +5.62 | +6.51 | +35.76 | 27.4d | $+950.03 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,872 | +4.28% | +44.14% | +54.07% | 2.89% | +2.58 | +2.67 | +15.27 | 35.4d | $+58.76 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,493 | +3.87% | +69.24% | +97.26% | 1.18% | +6.24 | +11.01 | +58.72 | 20.4d | $+121.58 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,080 | +21.12% | +169.91% | +367.18% | 10.23% | +2.49 | +4.48 | +16.61 | 45.4d | $+245.18 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
