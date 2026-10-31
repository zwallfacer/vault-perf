# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-31 09:57 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,276 | +8.61% | +40.58% | +47.60% | 57.56% | +1.15 | +1.02 | +0.71 | 77.5d | $+400.18 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,306 | +7.28% | +34.73% | +39.83% | 7.55% | +1.30 | +1.32 | +4.60 | 76.5d | $+521.75 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $4,792 | -88.75% | -453.47% | -100.00% | 92.09% | -1.48 | -1.74 | -4.92 | 71.4d | $-15,545.26 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,739 | -3.79% | -18.08% | -16.83% | 13.59% | -0.62 | -0.51 | -1.33 | 76.4d | $-373.37 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,521 | +5.74% | +34.06% | +39.27% | 4.68% | +2.46 | +2.19 | +7.28 | 61.5d | $+177.88 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,382 | +32.20% | +149.76% | +266.30% | 47.44% | +1.58 | +1.99 | +3.16 | 78.5d | $+1,197.11 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,969 | -0.97% | -8.98% | -8.63% | 1.37% | -2.49 | -2.12 | -6.57 | 39.4d | $-31.07 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,759 | +34.92% | +147.47% | +254.28% | 10.23% | +2.53 | +3.86 | +14.42 | 86.4d | $+446.40 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -68.45% | -51.64% | 22.12% | -1.26 | -1.57 | -3.09 | 60.4d | $-464.89 |
| 10 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,000 | -45.71% | -243.73% | -96.15% | 60.35% | -1.58 | -1.52 | -4.04 | 68.5d | $-1,684.61 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
