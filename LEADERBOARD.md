# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-07 10:41 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $6,040 | -50.93% | -220.05% | -95.39% | 79.28% | -0.00 | -0.00 | -2.78 | 84.5d | $-6,908.78 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,355 | +8.36% | +36.55% | +42.05% | 7.55% | +1.42 | +1.41 | +4.84 | 83.5d | $+575.37 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,502 | +5.00% | +26.66% | +29.71% | 4.68% | +1.74 | +1.54 | +5.69 | 68.5d | $+153.46 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,272 | -13.65% | -59.67% | -47.35% | 21.11% | -1.86 | -1.44 | -2.83 | 83.5d | $-747.68 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,115 | +35.84% | +139.98% | +230.80% | 10.23% | +2.40 | +3.48 | +13.69 | 93.4d | $+486.68 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,958 | -1.37% | -10.79% | -10.29% | 1.71% | -1.98 | -1.66 | -6.30 | 46.5d | $-43.14 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,829 | -22.18% | -107.24% | -70.26% | 60.35% | -0.11 | -0.12 | -1.78 | 75.5d | $-811.83 |
| 8 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $2,608 | -93.86% | — | — | — | — | — | — | 78.5d | $-17,722.34 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,511 | -3.21% | -13.71% | -13.01% | 47.44% | +0.76 | +0.90 | -0.29 | 85.5d | $+284.78 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -61.32% | -47.84% | 22.12% | -1.19 | -1.49 | -2.77 | 67.5d | $-464.90 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
