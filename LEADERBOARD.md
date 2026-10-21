# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-21 08:53 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,349 | -1.67% | -9.04% | -8.71% | 57.56% | +0.77 | +0.70 | -0.16 | 67.4d | $-861.57 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,411 | -85.11% | -506.04% | -100.00% | 87.42% | -3.35 | -3.11 | -5.79 | 61.4d | $-13,993.65 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,990 | +1.05% | +5.77% | +5.91% | 7.55% | +0.25 | +0.24 | +0.76 | 66.4d | $+213.81 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,924 | +0.86% | +4.74% | +4.84% | 13.59% | +0.33 | +0.28 | +0.35 | 66.4d | $-192.66 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -82.10% | -58.16% | 22.12% | -1.38 | -1.68 | -3.71 | 50.4d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,596 | +7.98% | +56.67% | +72.50% | 2.43% | +5.38 | +6.01 | +23.31 | 51.4d | $+252.76 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,145 | -14.75% | -92.19% | -63.12% | 55.42% | -0.33 | -0.30 | -1.66 | 58.4d | $-545.93 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,880 | +11.24% | +59.92% | +76.46% | 44.13% | +1.14 | +1.39 | +1.36 | 68.4d | $+656.99 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,367 | +39.35% | +188.07% | +388.35% | 10.23% | +3.08 | +4.70 | +18.39 | 76.4d | $+556.23 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,973 | +34.85% | +203.93% | +475.22% | 14.86% | +3.63 | +3.85 | +13.72 | 62.4d | $+510.28 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
