# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-02 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $11,376 | -7.30% | -33.35% | -29.27% | 57.56% | +0.70 | +0.61 | -0.58 | 79.9d | $-1,553.32 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,334 | +7.85% | +36.30% | +41.83% | 7.55% | +1.38 | +1.38 | +4.81 | 78.9d | $+550.17 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,145 | -87.97% | -434.38% | -100.00% | 92.09% | -1.36 | -1.62 | -4.72 | 73.9d | $-15,211.29 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,545 | -8.56% | -39.57% | -33.88% | 16.39% | -1.44 | -1.15 | -2.41 | 78.9d | $-558.78 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,494 | +4.91% | +28.01% | +31.45% | 4.68% | +2.03 | +1.82 | +5.98 | 64.0d | $+150.26 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,051 | +18.51% | +83.45% | +115.03% | 47.44% | +1.27 | +1.59 | +1.76 | 81.0d | $+844.40 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,965 | -1.13% | -9.82% | -9.40% | 1.39% | -2.74 | -2.31 | -7.05 | 41.9d | $-35.77 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,794 | +36.30% | +149.03% | +256.61% | 10.23% | +2.57 | +3.99 | +14.57 | 88.9d | $+474.66 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,594 | -30.33% | -156.08% | -84.43% | 60.35% | -0.53 | -0.58 | -2.59 | 70.9d | $-1,119.01 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -65.75% | -50.23% | 22.12% | -1.24 | -1.55 | -2.97 | 62.9d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
