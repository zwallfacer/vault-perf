# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-17 08:02 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,584 | -14.39% | -82.85% | -59.12% | 50.72% | +0.18 | +0.16 | -1.63 | 63.4d | $-2,406.57 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,780 | -81.98% | -521.71% | -100.00% | 83.26% | -3.34 | -3.04 | -6.27 | 57.4d | $-12,660.01 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,907 | -0.62% | -3.63% | -3.58% | 7.55% | -0.11 | -0.11 | -0.48 | 62.4d | $+131.21 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,758 | -1.70% | -9.95% | -9.55% | 10.75% | -0.39 | -0.31 | -0.93 | 62.4d | $-269.20 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -89.25% | -61.22% | 22.12% | -1.44 | -1.80 | -4.03 | 46.3d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,580 | +7.46% | +57.45% | +74.04% | 2.43% | +5.37 | +6.01 | +23.64 | 47.4d | $+235.27 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,873 | -23.52% | -157.88% | -83.47% | 52.13% | -1.15 | -0.97 | -3.03 | 54.4d | $-868.41 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,711 | +5.96% | +33.80% | +38.86% | 43.59% | +1.00 | +1.27 | +0.78 | 64.4d | $+521.17 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,316 | +36.32% | +183.26% | +377.47% | 10.23% | +3.01 | +4.50 | +17.92 | 72.3d | $+504.75 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,972 | +34.61% | +216.54% | +542.05% | 14.86% | +3.74 | +3.91 | +14.57 | 58.3d | $+506.79 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
