# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-25 08:43 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,477 | -22.69% | -116.00% | -73.17% | 57.56% | +0.03 | +0.02 | -2.02 | 71.4d | $-3,442.31 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,466 | -82.49% | -460.48% | -99.99% | 92.09% | -1.15 | -1.42 | -5.00 | 65.4d | $-12,874.55 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,078 | +2.76% | +14.30% | +15.15% | 7.55% | +0.57 | +0.56 | +1.90 | 70.4d | $+298.37 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,740 | -3.81% | -19.76% | -18.25% | 13.59% | -0.72 | -0.60 | -1.45 | 70.4d | $-374.36 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,525 | +5.86% | +38.62% | +45.54% | 2.72% | +3.51 | +3.74 | +14.19 | 55.4d | $+182.11 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,987 | -0.38% | -4.21% | -4.13% | 0.97% | -1.28 | -1.18 | -4.34 | 33.4d | $-13.50 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,857 | -21.40% | -125.15% | -75.54% | 55.42% | -0.37 | -0.37 | -2.26 | 62.4d | $-790.31 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,810 | +37.75% | +171.46% | +328.29% | 10.23% | +2.83 | +4.30 | +16.76 | 80.4d | $+504.34 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -76.07% | -55.40% | 22.12% | -1.33 | -1.67 | -3.44 | 54.4d | $-464.90 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,296 | -10.68% | -53.84% | -43.41% | 47.44% | +0.44 | +0.52 | -1.13 | 72.4d | $+92.28 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
