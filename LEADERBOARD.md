# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-08 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,375 | +39.47% | +262.42% | +813.29% | 24.43% | +2.56 | +2.59 | +10.74 | 54.9d | $+4,288.08 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $12,347 | -71.42% | -533.35% | -99.99% | 73.12% | -2.60 | -2.49 | -7.29 | 48.9d | $-8,094.47 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,024 | +3.80% | +25.75% | +28.76% | 5.74% | +1.49 | +1.37 | +4.49 | 53.9d | $-3.01 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,911 | -0.74% | -5.04% | -4.93% | 7.55% | -0.19 | -0.18 | -0.67 | 53.9d | $+125.08 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -83.23% | -58.12% | 19.75% | -1.14 | -1.46 | -4.21 | 37.9d | $-347.93 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,555 | -4.87% | -38.74% | -32.78% | 36.90% | -0.01 | -0.00 | -1.05 | 45.9d | $-182.45 |
| 7 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,545 | +6.44% | +60.41% | +79.58% | 2.12% | +6.03 | +7.53 | +28.49 | 38.9d | $+201.31 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,206 | +23.99% | +156.61% | +307.02% | 43.59% | +1.65 | +2.11 | +3.59 | 55.9d | $+984.00 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,298 | +35.04% | +200.28% | +456.81% | 10.23% | +3.14 | +4.79 | +19.58 | 63.9d | $+483.03 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,972 | +34.68% | +253.82% | +783.81% | 14.86% | +4.14 | +4.35 | +17.08 | 49.9d | $+507.68 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
