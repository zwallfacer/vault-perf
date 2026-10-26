# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-26 09:22 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,921 | -18.42% | -92.83% | -64.16% | 57.56% | +0.21 | +0.18 | -1.61 | 72.4d | $-2,918.05 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,072 | -83.38% | -458.25% | -99.99% | 92.09% | -1.19 | -1.48 | -4.98 | 66.4d | $-13,253.63 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,041 | +1.92% | +9.84% | +10.23% | 7.55% | +0.41 | +0.41 | +1.30 | 71.4d | $+257.10 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,775 | -2.86% | -14.59% | -13.76% | 13.59% | -0.50 | -0.42 | -1.07 | 71.4d | $-337.20 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,539 | +6.36% | +41.13% | +48.99% | 2.72% | +3.79 | +3.92 | +15.11 | 56.4d | $+198.66 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,985 | -0.39% | -4.09% | -4.02% | 0.97% | -1.25 | -1.13 | -4.23 | 34.4d | $-13.54 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,781 | +36.45% | +163.47% | +303.03% | 10.23% | +2.73 | +4.16 | +15.98 | 81.4d | $+477.82 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,660 | -27.23% | -156.69% | -83.94% | 55.42% | -0.67 | -0.68 | -2.83 | 63.4d | $-1,004.86 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,411 | -5.81% | -28.88% | -25.73% | 47.44% | +0.60 | +0.70 | -0.61 | 73.5d | $+217.81 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -74.66% | -54.72% | 22.12% | -1.32 | -1.64 | -3.38 | 55.4d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
