# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-29 10:25 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,916 | +5.53% | +26.74% | +29.73% | 57.56% | +1.06 | +0.93 | +0.46 | 75.5d | $+21.91 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,134 | -83.28% | -437.64% | -99.99% | 92.09% | -1.06 | -1.29 | -4.75 | 69.5d | $-13,211.19 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,176 | +4.61% | +22.57% | +24.69% | 7.55% | +0.89 | +0.88 | +2.99 | 74.5d | $+389.68 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,777 | -2.74% | -13.45% | -12.75% | 13.59% | -0.44 | -0.37 | -0.99 | 74.5d | $-332.87 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,529 | +6.01% | +36.90% | +43.09% | 2.72% | +3.31 | +3.23 | +13.56 | 59.5d | $+187.11 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,985 | -0.45% | -4.34% | -4.26% | 0.97% | -1.33 | -1.24 | -4.48 | 37.5d | $-15.33 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,744 | +34.52% | +149.22% | +260.35% | 10.23% | +2.52 | +3.80 | +14.59 | 84.4d | $+438.33 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,634 | +2.89% | +13.80% | +14.57% | 47.44% | +0.87 | +1.02 | +0.29 | 76.5d | $+442.02 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,342 | -35.89% | -197.08% | -91.30% | 56.06% | -1.10 | -1.10 | -3.52 | 66.5d | $-1,323.52 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -70.77% | -52.82% | 22.12% | -1.28 | -1.60 | -3.20 | 58.4d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
