# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-17 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,302 | -17.28% | -98.72% | -66.17% | 51.93% | +0.03 | +0.03 | -1.90 | 63.9d | $-2,766.52 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,656 | -82.30% | -519.07% | -100.00% | 83.26% | -3.39 | -3.14 | -6.23 | 57.9d | $-12,799.95 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,976 | +0.65% | +3.78% | +3.84% | 7.55% | +0.17 | +0.16 | +0.50 | 62.9d | $+194.13 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,714 | -2.57% | -14.93% | -14.04% | 11.38% | -0.64 | -0.53 | -1.31 | 62.9d | $-311.44 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -88.26% | -60.81% | 22.12% | -1.44 | -1.80 | -3.99 | 46.9d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,569 | +7.17% | +54.64% | +69.50% | 2.43% | +5.14 | +5.89 | +22.48 | 47.9d | $+225.67 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,733 | -25.92% | -172.34% | -86.40% | 52.13% | -1.34 | -1.15 | -3.31 | 54.9d | $-956.63 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,650 | +2.86% | +16.10% | +17.21% | 43.59% | +0.90 | +1.14 | +0.37 | 64.9d | $+441.32 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,295 | +35.16% | +176.13% | +352.34% | 10.23% | +2.92 | +4.44 | +17.22 | 72.9d | $+485.00 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,971 | +34.63% | +214.70% | +531.91% | 14.86% | +3.74 | +3.91 | +14.45 | 58.9d | $+506.94 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
