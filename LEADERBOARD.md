# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-19 09:18 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $11,408 | -7.59% | -42.33% | -35.61% | 57.56% | +0.52 | +0.49 | -0.74 | 65.4d | $-1,586.62 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,141 | -83.59% | -513.57% | -100.00% | 87.42% | -3.19 | -2.89 | -5.87 | 59.4d | $-13,355.44 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,062 | +2.26% | +12.80% | +13.49% | 7.55% | +0.51 | +0.49 | +1.70 | 64.4d | $+273.65 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,698 | -2.88% | -16.32% | -15.26% | 13.59% | -0.69 | -0.57 | -1.20 | 64.4d | $-326.35 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -85.46% | -59.63% | 22.12% | -1.41 | -1.75 | -3.86 | 48.4d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,576 | +7.40% | +54.64% | +69.40% | 2.43% | +5.09 | +5.80 | +22.48 | 49.4d | $+233.33 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,726 | +5.98% | +32.82% | +37.55% | 44.13% | +0.99 | +1.22 | +0.74 | 66.5d | $+521.48 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,715 | -26.23% | -169.68% | -86.03% | 55.42% | -1.28 | -1.10 | -3.06 | 56.4d | $-968.15 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,329 | +37.35% | +183.29% | +374.62% | 10.23% | +2.99 | +4.54 | +17.92 | 74.4d | $+522.34 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,972 | +34.91% | +210.98% | +510.82% | 14.86% | +3.70 | +3.90 | +14.20 | 60.4d | $+511.14 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
