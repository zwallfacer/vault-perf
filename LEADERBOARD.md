# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-14 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,827 | +2.62% | +15.67% | +16.73% | 39.11% | +0.92 | +0.88 | +0.40 | 60.9d | $-293.19 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $10,701 | -75.34% | -501.12% | -99.99% | 76.28% | -2.72 | -2.52 | -6.57 | 54.9d | $-9,789.96 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,890 | -1.02% | -6.20% | -6.05% | 7.55% | -0.21 | -0.20 | -0.82 | 59.9d | $+111.54 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,884 | +0.76% | +4.63% | +4.72% | 7.87% | +0.34 | +0.29 | +0.59 | 59.9d | $-150.19 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,929 | -9.56% | -79.56% | -56.67% | 21.26% | -1.21 | -1.51 | -3.74 | 43.9d | $-388.16 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,554 | +6.67% | +54.22% | +69.02% | 2.12% | +5.15 | +5.59 | +25.57 | 44.9d | $+209.00 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,877 | +11.56% | +68.16% | +90.60% | 43.59% | +1.20 | +1.52 | +1.56 | 61.9d | $+665.43 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,699 | -27.09% | -190.53% | -89.16% | 45.57% | -1.56 | -1.31 | -4.18 | 51.9d | $-999.69 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,330 | +36.84% | +192.48% | +414.86% | 10.23% | +3.13 | +4.63 | +18.82 | 69.9d | $+513.57 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,972 | +34.92% | +228.17% | +607.84% | 14.86% | +3.90 | +4.08 | +15.35 | 55.9d | $+511.31 |
| 39 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
