# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-08 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,390 | +8.99% | +38.62% | +44.74% | 7.55% | +1.51 | +1.49 | +5.12 | 84.9d | $+606.35 |
| 2 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,357 | -57.66% | -244.91% | -97.40% | 79.28% | -0.27 | -0.23 | -3.09 | 85.9d | $-7,734.50 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,478 | +4.30% | +22.44% | +24.57% | 4.68% | +1.48 | +1.32 | +4.79 | 70.0d | $+130.04 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,202 | -15.52% | -66.70% | -51.56% | 22.76% | -2.14 | -1.66 | -2.93 | 84.9d | $-818.65 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,074 | +33.74% | +129.75% | +205.90% | 10.23% | +2.26 | +3.26 | +12.69 | 94.9d | $+438.51 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,956 | -1.45% | -11.03% | -10.52% | 1.71% | -2.07 | -1.75 | -6.44 | 47.9d | $-45.40 |
| 7 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $2,739 | -93.59% | — | — | — | — | — | — | 79.9d | $-17,607.37 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,710 | -27.09% | -128.52% | -77.66% | 60.35% | -0.29 | -0.32 | -2.13 | 76.9d | $-987.73 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -60.03% | -47.12% | 22.12% | -1.19 | -1.48 | -2.71 | 68.9d | $-464.90 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,291 | -12.48% | -52.38% | -42.85% | 47.99% | +0.52 | +0.61 | -1.09 | 87.0d | $+45.99 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
