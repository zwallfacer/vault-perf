# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-21 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,227 | -1.93% | -10.36% | -9.94% | 57.56% | +0.76 | +0.69 | -0.18 | 67.9d | $-893.36 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,589 | -84.52% | -498.60% | -100.00% | 87.42% | -3.26 | -3.03 | -5.70 | 61.9d | $-13,742.46 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,978 | +0.51% | +2.80% | +2.83% | 7.55% | +0.14 | +0.13 | +0.37 | 66.9d | $+187.29 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,028 | +7.22% | +44.75% | +54.04% | 55.42% | +0.90 | +0.94 | +0.81 | 58.9d | $+262.32 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,019 | +3.36% | +18.31% | +19.74% | 13.59% | +0.91 | +0.82 | +1.35 | 66.9d | $-95.75 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,607 | +8.28% | +58.22% | +74.96% | 2.43% | +5.55 | +6.23 | +23.95 | 51.9d | $+262.61 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` † | $3,003 | +0.15% | +1.87% | +1.89% | 0.97% | +0.65 | +0.61 | +1.93 | 29.9d | $+2.65 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,970 | +44.92% | +213.31% | +482.33% | 10.23% | +3.43 | +5.19 | +20.85 | 76.9d | $+650.73 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,911 | +9.91% | +52.48% | +64.93% | 44.13% | +1.10 | +1.36 | +1.19 | 68.9d | $+622.81 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -81.32% | -57.81% | 22.12% | -1.38 | -1.71 | -3.68 | 50.9d | $-464.89 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
