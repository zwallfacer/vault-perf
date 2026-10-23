# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-23 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,281 | -19.17% | -100.12% | -67.09% | 57.56% | +0.19 | +0.16 | -1.74 | 69.9d | $-3,010.18 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,347 | -82.78% | -473.05% | -100.00% | 92.09% | -1.22 | -1.50 | -5.14 | 63.9d | $-13,000.83 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,087 | +3.17% | +16.80% | +17.99% | 7.55% | +0.66 | +0.65 | +2.23 | 68.9d | $+318.74 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,800 | -2.20% | -11.63% | -11.10% | 13.59% | -0.37 | -0.31 | -0.86 | 68.9d | $-311.55 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,567 | +6.87% | +46.50% | +56.79% | 2.43% | +4.24 | +4.30 | +19.13 | 53.9d | $+215.55 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,997 | -19.66% | -117.83% | -73.07% | 55.42% | -0.29 | -0.29 | -2.13 | 60.9d | $-726.32 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,992 | -0.27% | -3.13% | -3.09% | 0.97% | -0.91 | -0.82 | -3.24 | 31.9d | $-9.86 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,906 | +40.71% | +188.45% | +385.96% | 10.23% | +3.08 | +4.61 | +18.42 | 78.9d | $+564.86 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,556 | -4.80% | -24.69% | -22.35% | 44.13% | +0.65 | +0.77 | -0.56 | 70.9d | $+243.93 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -78.24% | -56.41% | 22.12% | -1.35 | -1.67 | -3.54 | 52.9d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
