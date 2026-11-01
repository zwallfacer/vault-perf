# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-01 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,531 | +11.35% | +52.50% | +64.42% | 57.56% | +1.22 | +1.08 | +0.91 | 78.9d | $+736.59 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,311 | +7.36% | +34.48% | +39.47% | 7.55% | +1.31 | +1.32 | +4.57 | 77.9d | $+526.01 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,203 | -87.76% | -439.30% | -100.00% | 92.09% | -1.35 | -1.59 | -4.77 | 72.9d | $-15,122.69 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,716 | -4.38% | -20.50% | -18.91% | 13.59% | -0.73 | -0.60 | -1.51 | 77.9d | $-396.32 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,528 | +5.95% | +34.52% | +39.83% | 4.68% | +2.54 | +2.29 | +7.37 | 63.0d | $+185.08 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,398 | +33.64% | +153.56% | +275.73% | 47.44% | +1.60 | +2.03 | +3.24 | 80.0d | $+1,234.24 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,972 | -0.87% | -7.75% | -7.48% | 1.37% | -2.18 | -1.84 | -5.66 | 40.9d | $-28.00 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,793 | +36.84% | +152.96% | +267.77% | 10.23% | +2.62 | +4.04 | +14.95 | 87.9d | $+485.63 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,784 | -24.20% | -126.28% | -76.44% | 60.35% | -0.26 | -0.28 | -2.09 | 69.9d | $-893.27 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -66.81% | -50.79% | 22.12% | -1.25 | -1.56 | -3.02 | 61.9d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
