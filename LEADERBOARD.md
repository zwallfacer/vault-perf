# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-20 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $16,314 | +39.99% | +395.61% | +2688.06% | 24.43% | +3.36 | +3.34 | +16.19 | 36.9d | $+4,545.31 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $9,696 | -20.96% | -247.76% | -93.80% | 69.24% | -0.26 | -0.24 | -3.58 | 30.9d | $-1,541.13 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $6,476 | +49.68% | +478.18% | +4752.50% | 43.59% | +3.01 | +3.73 | +10.97 | 37.9d | $+1,849.89 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,866 | -2.32% | -23.62% | -21.26% | 6.01% | -1.25 | -1.18 | -3.93 | 35.9d | $+46.98 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,661 | +11.75% | +143.53% | +288.47% | 10.73% | +2.19 | +2.06 | +13.38 | 29.9d | $+276.90 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,629 | -10.33% | -189.79% | -86.51% | 13.68% | -1.05 | -1.43 | -13.88 | 19.9d | $-543.01 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,548 | +30.38% | +397.52% | +3117.47% | 10.24% | +6.22 | +6.81 | +38.82 | 27.9d | $+1,050.68 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,937 | +5.97% | +60.68% | +80.29% | 2.90% | +3.48 | +3.55 | +20.91 | 35.9d | $+121.32 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,509 | +4.44% | +77.55% | +113.56% | 1.18% | +7.27 | +12.35 | +65.77 | 20.9d | $+140.69 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,135 | +24.36% | +193.93% | +467.21% | 10.23% | +2.88 | +5.15 | +18.96 | 45.9d | $+300.80 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
