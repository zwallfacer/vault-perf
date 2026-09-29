# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-29 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,061 | +53.35% | +424.27% | +2896.94% | 24.43% | +3.47 | +3.55 | +17.37 | 45.9d | $+6,013.56 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,995 | -66.36% | -607.46% | -100.00% | 73.12% | -3.48 | -3.36 | -8.31 | 39.9d | $-6,442.35 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,704 | +7.64% | +62.16% | +82.03% | 2.90% | +3.56 | +3.58 | +21.42 | 44.9d | $+178.42 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,677 | -5.40% | -43.92% | -36.33% | 7.55% | -1.77 | -1.62 | -5.82 | 44.9d | $-105.32 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,625 | +25.30% | +250.27% | +830.98% | 11.46% | +4.19 | +4.73 | +21.83 | 36.9d | $+927.27 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $4,586 | +29.39% | +228.60% | +642.00% | 43.59% | +2.01 | +2.68 | +5.24 | 46.9d | $+1,142.21 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,270 | -17.82% | -225.44% | -91.65% | 14.00% | -2.49 | -3.24 | -16.10 | 28.9d | $-931.57 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,543 | +5.38% | +65.64% | +89.52% | 2.12% | +6.28 | +8.22 | +30.95 | 29.9d | $+172.16 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,251 | +31.37% | +208.74% | +514.46% | 10.23% | +3.16 | +5.28 | +20.41 | 54.9d | $+421.20 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,836 | +25.84% | +230.79% | +679.00% | 6.34% | +5.03 | +5.26 | +36.41 | 40.9d | $+378.31 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
