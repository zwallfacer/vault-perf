# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-16 14:27 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,905 | +2.60% | +29.09% | +33.27% | 24.37% | +1.16 | +1.03 | +1.19 | 32.6d | $+255.43 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $7,460 | -40.03% | -548.90% | -99.91% | 69.24% | -2.13 | -1.91 | -7.93 | 26.6d | $-3,887.40 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,931 | +12.87% | +148.44% | +304.04% | 4.89% | +3.56 | +7.13 | +30.33 | 31.6d | $+184.13 |
| 4 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,862 | -17.23% | -403.05% | -98.80% | 13.04% | -6.19 | -5.92 | -30.92 | 15.6d | $-890.81 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,700 | +15.23% | +216.90% | +653.00% | 10.73% | +2.93 | +2.64 | +20.22 | 25.6d | $+421.91 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,058 | +13.78% | +212.72% | +633.65% | 10.24% | +4.00 | +3.66 | +20.78 | 23.6d | $+470.96 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $4,033 | -7.94% | -104.88% | -66.47% | 43.59% | -1.26 | -1.03 | -2.41 | 27.6d | $-697.11 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,401 | +0.95% | +20.84% | +23.05% | 1.18% | +2.36 | +3.48 | +17.67 | 16.7d | $+23.27 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,825 | +3.80% | +43.86% | +53.79% | 2.37% | +2.87 | +2.66 | +18.52 | 31.6d | $+26.92 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,285 | +20.66% | +181.24% | +419.41% | 10.23% | +2.59 | +4.73 | +17.72 | 41.6d | $+240.95 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
