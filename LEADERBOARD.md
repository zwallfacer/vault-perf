# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-12 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $6,148 | -46.89% | -190.30% | -92.33% | 82.47% | +0.37 | +0.33 | -2.31 | 89.9d | $-6,412.31 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,174 | +4.60% | +18.89% | +20.28% | 7.55% | +0.77 | +0.76 | +2.50 | 88.9d | $+389.51 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ✂ | $4,492 | +20.76% | +874.51% | +282356.50% | 58.90% | +1.75 | +1.81 | +14.85 | 8.7d | $+776.14 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,374 | +1.53% | +7.53% | +7.76% | 7.67% | +0.49 | +0.43 | +0.98 | 74.0d | $+37.60 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,007 | -20.66% | -84.80% | -61.32% | 27.99% | -2.84 | -2.22 | -3.03 | 88.9d | $-1,013.45 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,917 | -2.69% | -18.90% | -17.43% | 2.99% | -3.45 | -2.86 | -6.33 | 51.9d | $-82.55 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,896 | +26.72% | +98.61% | +139.63% | 16.61% | +1.76 | +2.40 | +5.94 | 98.9d | $+277.70 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,723 | -23.47% | -105.83% | -70.06% | 60.35% | -0.04 | -0.05 | -1.75 | 80.9d | $-857.95 |
| 9 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,597 | +0.00% | +0.00% | +0.00% | 0.00% | — | — | — | 0.5d | $+0.00 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -56.74% | -45.24% | 22.12% | -1.15 | -1.45 | -2.56 | 72.9d | $-464.92 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
