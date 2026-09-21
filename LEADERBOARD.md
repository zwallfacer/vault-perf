# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-21 09:18 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $16,628 | +47.16% | +459.93% | +4228.70% | 24.43% | +3.66 | +3.60 | +18.83 | 37.4d | $+5,382.34 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,689 | -13.49% | -156.81% | -81.45% | 69.24% | +0.23 | +0.21 | -2.26 | 31.4d | $-623.25 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +471.55% | +4498.25% | 43.59% | +2.97 | +3.63 | +10.82 | 38.5d | $+1,849.89 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,823 | -3.34% | -33.49% | -28.87% | 6.01% | -1.71 | -1.62 | -5.57 | 36.4d | $-3.46 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,631 | +33.38% | +428.59% | +3937.41% | 10.24% | +6.64 | +7.15 | +41.86 | 28.4d | $+1,155.45 |
| 6 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,589 | +8.80% | +105.64% | +175.25% | 10.73% | +1.71 | +1.65 | +9.85 | 30.4d | $+154.08 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,565 | -6.05% | -108.35% | -67.30% | 13.68% | +0.36 | +0.54 | -7.92 | 20.4d | $-321.59 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,975 | +7.08% | +70.99% | +98.55% | 2.90% | +3.98 | +4.07 | +24.46 | 36.4d | $+162.80 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,516 | +4.89% | +83.29% | +125.50% | 1.18% | +7.79 | +12.93 | +70.63 | 21.4d | $+155.84 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,150 | +25.00% | +196.70% | +478.76% | 10.23% | +2.91 | +5.15 | +19.23 | 46.4d | $+311.69 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
