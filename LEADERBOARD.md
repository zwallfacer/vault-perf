# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-31 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,564 | +10.47% | +49.05% | +59.44% | 57.56% | +1.20 | +1.07 | +0.85 | 77.9d | $+628.69 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,309 | +7.34% | +34.80% | +39.92% | 7.55% | +1.31 | +1.33 | +4.61 | 76.9d | $+524.76 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $4,756 | -88.82% | -450.80% | -100.00% | 92.09% | -1.49 | -1.77 | -4.90 | 71.9d | $-15,575.09 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,768 | -3.09% | -14.66% | -13.84% | 13.59% | -0.48 | -0.40 | -1.08 | 76.9d | $-346.33 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,533 | +6.08% | +35.80% | +41.55% | 4.68% | +2.62 | +2.33 | +7.65 | 62.0d | $+189.18 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,476 | +34.91% | +161.36% | +299.12% | 47.44% | +1.63 | +2.06 | +3.40 | 79.0d | $+1,266.87 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,970 | -0.96% | -8.74% | -8.41% | 1.37% | -2.45 | -2.09 | -6.39 | 39.9d | $-30.64 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,812 | +37.47% | +157.38% | +280.62% | 10.23% | +2.68 | +4.11 | +15.39 | 86.9d | $+498.56 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,714 | -26.40% | -139.78% | -80.27% | 60.35% | -0.33 | -0.34 | -2.32 | 68.9d | $-974.29 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -67.91% | -51.36% | 22.12% | -1.26 | -1.57 | -3.07 | 60.9d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
