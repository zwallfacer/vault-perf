# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-29 21:46 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,065 | +53.27% | +423.19% | +2873.78% | 24.43% | +3.47 | +3.54 | +17.32 | 45.9d | $+6,004.34 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,014 | -66.42% | -607.17% | -100.00% | 73.12% | -3.49 | -3.37 | -8.30 | 39.9d | $-6,452.41 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,700 | +7.56% | +61.41% | +80.75% | 2.90% | +3.53 | +3.55 | +21.16 | 44.9d | $+174.76 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,691 | -5.03% | -40.85% | -34.24% | 7.55% | -1.65 | -1.52 | -5.41 | 45.0d | $-86.92 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,576 | +24.07% | +237.75% | +741.76% | 11.46% | +4.01 | +4.52 | +20.74 | 37.0d | $+881.98 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $4,517 | +29.14% | +226.39% | +629.20% | 43.59% | +2.00 | +2.67 | +5.19 | 47.0d | $+1,133.43 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,248 | -18.23% | -230.11% | -92.12% | 14.14% | -2.58 | -3.36 | -16.27 | 28.9d | $-952.42 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,545 | +5.41% | +65.96% | +90.10% | 2.12% | +6.31 | +8.28 | +31.11 | 30.0d | $+173.38 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,252 | +31.26% | +207.77% | +509.79% | 10.23% | +3.15 | +5.26 | +20.31 | 54.9d | $+419.21 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,841 | +25.79% | +230.05% | +674.18% | 6.34% | +5.01 | +5.24 | +36.30 | 40.9d | $+377.58 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
