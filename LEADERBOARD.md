# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-05 11:29 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,107 | -25.99% | -114.97% | -73.59% | 57.56% | +0.12 | +0.10 | -2.00 | 82.5d | $-3,847.20 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $5,410 | -87.34% | — | — | — | — | — | — | 76.5d | $-14,943.93 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,343 | +8.05% | +36.03% | +41.42% | 7.55% | +1.39 | +1.38 | +4.78 | 81.5d | $+559.93 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,580 | -5.65% | -25.28% | -22.91% | 17.18% | -0.83 | -0.68 | -1.47 | 81.5d | $-444.41 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,580 | +7.41% | +40.62% | +47.98% | 4.68% | +2.83 | +2.68 | +8.68 | 66.5d | $+233.44 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,172 | -12.80% | -63.54% | -49.33% | 60.35% | +0.25 | +0.28 | -1.05 | 73.5d | $-475.74 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,990 | -0.29% | -2.40% | -2.37% | 1.43% | -0.52 | -0.51 | -1.67 | 44.5d | $-10.73 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,882 | +11.90% | +51.99% | +63.43% | 47.44% | +1.10 | +1.38 | +1.10 | 83.5d | $+674.11 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,690 | +44.42% | +177.25% | +333.47% | 10.23% | +2.99 | +4.60 | +17.33 | 91.5d | $+639.67 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -63.16% | -48.85% | 22.12% | -1.21 | -1.52 | -2.85 | 65.5d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
