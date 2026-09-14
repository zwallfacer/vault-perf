# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-14 09:13 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,399 | +7.34% | +88.04% | +133.87% | 21.31% | +1.18 | +1.05 | +4.13 | 30.4d | $+746.03 |
| 2 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $5,018 | -13.49% | -367.67% | -98.07% | 9.05% | -4.43 | -4.36 | -40.62 | 13.4d | $-673.55 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $4,991 | -35.19% | -526.40% | -99.85% | 52.89% | -4.59 | -3.37 | -9.95 | 24.4d | $-3,275.54 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` † | $4,951 | +12.94% | +160.45% | +352.16% | 4.89% | +3.71 | +7.04 | +32.78 | 29.4d | $+187.03 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,688 | +12.30% | +191.71% | +509.90% | 10.73% | +2.59 | +2.43 | +17.87 | 23.4d | $+299.76 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $4,313 | -2.49% | -35.79% | -30.40% | 36.39% | -1.24 | -0.99 | -0.98 | 25.4d | $-468.53 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,141 | +17.97% | +306.11% | +1569.48% | 10.24% | +6.40 | +7.77 | +29.90 | 21.4d | $+617.24 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,411 | +1.41% | +35.56% | +42.34% | 0.92% | +4.29 | +7.71 | +38.56 | 14.4d | $+38.60 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` † | $2,852 | +4.66% | +57.83% | +75.99% | 1.80% | +3.79 | +3.61 | +32.16 | 29.4d | $+51.66 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,314 | +20.18% | +187.04% | +449.46% | 10.23% | +2.61 | +4.77 | +18.29 | 39.4d | $+234.58 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
