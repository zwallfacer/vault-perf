# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-27 09:31 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,891 | +60.01% | +504.23% | +5092.20% | 24.43% | +3.88 | +3.88 | +20.64 | 43.4d | $+6,841.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,411 | -58.33% | -568.99% | -99.98% | 73.12% | -2.77 | -2.68 | -7.78 | 37.4d | $-5,008.11 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,232 | +50.54% | +414.85% | +2772.35% | 43.59% | +2.78 | +3.62 | +9.52 | 44.5d | $+1,879.77 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,763 | +9.00% | +77.44% | +109.90% | 2.90% | +4.43 | +4.83 | +26.68 | 42.4d | $+238.09 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,704 | +29.25% | +309.96% | +1416.54% | 10.24% | +5.10 | +6.02 | +30.27 | 34.4d | $+1,072.48 |
| 6 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,684 | -5.81% | -49.98% | -40.24% | 7.55% | -2.01 | -1.78 | -6.62 | 42.4d | $-125.52 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,648 | -10.04% | -138.87% | -76.86% | 13.68% | -0.66 | -0.90 | -10.15 | 26.4d | $-528.42 |
| 8 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,131 | -1.50% | -15.03% | -14.05% | 16.00% | +0.17 | +0.17 | -0.94 | 36.4d | $-275.28 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,512 | +4.37% | +58.13% | +76.64% | 2.12% | +5.43 | +7.21 | +27.41 | 27.5d | $+138.31 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,201 | +28.33% | +197.34% | +468.29% | 10.23% | +2.95 | +4.91 | +19.29 | 52.4d | $+369.02 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
