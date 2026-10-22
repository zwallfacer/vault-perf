# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-22 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,246 | -24.60% | -130.32% | -77.59% | 57.56% | -0.12 | -0.10 | -2.26 | 68.9d | $-3,676.24 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,085 | +2.82% | +15.17% | +16.14% | 7.55% | +0.60 | +0.59 | +2.01 | 67.9d | $+301.45 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,836 | -1.31% | -7.02% | -6.82% | 13.59% | -0.18 | -0.15 | -0.52 | 67.9d | $-276.93 |
| 4 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $3,557 | -91.66% | -532.10% | -100.00% | 91.98% | -4.01 | -3.55 | -5.79 | 62.9d | $-16,785.53 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,554 | +6.71% | +46.32% | +56.56% | 2.43% | +4.19 | +4.32 | +19.05 | 52.9d | $+210.43 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,499 | -4.77% | -29.09% | -25.77% | 55.42% | +0.38 | +0.39 | -0.52 | 59.9d | $-178.83 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,991 | -0.26% | -3.08% | -3.04% | 0.97% | -0.94 | -0.83 | -3.18 | 30.9d | $-9.74 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,911 | +42.41% | +198.82% | +424.59% | 10.23% | +3.23 | +4.87 | +19.44 | 77.9d | $+599.52 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,483 | -3.63% | -18.94% | -17.55% | 44.13% | +0.69 | +0.81 | -0.43 | 69.9d | $+274.04 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -79.75% | -57.11% | 22.12% | -1.37 | -1.70 | -3.61 | 51.9d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
