# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-15 08:53 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,773 | +0.72% | +8.38% | +8.71% | 21.31% | +1.01 | +0.92 | +0.39 | 31.4d | $+22.68 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,954 | +12.90% | +154.76% | +328.74% | 4.89% | +3.63 | +7.07 | +31.62 | 30.4d | $+185.27 |
| 3 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,862 | -16.13% | -409.59% | -98.85% | 10.56% | -5.97 | -6.04 | -38.80 | 14.4d | $-826.89 |
| 4 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,719 | +13.26% | +198.37% | +544.17% | 10.73% | +2.70 | +2.29 | +18.49 | 24.4d | $+339.80 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,061 | +16.40% | +267.13% | +1086.48% | 10.24% | +6.08 | +7.18 | +26.09 | 22.4d | $+562.55 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,940 | -6.48% | -89.56% | -60.38% | 36.39% | -1.45 | -1.25 | -2.46 | 26.4d | $-635.45 |
| 7 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $3,709 | -51.57% | -741.32% | -100.00% | 65.99% | -5.70 | -4.06 | -11.23 | 25.4d | $-4,535.39 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,413 | +1.49% | +35.31% | +41.98% | 0.92% | +4.20 | +7.83 | +38.29 | 15.4d | $+41.48 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,850 | +4.60% | +55.25% | +71.62% | 1.80% | +3.69 | +3.63 | +30.72 | 30.4d | $+50.05 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,238 | +18.19% | +164.44% | +353.06% | 10.23% | +2.31 | +4.21 | +16.08 | 40.4d | $+196.15 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
