# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-02 21:59 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,831 | +59.10% | +440.63% | +3088.57% | 24.43% | +3.58 | +3.64 | +18.04 | 49.0d | $+6,728.85 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,167 | -65.54% | -557.20% | -99.99% | 73.12% | -3.05 | -2.95 | -7.62 | 42.9d | $-6,296.52 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,134 | +6.11% | +46.55% | +57.12% | 2.99% | +2.70 | +2.69 | +15.59 | 47.9d | $+108.70 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,811 | -2.73% | -20.79% | -19.01% | 7.55% | -0.85 | -0.77 | -2.76 | 48.0d | $+26.78 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $4,019 | -17.28% | -197.64% | -88.58% | 18.61% | -3.33 | -4.07 | -10.62 | 31.9d | $-922.37 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,514 | +5.09% | +56.35% | +73.26% | 2.12% | +5.19 | +6.75 | +26.58 | 33.0d | $+158.65 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,329 | -10.18% | -93.02% | -62.51% | 32.95% | -0.97 | -0.76 | -2.82 | 40.0d | $-377.84 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,271 | +31.05% | +226.73% | +620.36% | 43.59% | +1.98 | +2.64 | +5.20 | 50.0d | $+1,174.62 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,224 | +27.86% | +175.59% | +370.65% | 10.23% | +2.70 | +4.38 | +17.17 | 57.9d | $+359.85 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,877 | +27.88% | +231.64% | +671.57% | 14.86% | +4.20 | +4.92 | +15.59 | 43.9d | $+408.15 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
