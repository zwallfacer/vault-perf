# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-03 11:20 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $11,972 | -3.64% | -16.49% | -15.46% | 57.56% | +0.80 | +0.69 | -0.29 | 80.5d | $-1,103.24 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,340 | +7.97% | +36.61% | +42.22% | 7.55% | +1.39 | +1.38 | +4.85 | 79.5d | $+556.33 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $3,623 | -91.61% | -448.85% | -100.00% | 92.52% | -1.74 | -2.02 | -4.85 | 74.5d | $-16,763.04 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,563 | -8.41% | -38.62% | -33.20% | 17.18% | -1.41 | -1.12 | -2.25 | 79.5d | $-553.19 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,508 | +5.31% | +30.02% | +33.97% | 4.68% | +2.18 | +1.95 | +6.41 | 64.5d | $+163.55 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,121 | +20.33% | +91.01% | +128.99% | 47.44% | +1.30 | +1.63 | +1.92 | 81.5d | $+891.33 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,968 | -1.05% | -8.98% | -8.63% | 1.43% | -2.50 | -2.08 | -6.27 | 42.5d | $-33.31 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,803 | +36.91% | +150.58% | +260.25% | 10.23% | +2.60 | +4.00 | +14.72 | 89.5d | $+487.21 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,769 | -25.16% | -128.43% | -77.22% | 60.35% | -0.29 | -0.32 | -2.13 | 71.5d | $-928.82 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -65.15% | -49.92% | 22.12% | -1.23 | -1.53 | -2.95 | 63.5d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
