# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-29 11:17 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,844 | +51.55% | +413.47% | +2706.49% | 24.43% | +3.40 | +3.47 | +16.92 | 45.5d | $+5,790.64 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,975 | -66.58% | -615.34% | -100.00% | 73.12% | -3.51 | -3.38 | -8.42 | 39.5d | $-6,480.59 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $4,758 | +36.39% | +285.42% | +1040.63% | 43.59% | +2.25 | +2.94 | +6.55 | 46.5d | $+1,386.46 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,735 | -4.32% | -35.42% | -30.38% | 7.55% | -1.42 | -1.28 | -4.69 | 44.5d | $-51.78 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,699 | +7.54% | +61.86% | +81.55% | 2.90% | +3.52 | +3.54 | +21.31 | 44.5d | $+173.95 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,494 | +22.35% | +223.42% | +651.14% | 11.46% | +3.74 | +4.38 | +19.49 | 36.5d | $+818.79 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,274 | -17.55% | -224.91% | -91.57% | 13.68% | -2.42 | -3.15 | -16.44 | 28.5d | $-917.16 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,536 | +5.16% | +63.84% | +86.35% | 2.12% | +6.11 | +7.90 | +30.11 | 29.5d | $+164.96 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,282 | +33.11% | +221.84% | +579.56% | 10.23% | +3.33 | +5.61 | +21.69 | 54.5d | $+450.94 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,836 | +25.28% | +227.97% | +663.26% | 6.34% | +4.88 | +5.11 | +35.97 | 40.5d | $+370.18 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
