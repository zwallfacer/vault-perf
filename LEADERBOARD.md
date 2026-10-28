# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-28 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,888 | +11.31% | +55.11% | +68.55% | 57.56% | +1.24 | +1.08 | +0.96 | 74.9d | $+731.85 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,465 | -77.88% | -412.46% | -99.97% | 92.09% | -0.72 | -0.89 | -4.48 | 68.9d | $-10,908.82 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,078 | +2.72% | +13.44% | +14.18% | 7.55% | +0.55 | +0.54 | +1.78 | 73.9d | $+296.54 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,852 | -1.02% | -5.04% | -4.94% | 13.59% | -0.09 | -0.08 | -0.37 | 73.9d | $-265.86 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,572 | +7.06% | +43.68% | +52.52% | 2.72% | +4.12 | +4.19 | +16.05 | 59.0d | $+221.81 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,991 | -0.26% | -2.54% | -2.51% | 0.97% | -0.76 | -0.71 | -2.63 | 36.9d | $-9.68 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,832 | +8.63% | +41.48% | +48.86% | 47.44% | +1.04 | +1.22 | +0.87 | 76.0d | $+589.92 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,828 | +38.05% | +165.54% | +306.68% | 10.23% | +2.79 | +4.26 | +16.18 | 83.9d | $+510.48 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,497 | -34.00% | -188.18% | -89.97% | 55.42% | -0.99 | -0.98 | -3.40 | 65.9d | $-1,253.69 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -71.43% | -53.14% | 22.12% | -1.29 | -1.61 | -3.23 | 57.9d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
