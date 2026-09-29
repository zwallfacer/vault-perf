# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-29 10:08 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,783 | +51.29% | +411.75% | +2676.63% | 24.43% | +3.39 | +3.46 | +16.85 | 45.5d | $+5,757.30 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,868 | -67.08% | -620.72% | -100.00% | 73.12% | -3.56 | -3.43 | -8.49 | 39.4d | $-6,569.89 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $4,774 | +37.31% | +292.92% | +1105.33% | 43.59% | +2.28 | +2.98 | +6.72 | 46.5d | $+1,418.47 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,734 | -4.25% | -34.87% | -29.97% | 7.55% | -1.40 | -1.26 | -4.62 | 44.5d | $-48.19 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,701 | +7.58% | +62.20% | +82.13% | 2.90% | +3.53 | +3.55 | +21.43 | 44.5d | $+175.42 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,521 | +23.00% | +230.24% | +694.29% | 11.46% | +3.85 | +4.34 | +20.09 | 36.5d | $+842.78 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,272 | -17.69% | -227.11% | -91.79% | 13.68% | -2.45 | -3.20 | -16.60 | 28.4d | $-924.50 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,538 | +5.20% | +64.37% | +87.29% | 2.12% | +6.14 | +7.95 | +30.36 | 29.5d | $+166.11 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,290 | +33.54% | +224.93% | +595.64% | 10.23% | +3.37 | +5.54 | +21.99 | 54.4d | $+458.34 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,834 | +25.44% | +229.62% | +673.56% | 6.34% | +4.92 | +5.15 | +36.23 | 40.4d | $+372.42 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
