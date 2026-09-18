# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-18 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $16,045 | +33.34% | +348.70% | +1927.59% | 24.43% | +3.10 | +3.03 | +14.27 | 34.9d | $+3,908.07 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $9,742 | -20.78% | -262.69% | -94.74% | 69.24% | -0.25 | -0.24 | -3.79 | 28.9d | $-1,519.47 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $6,577 | +55.79% | +681.66% | +22415.91% | 43.59% | +2.97 | +3.65 | +15.64 | 29.9d | $+1,992.05 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,693 | -3.69% | -39.68% | -33.25% | 5.78% | -2.21 | -1.77 | -6.87 | 33.9d | $-76.66 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,636 | +11.30% | +147.88% | +305.95% | 10.73% | +2.20 | +2.15 | +13.79 | 27.9d | $+257.96 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,619 | -10.88% | -222.39% | -90.51% | 13.68% | -1.35 | -1.83 | -16.26 | 17.9d | $-571.78 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,465 | +27.91% | +393.30% | +3109.97% | 10.24% | +5.97 | +6.82 | +38.41 | 25.9d | $+964.16 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,936 | +6.93% | +74.68% | +105.86% | 2.51% | +4.48 | +4.46 | +29.73 | 33.9d | $+131.75 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,496 | +3.96% | +76.42% | +111.58% | 1.18% | +6.71 | +12.25 | +64.80 | 18.9d | $+124.43 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,089 | +21.73% | +180.83% | +413.62% | 10.23% | +2.65 | +4.84 | +17.68 | 43.9d | $+255.58 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
