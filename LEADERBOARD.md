# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-27 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $20,100 | +61.79% | +513.82% | +5364.49% | 24.43% | +3.95 | +3.95 | +21.03 | 43.9d | $+7,063.35 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,540 | -57.71% | -556.12% | -99.97% | 73.12% | -2.71 | -2.55 | -7.61 | 37.9d | $-4,896.93 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,118 | +46.51% | +377.87% | +2126.35% | 43.59% | +2.65 | +3.55 | +8.67 | 44.9d | $+1,739.16 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,778 | +9.33% | +79.44% | +113.72% | 2.90% | +4.59 | +4.84 | +27.37 | 42.9d | $+252.62 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,701 | +28.15% | +294.43% | +1238.61% | 10.24% | +4.91 | +5.77 | +28.75 | 34.9d | $+1,032.12 |
| 6 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,651 | -6.05% | -51.50% | -41.21% | 7.55% | -2.10 | -1.89 | -6.83 | 42.9d | $-137.47 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,587 | -12.01% | -163.24% | -82.43% | 13.68% | -1.16 | -1.62 | -11.93 | 26.9d | $-630.39 |
| 8 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,070 | -2.03% | -20.05% | -18.34% | 16.21% | +0.10 | +0.10 | -1.24 | 36.9d | $-297.20 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,516 | +4.54% | +59.42% | +78.80% | 2.12% | +5.62 | +7.49 | +28.02 | 27.9d | $+144.08 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,212 | +28.98% | +200.15% | +479.85% | 10.23% | +3.02 | +5.05 | +19.57 | 52.9d | $+380.25 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
