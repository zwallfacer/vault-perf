# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-25 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,233 | -18.28% | -92.76% | -64.10% | 57.56% | +0.21 | +0.18 | -1.61 | 71.9d | $-2,900.96 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $8,164 | -80.92% | -448.09% | -99.99% | 92.09% | -1.00 | -1.24 | -4.87 | 65.9d | $-12,206.72 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,063 | +2.14% | +11.01% | +11.50% | 7.55% | +0.45 | +0.45 | +1.46 | 70.9d | $+267.69 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,779 | -2.73% | -14.04% | -13.27% | 13.59% | -0.48 | -0.39 | -1.03 | 70.9d | $-332.26 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,547 | +6.41% | +41.81% | +49.97% | 2.72% | +3.85 | +4.02 | +15.36 | 56.0d | $+200.29 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,987 | -0.38% | -4.13% | -4.05% | 0.97% | -1.28 | -1.18 | -4.26 | 33.9d | $-13.47 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,838 | -23.07% | -133.79% | -78.15% | 55.42% | -0.46 | -0.46 | -2.41 | 62.9d | $-851.80 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,821 | +37.72% | +170.19% | +323.78% | 10.23% | +2.83 | +4.29 | +16.64 | 80.9d | $+503.71 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,436 | -6.79% | -33.99% | -29.67% | 47.44% | +0.57 | +0.67 | -0.72 | 73.0d | $+192.49 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -75.33% | -55.05% | 22.12% | -1.33 | -1.65 | -3.41 | 54.9d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
