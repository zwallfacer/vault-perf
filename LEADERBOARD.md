# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-06 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,882 | -51.03% | -221.92% | -95.52% | 76.39% | -0.26 | -0.21 | -2.91 | 83.9d | $-6,920.91 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,346 | +8.08% | +35.55% | +40.75% | 7.55% | +1.38 | +1.39 | +4.71 | 82.9d | $+561.38 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,511 | +5.39% | +28.96% | +32.58% | 4.68% | +1.89 | +1.66 | +6.18 | 68.0d | $+166.35 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,289 | -13.22% | -58.19% | -46.42% | 20.65% | -1.81 | -1.39 | -2.82 | 82.9d | $-731.48 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,117 | +37.10% | +145.76% | +245.47% | 10.23% | +2.50 | +3.59 | +14.25 | 92.9d | $+515.57 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,955 | -1.43% | -11.35% | -10.80% | 1.71% | -2.08 | -1.76 | -6.63 | 45.9d | $-44.76 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,872 | -18.00% | -87.68% | -61.97% | 60.35% | +0.05 | +0.06 | -1.45 | 74.9d | $-662.17 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,483 | -2.80% | -12.03% | -11.49% | 47.44% | +0.78 | +0.91 | -0.25 | 85.0d | $+295.36 |
| 9 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $2,407 | -94.12% | — | — | — | — | — | — | 77.9d | $-17,834.03 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -61.82% | -48.11% | 22.12% | -1.20 | -1.49 | -2.79 | 66.9d | $-464.90 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
