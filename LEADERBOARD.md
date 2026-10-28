# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-28 10:01 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $14,184 | +15.57% | +76.34% | +103.29% | 57.56% | +1.36 | +1.19 | +1.33 | 74.5d | $+1,254.54 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,396 | -77.98% | -415.92% | -99.97% | 92.09% | -0.73 | -0.90 | -4.52 | 68.4d | $-10,954.91 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,069 | +2.53% | +12.59% | +13.24% | 7.55% | +0.52 | +0.51 | +1.67 | 73.5d | $+287.24 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,867 | -0.53% | -2.65% | -2.63% | 13.59% | +0.01 | +0.01 | -0.20 | 73.4d | $-246.95 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,573 | +7.29% | +45.51% | +55.15% | 2.72% | +4.24 | +4.33 | +16.72 | 58.5d | $+229.63 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,992 | -0.19% | -1.94% | -1.93% | 0.97% | -0.55 | -0.51 | -2.01 | 36.4d | $-7.79 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,937 | +14.25% | +68.88% | +90.40% | 47.44% | +1.19 | +1.38 | +1.45 | 75.5d | $+734.51 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,834 | +38.79% | +169.71% | +319.59% | 10.23% | +2.84 | +4.34 | +16.59 | 83.4d | $+525.47 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,627 | -28.41% | -158.39% | -84.48% | 55.42% | -0.70 | -0.70 | -2.86 | 65.5d | $-1,048.07 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -72.02% | -53.44% | 22.12% | -1.29 | -1.59 | -3.26 | 57.4d | $-464.89 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
