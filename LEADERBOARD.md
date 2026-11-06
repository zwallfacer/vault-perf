# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-06 11:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $6,486 | -46.87% | -204.83% | -93.70% | 76.39% | -0.04 | -0.03 | -2.68 | 83.5d | $-6,409.92 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,333 | +7.83% | +34.63% | +39.57% | 7.55% | +1.34 | +1.34 | +4.59 | 82.5d | $+549.09 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,512 | +5.47% | +29.59% | +33.38% | 4.68% | +1.92 | +1.68 | +6.32 | 67.5d | $+169.15 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,339 | -11.91% | -52.70% | -42.95% | 20.19% | -1.60 | -1.21 | -2.61 | 82.5d | $-682.00 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,165 | -11.55% | -56.56% | -45.18% | 60.35% | +0.29 | +0.32 | -0.94 | 74.5d | $-430.97 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,110 | +35.79% | +141.25% | +234.50% | 10.23% | +2.42 | +3.48 | +13.81 | 92.5d | $+485.58 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,958 | -1.33% | -10.71% | -10.22% | 1.67% | -1.94 | -1.61 | -6.40 | 45.5d | $-41.99 |
| 8 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $2,748 | -93.49% | — | — | — | — | — | — | 77.5d | $-17,566.57 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,503 | -2.79% | -12.03% | -11.49% | 47.44% | +0.78 | +0.91 | -0.25 | 84.5d | $+295.74 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -62.21% | -48.33% | 22.12% | -1.20 | -1.49 | -2.81 | 66.5d | $-464.90 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
