# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-03 22:18 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $20,277 | +63.28% | +462.26% | +3492.85% | 24.43% | +3.68 | +3.82 | +18.92 | 50.0d | $+7,248.90 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,135 | -65.46% | -543.61% | -99.99% | 73.12% | -3.01 | -2.95 | -7.43 | 43.9d | $-6,280.66 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,157 | +6.59% | +49.11% | +60.90% | 3.02% | +2.87 | +2.84 | +16.24 | 49.0d | $+131.77 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,739 | -4.13% | -30.79% | -26.98% | 7.55% | -1.25 | -1.13 | -4.08 | 49.0d | $-42.45 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $4,102 | -15.71% | -174.13% | -84.96% | 18.67% | -2.88 | -3.50 | -9.33 | 32.9d | $-845.98 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,576 | +44.28% | +316.94% | +1278.91% | 43.59% | +2.36 | +3.14 | +7.27 | 51.0d | $+1,504.30 |
| 7 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,528 | +5.50% | +59.09% | +77.75% | 2.12% | +5.54 | +7.16 | +27.87 | 34.0d | $+172.40 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,410 | -8.56% | -76.28% | -54.95% | 36.90% | -0.74 | -0.58 | -2.07 | 41.0d | $-318.23 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,265 | +30.32% | +187.80% | +415.68% | 10.23% | +2.90 | +4.57 | +18.36 | 58.9d | $+402.38 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,717 | +20.41% | +165.77% | +352.00% | 14.86% | +2.48 | +2.50 | +11.15 | 44.9d | $+298.83 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
