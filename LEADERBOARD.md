# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-20 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $11,136 | -9.17% | -50.04% | -40.83% | 57.56% | +0.46 | +0.43 | -0.87 | 66.9d | $-1,782.41 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,439 | -84.91% | -509.12% | -100.00% | 87.42% | -3.32 | -3.06 | -5.82 | 60.9d | $-13,908.21 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,988 | +0.81% | +4.46% | +4.54% | 7.55% | +0.20 | +0.19 | +0.59 | 65.9d | $+201.73 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,855 | -0.80% | -4.44% | -4.36% | 13.59% | -0.11 | -0.09 | -0.33 | 65.9d | $-257.38 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -82.95% | -58.54% | 22.12% | -1.39 | -1.72 | -3.75 | 49.9d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,579 | +7.53% | +53.99% | +68.30% | 2.43% | +5.14 | +5.79 | +22.21 | 50.9d | $+237.64 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,834 | -22.10% | -139.30% | -79.28% | 55.42% | -0.93 | -0.81 | -2.51 | 57.9d | $-816.00 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,746 | +6.98% | +37.49% | +43.67% | 44.13% | +1.02 | +1.24 | +0.85 | 67.9d | $+547.24 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,381 | +40.59% | +195.33% | +415.19% | 10.23% | +3.18 | +4.82 | +19.10 | 75.9d | $+577.33 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,977 | +35.13% | +207.24% | +490.68% | 14.86% | +3.69 | +3.86 | +13.95 | 61.9d | $+514.28 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
