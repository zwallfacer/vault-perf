# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-12 11:51 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,761 | -53.22% | -216.96% | -95.48% | 82.47% | +0.16 | +0.14 | -2.63 | 89.5d | $-7,189.45 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,191 | +4.93% | +20.32% | +21.94% | 7.55% | +0.83 | +0.81 | +2.69 | 88.5d | $+405.67 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ✂ | $4,563 | +22.43% | +990.66% | +761572.68% | 58.90% | +1.82 | +1.90 | +16.82 | 8.3d | $+838.42 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,374 | +1.28% | +6.35% | +6.51% | 6.74% | +0.41 | +0.36 | +0.94 | 73.6d | $+29.40 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,001 | -20.83% | -85.88% | -61.83% | 27.61% | -2.86 | -2.24 | -3.11 | 88.5d | $-1,019.88 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,930 | -2.28% | -16.18% | -15.10% | 2.52% | -3.05 | -2.57 | -6.41 | 51.5d | $-70.43 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,908 | +26.71% | +98.96% | +140.40% | 16.61% | +1.76 | +2.40 | +5.96 | 98.5d | $+277.41 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,618 | -27.24% | -123.44% | -76.33% | 60.35% | -0.18 | -0.20 | -2.05 | 80.5d | $-993.01 |
| 9 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,597 | +0.00% | +0.00% | +0.00% | 0.00% | — | — | — | 0.1d | $+0.00 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -57.05% | -45.42% | 22.12% | -1.15 | -1.45 | -2.58 | 72.5d | $-464.92 |
| 44 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
