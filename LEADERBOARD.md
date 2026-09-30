# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-30 22:18 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,511 | +49.46% | +384.35% | +2171.07% | 24.43% | +3.27 | +3.39 | +15.73 | 47.0d | $+5,530.32 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,985 | -60.78% | -541.81% | -99.98% | 73.12% | -2.67 | -2.63 | -7.41 | 40.9d | $-5,446.71 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,726 | -4.58% | -36.37% | -31.09% | 7.55% | -1.49 | -1.36 | -4.82 | 46.0d | $-64.71 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,721 | +8.04% | +63.87% | +84.84% | 2.90% | +3.69 | +3.68 | +22.01 | 46.0d | $+195.84 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,343 | -16.10% | -196.31% | -88.24% | 14.71% | -1.99 | -2.57 | -13.34 | 29.9d | $-842.16 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,026 | +9.06% | +87.08% | +130.15% | 26.53% | +1.42 | +1.36 | +3.28 | 38.0d | $+329.93 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,775 | +52.73% | +401.01% | +2404.57% | 43.59% | +2.70 | +3.70 | +9.20 | 48.0d | $+1,714.26 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,547 | +5.43% | +63.92% | +86.34% | 2.12% | +6.15 | +8.36 | +30.14 | 31.0d | $+173.75 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,311 | +32.92% | +214.84% | +540.54% | 10.23% | +3.25 | +5.30 | +21.00 | 55.9d | $+447.74 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,791 | +22.79% | +198.31% | +496.87% | 6.34% | +4.05 | +4.21 | +31.29 | 41.9d | $+333.62 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
