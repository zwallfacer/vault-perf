# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-19 08:18 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $15,935 | +32.42% | +334.35% | +1710.33% | 24.43% | +3.00 | +3.01 | +13.69 | 35.4d | $+3,797.18 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $9,631 | -21.41% | -266.09% | -94.99% | 69.24% | -0.29 | -0.28 | -3.84 | 29.4d | $-1,596.63 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $6,579 | +60.04% | +721.62% | +28388.51% | 43.59% | +3.06 | +3.76 | +16.56 | 30.4d | $+2,171.07 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,748 | -3.58% | -37.95% | -32.05% | 5.83% | -2.12 | -1.75 | -6.50 | 34.4d | $-44.46 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,661 | +11.80% | +151.82% | +320.01% | 10.73% | +2.24 | +2.14 | +14.15 | 28.4d | $+279.04 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,624 | -10.89% | -216.53% | -89.90% | 13.68% | -1.28 | -1.79 | -15.83 | 18.4d | $-572.01 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,508 | +30.30% | +419.05% | +3787.90% | 10.24% | +6.30 | +7.06 | +40.93 | 26.4d | $+1,047.67 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,983 | +8.23% | +87.36% | +131.53% | 2.51% | +5.06 | +5.10 | +34.78 | 34.4d | $+179.42 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,499 | +4.14% | +77.95% | +114.64% | 1.18% | +6.96 | +12.14 | +66.11 | 19.4d | $+130.63 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,073 | +20.68% | +170.23% | +369.86% | 10.23% | +2.47 | +4.51 | +16.64 | 44.3d | $+237.68 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
