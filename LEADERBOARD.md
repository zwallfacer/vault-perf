# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-13 11:06 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,954 | +12.34% | +75.68% | +104.14% | 33.34% | +1.35 | +1.30 | +2.27 | 59.5d | $+915.49 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $12,632 | -70.81% | -483.27% | -99.98% | 73.12% | -2.35 | -2.23 | -6.61 | 53.5d | $-7,833.34 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,963 | +0.37% | +2.29% | +2.31% | 7.55% | +0.11 | +0.11 | +0.30 | 58.5d | $+180.05 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,953 | +2.46% | +15.35% | +16.38% | 7.24% | +0.92 | +0.84 | +2.12 | 58.5d | $-67.92 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -74.20% | -53.97% | 19.75% | -1.07 | -1.36 | -3.76 | 42.5d | $-347.93 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,571 | +7.19% | +60.32% | +79.04% | 2.12% | +5.83 | +6.50 | +28.45 | 43.5d | $+226.34 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,982 | -18.87% | -136.39% | -77.94% | 40.43% | -0.95 | -0.81 | -3.37 | 50.5d | $-697.45 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,937 | +13.84% | +83.43% | +118.45% | 43.59% | +1.28 | +1.61 | +1.91 | 60.5d | $+723.97 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,305 | +35.80% | +190.87% | +411.17% | 10.23% | +3.07 | +4.67 | +18.66 | 68.5d | $+495.98 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,972 | +34.84% | +233.44% | +641.04% | 14.86% | +3.93 | +4.16 | +15.71 | 54.5d | $+510.09 |
| 39 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
