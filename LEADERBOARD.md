# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-15 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,439 | +1.57% | +9.25% | +9.61% | 50.72% | +0.89 | +0.83 | +0.18 | 61.9d | $-423.27 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $8,333 | -80.52% | -526.01% | -100.00% | 83.26% | -3.21 | -2.94 | -6.32 | 55.9d | $-12,029.62 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,903 | +1.36% | +8.16% | +8.44% | 10.75% | +0.52 | +0.44 | +0.76 | 60.9d | $-121.10 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,854 | -1.29% | -7.71% | -7.47% | 7.55% | -0.27 | -0.26 | -1.02 | 60.9d | $+98.26 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -92.19% | -62.41% | 22.12% | -1.47 | -1.82 | -4.17 | 44.9d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,590 | +7.79% | +61.91% | +81.52% | 2.43% | +5.82 | +6.47 | +25.47 | 45.9d | $+246.18 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,924 | +13.99% | +81.13% | +113.69% | 43.59% | +1.27 | +1.59 | +1.86 | 62.9d | $+727.84 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,594 | -29.50% | -203.55% | -91.04% | 52.13% | -1.70 | -1.44 | -3.90 | 52.9d | $-1,088.29 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,341 | +37.82% | +194.81% | +421.92% | 10.23% | +3.17 | +4.75 | +19.05 | 70.9d | $+530.20 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,973 | +34.78% | +223.24% | +579.23% | 14.86% | +3.84 | +3.98 | +15.02 | 56.9d | $+509.21 |
| 40 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
