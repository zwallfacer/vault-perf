# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-15 11:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,182 | +4.76% | +19.00% | +20.40% | 7.55% | +0.79 | +0.76 | +2.52 | 91.5d | $+397.56 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,188 | -4.14% | -19.74% | -18.26% | 18.94% | -0.42 | -0.35 | -1.04 | 76.5d | $-151.05 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,898 | -23.54% | -93.91% | -65.72% | 30.09% | -3.22 | -2.52 | -3.12 | 91.5d | $-1,122.77 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,858 | -4.70% | -31.49% | -27.57% | 5.86% | -4.29 | -3.39 | -5.38 | 54.5d | $-142.96 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,681 | +17.10% | +61.51% | +76.44% | 26.04% | +1.07 | +1.25 | +2.36 | 101.5d | $+57.33 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,585 | -0.46% | -54.72% | -42.21% | 0.81% | -7.76 | -7.70 | -67.64 | 3.1d | $-12.03 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,434 | -32.09% | -140.23% | -81.57% | 60.35% | -0.18 | -0.19 | -2.32 | 83.5d | $-1,166.76 |
| 8 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -54.80% | -44.10% | 22.12% | -1.13 | -1.42 | -2.48 | 75.5d | $-464.92 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,986 | +35.62% | +148.60% | +256.47% | 14.86% | +3.07 | +3.37 | +10.00 | 87.5d | $+521.49 |
| 10 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $1,622 | -86.83% | -342.54% | -99.97% | 93.68% | -0.71 | -0.57 | -3.66 | 92.5d | $-11,314.39 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
