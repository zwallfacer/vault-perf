# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-18 08:20 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,696 | -20.23% | -114.67% | -72.23% | 54.76% | -0.12 | -0.11 | -2.09 | 64.4d | $-3,138.34 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,856 | -84.14% | -526.16% | -100.00% | 87.42% | -3.28 | -3.01 | -6.02 | 58.4d | $-13,592.64 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,019 | +1.41% | +8.13% | +8.41% | 7.55% | +0.33 | +0.32 | +1.08 | 63.4d | $+231.77 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,658 | -3.68% | -21.22% | -19.44% | 11.93% | -0.94 | -0.77 | -1.78 | 63.4d | $-365.20 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -87.34% | -60.43% | 22.12% | -1.42 | -1.76 | -3.95 | 47.4d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,564 | +6.98% | +52.66% | +66.37% | 2.43% | +4.89 | +5.44 | +21.67 | 48.4d | $+219.42 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,596 | +0.70% | +3.88% | +3.94% | 43.59% | +0.83 | +1.03 | +0.09 | 65.4d | $+385.44 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,520 | -31.03% | -204.50% | -91.36% | 52.13% | -1.73 | -1.49 | -3.92 | 55.4d | $-1,144.73 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,257 | +33.03% | +164.37% | +313.84% | 10.23% | +2.73 | +4.15 | +16.07 | 73.3d | $+448.94 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,978 | +34.96% | +214.95% | +531.80% | 14.86% | +3.74 | +3.88 | +14.46 | 59.4d | $+511.80 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
