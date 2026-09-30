# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-30 10:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,738 | +50.64% | +397.87% | +2400.68% | 24.43% | +3.32 | +3.45 | +16.29 | 46.5d | $+5,677.18 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,025 | -60.63% | -547.25% | -99.98% | 73.12% | -2.65 | -2.61 | -7.48 | 40.4d | $-5,418.50 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,710 | +7.79% | +62.56% | +82.66% | 2.90% | +3.59 | +3.57 | +21.56 | 45.4d | $+184.80 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,694 | -5.02% | -40.33% | -33.89% | 7.55% | -1.63 | -1.52 | -5.35 | 45.5d | $-86.55 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,289 | -17.23% | -213.78% | -90.43% | 14.71% | -2.29 | -2.94 | -14.53 | 29.4d | $-900.87 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,819 | +3.43% | +33.40% | +38.88% | 26.53% | +0.59 | +0.50 | +1.26 | 37.5d | $+122.82 |
| 7 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,548 | +5.50% | +65.82% | +89.78% | 2.12% | +6.24 | +8.48 | +31.04 | 30.5d | $+176.07 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,211 | +32.07% | +246.49% | +748.25% | 43.59% | +2.08 | +2.75 | +5.66 | 47.5d | $+1,209.73 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,232 | +30.24% | +199.14% | +469.69% | 10.23% | +3.01 | +4.90 | +19.47 | 55.4d | $+401.71 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,851 | +26.19% | +230.76% | +676.47% | 6.34% | +5.04 | +5.20 | +36.41 | 41.4d | $+383.47 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
