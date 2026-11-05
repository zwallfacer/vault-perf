# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-05 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,699 | -58.85% | -259.01% | -97.99% | 76.25% | -0.76 | -0.60 | -3.40 | 82.9d | $-7,880.79 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,343 | +8.06% | +35.89% | +41.22% | 7.55% | +1.39 | +1.38 | +4.76 | 81.9d | $+560.39 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $4,319 | -90.52% | — | — | — | — | — | — | 76.9d | $-16,301.85 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,515 | +5.11% | +27.86% | +31.22% | 4.68% | +1.84 | +1.63 | +5.95 | 67.0d | $+157.00 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,343 | -11.84% | -52.74% | -42.96% | 20.19% | -1.63 | -1.25 | -2.61 | 81.9d | $-679.14 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,214 | -11.61% | -57.32% | -45.63% | 60.35% | +0.29 | +0.33 | -0.95 | 73.9d | $-433.22 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,127 | +35.73% | +141.93% | +236.53% | 10.23% | +2.43 | +3.53 | +13.88 | 91.9d | $+484.32 |
| 8 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,958 | -1.37% | -11.17% | -10.64% | 1.62% | -2.04 | -1.71 | -6.91 | 44.9d | $-43.19 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,502 | -5.48% | -23.84% | -21.74% | 47.44% | +0.70 | +0.83 | -0.50 | 84.0d | $+226.25 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -62.76% | -48.63% | 22.12% | -1.21 | -1.52 | -2.84 | 65.9d | $-464.90 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
