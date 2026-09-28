# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-28 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,221 | +46.54% | +378.38% | +2134.84% | 24.43% | +3.23 | +3.32 | +15.49 | 44.9d | $+5,167.33 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,310 | -64.64% | -606.90% | -99.99% | 73.12% | -3.32 | -3.18 | -8.30 | 38.9d | $-6,134.52 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,726 | -4.57% | -38.00% | -32.22% | 7.55% | -1.53 | -1.39 | -5.04 | 43.9d | $-64.13 |
| 4 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $4,726 | +35.84% | +284.88% | +1041.28% | 43.59% | +2.26 | +3.01 | +6.54 | 45.9d | $+1,367.29 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,706 | +7.69% | +63.99% | +85.24% | 2.90% | +3.67 | +3.80 | +22.05 | 43.9d | $+180.59 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,533 | +23.01% | +234.01% | +721.60% | 10.63% | +3.91 | +4.49 | +22.02 | 35.9d | $+843.23 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,294 | -17.14% | -224.52% | -91.48% | 13.68% | -2.35 | -3.05 | -16.41 | 27.9d | $-895.93 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,518 | +4.54% | +57.31% | +75.15% | 2.12% | +5.52 | +7.21 | +27.03 | 28.9d | $+143.93 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,293 | +33.62% | +227.83% | +612.85% | 10.23% | +3.40 | +5.68 | +22.27 | 53.9d | $+459.68 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,839 | +25.65% | +234.84% | +708.88% | 6.34% | +4.97 | +5.37 | +37.05 | 39.9d | $+375.53 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
