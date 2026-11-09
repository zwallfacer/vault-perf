# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-09 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $6,205 | -48.47% | -203.51% | -93.82% | 82.47% | +0.22 | +0.19 | -2.47 | 86.9d | $-6,606.51 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,268 | +6.44% | +27.33% | +30.33% | 7.55% | +1.09 | +1.06 | +3.62 | 85.9d | $+480.20 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $3,990 | -90.61% | — | — | — | — | — | — | 80.9d | $-16,337.66 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,464 | +4.11% | +21.13% | +23.01% | 5.24% | +1.39 | +1.21 | +4.03 | 71.0d | $+123.62 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,153 | -16.74% | -71.10% | -54.07% | 24.75% | -2.31 | -1.80 | -2.87 | 85.9d | $-864.83 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,993 | +30.72% | +116.93% | +177.23% | 12.06% | +2.05 | +2.87 | +9.70 | 95.9d | $+369.47 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,949 | -1.64% | -12.27% | -11.64% | 2.13% | -2.29 | -1.91 | -5.76 | 48.9d | $-51.27 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,847 | -20.50% | -96.01% | -65.85% | 60.35% | +0.03 | +0.03 | -1.59 | 77.9d | $-751.71 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -59.17% | -46.63% | 22.12% | -1.18 | -1.48 | -2.67 | 69.9d | $-464.91 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,071 | -15.85% | -65.77% | -51.14% | 54.57% | +0.43 | +0.49 | -1.21 | 88.0d | $-41.82 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
