# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-26 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,703 | -13.26% | -66.36% | -50.93% | 57.56% | +0.42 | +0.35 | -1.15 | 72.9d | $-2,284.45 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,417 | -82.57% | -450.41% | -99.99% | 92.09% | -1.13 | -1.40 | -4.89 | 66.9d | $-12,911.95 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,069 | +2.50% | +12.67% | +13.33% | 7.55% | +0.52 | +0.51 | +1.68 | 71.9d | $+285.39 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,760 | -3.28% | -16.65% | -15.57% | 13.59% | -0.59 | -0.49 | -1.23 | 71.9d | $-353.73 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,540 | +6.26% | +40.10% | +47.54% | 2.72% | +3.72 | +3.94 | +14.73 | 57.0d | $+195.20 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,983 | -0.46% | -4.85% | -4.75% | 0.97% | -1.53 | -1.38 | -5.01 | 34.9d | $-15.89 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,784 | +36.05% | +160.65% | +294.28% | 10.23% | +2.70 | +4.11 | +15.71 | 81.9d | $+469.50 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,555 | -32.22% | -183.92% | -89.14% | 55.42% | -0.92 | -0.92 | -3.32 | 63.9d | $-1,188.26 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,498 | -4.44% | -21.92% | -20.09% | 47.44% | +0.65 | +0.75 | -0.46 | 74.0d | $+253.10 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -73.99% | -54.40% | 22.12% | -1.32 | -1.64 | -3.34 | 55.9d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
