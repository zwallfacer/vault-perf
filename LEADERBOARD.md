# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-20 08:52 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,114 | -17.89% | -98.34% | -66.16% | 57.56% | +0.09 | +0.09 | -1.71 | 66.4d | $-2,853.14 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,990 | -86.01% | -519.85% | -100.00% | 87.42% | -3.42 | -3.12 | -5.95 | 60.4d | $-14,376.82 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,023 | +1.48% | +8.28% | +8.57% | 7.55% | +0.34 | +0.32 | +1.10 | 65.4d | $+235.29 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,643 | -4.05% | -22.58% | -20.59% | 13.59% | -0.97 | -0.81 | -1.66 | 65.4d | $-382.71 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -83.76% | -58.89% | 22.12% | -1.39 | -1.74 | -3.79 | 49.4d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,559 | +6.82% | +49.40% | +61.26% | 2.43% | +4.60 | +5.26 | +20.32 | 50.4d | $+214.10 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,731 | -25.54% | -162.39% | -84.67% | 55.42% | -1.22 | -1.05 | -2.93 | 57.4d | $-942.80 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,560 | -0.66% | -3.58% | -3.53% | 44.13% | +0.77 | +0.96 | -0.08 | 67.4d | $+350.48 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,343 | +37.88% | +183.45% | +373.80% | 10.23% | +3.00 | +4.53 | +17.94 | 75.4d | $+531.30 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,976 | +35.07% | +208.52% | +497.45% | 14.86% | +3.69 | +3.85 | +14.03 | 61.4d | $+513.41 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
