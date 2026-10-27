# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-27 09:20 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $11,018 | -9.19% | -45.68% | -38.07% | 57.56% | +0.57 | +0.48 | -0.79 | 73.4d | $-1,784.83 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $8,117 | -80.81% | -437.56% | -99.99% | 92.09% | -0.97 | -1.20 | -4.75 | 67.4d | $-12,159.41 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,998 | +0.88% | +4.43% | +4.51% | 7.55% | +0.21 | +0.20 | +0.59 | 72.4d | $+205.35 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,755 | -3.32% | -16.72% | -15.64% | 13.59% | -0.60 | -0.50 | -1.23 | 72.4d | $-355.17 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,532 | +6.08% | +38.63% | +45.50% | 2.72% | +3.56 | +3.71 | +14.19 | 57.4d | $+189.31 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,983 | -0.51% | -5.21% | -5.09% | 0.97% | -1.65 | -1.55 | -5.38 | 35.4d | $-17.13 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,764 | +35.07% | +155.39% | +278.84% | 10.23% | +2.61 | +4.01 | +15.19 | 82.4d | $+449.66 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,534 | -30.98% | -175.52% | -87.76% | 55.42% | -0.86 | -0.87 | -3.17 | 64.4d | $-1,142.90 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,493 | -3.34% | -16.38% | -15.35% | 47.44% | +0.68 | +0.78 | -0.35 | 74.5d | $+281.43 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -73.34% | -54.08% | 22.12% | -1.30 | -1.64 | -3.32 | 56.4d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
