# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-07 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,604 | -54.90% | -235.93% | -96.74% | 79.28% | -0.16 | -0.13 | -2.98 | 84.9d | $-7,395.76 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,366 | +8.51% | +37.01% | +42.65% | 7.55% | +1.44 | +1.44 | +4.91 | 83.9d | $+582.89 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,485 | +4.52% | +23.91% | +26.35% | 4.68% | +1.57 | +1.38 | +5.11 | 69.0d | $+137.25 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,229 | -14.87% | -64.67% | -50.35% | 22.16% | -2.04 | -1.57 | -2.92 | 83.9d | $-794.07 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,070 | +33.87% | +131.67% | +210.79% | 10.23% | +2.28 | +3.26 | +12.87 | 93.9d | $+441.64 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,954 | -1.47% | -11.46% | -10.90% | 1.71% | -2.12 | -1.78 | -6.68 | 46.9d | $-46.12 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,816 | -21.49% | -103.30% | -68.75% | 60.35% | -0.08 | -0.09 | -1.71 | 75.9d | $-787.21 |
| 8 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $2,595 | -93.97% | — | — | — | — | — | — | 78.9d | $-17,769.63 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,365 | -8.84% | -37.53% | -32.49% | 47.44% | +0.62 | +0.72 | -0.79 | 86.0d | $+139.80 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -60.91% | -47.61% | 22.12% | -1.19 | -1.49 | -2.75 | 67.9d | $-464.90 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
