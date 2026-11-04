# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-04 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,555 | -14.55% | -64.81% | -50.36% | 57.56% | +0.49 | +0.43 | -1.13 | 81.9d | $-2,442.78 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,340 | +7.93% | +35.75% | +41.06% | 7.55% | +1.38 | +1.38 | +4.74 | 80.9d | $+553.97 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $5,102 | -87.87% | — | — | — | — | — | — | 75.9d | $-15,169.54 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,688 | -5.20% | -23.46% | -21.41% | 17.18% | -0.77 | -0.63 | -1.37 | 80.9d | $-428.38 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,568 | +7.06% | +39.05% | +45.84% | 4.68% | +2.77 | +2.54 | +8.34 | 66.0d | $+221.81 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,149 | -15.47% | -77.42% | -56.88% | 60.35% | +0.15 | +0.17 | -1.28 | 72.9d | $-572.34 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,042 | +15.14% | +66.59% | +85.91% | 47.44% | +1.18 | +1.47 | +1.40 | 83.0d | $+757.48 |
| 8 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,989 | -0.33% | -2.78% | -2.75% | 1.43% | -0.65 | -0.61 | -1.94 | 43.9d | $-11.99 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,910 | +42.21% | +169.49% | +311.23% | 10.23% | +2.88 | +4.45 | +16.57 | 90.9d | $+595.43 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -63.72% | -49.15% | 22.12% | -1.22 | -1.52 | -2.88 | 64.9d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
