# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-23 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,885 | +62.31% | +570.04% | +8301.67% | 24.43% | +4.18 | +4.25 | +23.33 | 39.9d | $+7,123.55 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,580 | -44.82% | -482.97% | -99.84% | 69.24% | -1.61 | -1.52 | -6.98 | 33.9d | $-4,025.44 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +443.12% | +3550.60% | 43.59% | +2.89 | +3.58 | +10.17 | 40.9d | $+1,849.89 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,832 | +38.38% | +453.44% | +4541.74% | 10.24% | +7.18 | +7.55 | +44.28 | 30.9d | $+1,330.05 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,819 | -7.01% | -111.94% | -68.67% | 13.68% | +0.08 | +0.13 | -8.18 | 22.9d | $-371.17 |
| 6 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,802 | -2.96% | -27.78% | -24.57% | 6.64% | -1.20 | -1.11 | -4.19 | 38.9d | $+15.47 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,343 | +4.25% | +47.17% | +58.72% | 14.68% | +0.97 | +0.88 | +3.21 | 32.9d | $-35.68 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,973 | +7.04% | +66.04% | +89.31% | 2.90% | +3.71 | +4.05 | +22.76 | 38.9d | $+161.06 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,519 | +4.66% | +71.20% | +100.54% | 1.18% | +6.76 | +10.42 | +60.38 | 23.9d | $+148.13 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,251 | +28.07% | +209.74% | +535.08% | 10.23% | +3.10 | +5.30 | +20.50 | 48.9d | $+364.08 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
