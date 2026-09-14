# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-14 12:59 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,174 | +6.23% | +74.41% | +105.82% | 21.31% | +1.09 | +1.01 | +3.49 | 30.6d | $+608.65 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` † | $4,970 | +13.53% | +166.95% | +378.65% | 4.89% | +3.87 | +7.34 | +34.11 | 29.6d | $+213.17 |
| 3 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,961 | -14.25% | -384.01% | -98.41% | 9.05% | -4.98 | -5.12 | -42.43 | 13.5d | $-717.89 |
| 4 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $4,839 | -37.11% | -551.49% | -99.90% | 52.89% | -4.86 | -3.56 | -10.43 | 24.6d | $-3,422.89 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,642 | +11.48% | +177.79% | +438.18% | 10.73% | +2.45 | +2.29 | +16.57 | 23.6d | $+265.72 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $4,331 | -1.77% | -25.31% | -22.53% | 36.39% | -1.12 | -0.90 | -0.70 | 25.6d | $-436.98 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,061 | +15.91% | +269.11% | +1114.93% | 10.24% | +6.45 | +6.82 | +26.28 | 21.6d | $+545.45 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,409 | +1.39% | +34.75% | +41.21% | 0.92% | +4.24 | +7.62 | +37.68 | 14.6d | $+38.03 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` † | $2,843 | +4.36% | +53.79% | +69.31% | 1.80% | +3.53 | +3.33 | +29.91 | 29.6d | $+43.42 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,316 | +20.16% | +186.13% | +444.96% | 10.23% | +2.61 | +4.77 | +18.20 | 39.5d | $+234.21 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
