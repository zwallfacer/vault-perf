# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-26 08:49 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,891 | +60.01% | +516.47% | +5614.51% | 24.43% | +3.92 | +3.97 | +21.14 | 42.4d | $+6,841.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,522 | -50.16% | -503.17% | -99.91% | 69.24% | -2.02 | -1.91 | -7.27 | 36.4d | $-4,375.73 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,220 | +49.68% | +417.48% | +2864.49% | 43.59% | +2.79 | +3.67 | +9.58 | 43.4d | $+1,849.88 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,817 | +35.58% | +388.67% | +2680.25% | 10.24% | +6.25 | +6.54 | +37.96 | 33.4d | $+1,254.52 |
| 5 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,635 | -6.16% | -54.33% | -42.92% | 7.19% | -2.17 | -1.93 | -7.55 | 41.4d | $-142.98 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,601 | -11.56% | -166.29% | -82.92% | 13.68% | -1.07 | -1.52 | -12.16 | 25.4d | $-606.92 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,226 | +1.39% | +14.31% | +15.27% | 16.00% | +0.56 | +0.52 | +0.89 | 35.4d | $-154.94 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,031 | +8.55% | +75.42% | +106.21% | 2.90% | +4.28 | +4.71 | +25.99 | 41.4d | $+217.45 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,491 | +3.70% | +51.12% | +65.20% | 2.12% | +4.62 | +6.09 | +24.11 | 26.4d | $+115.75 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,268 | +29.02% | +206.16% | +511.15% | 10.23% | +3.06 | +5.05 | +20.16 | 51.4d | $+380.64 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
