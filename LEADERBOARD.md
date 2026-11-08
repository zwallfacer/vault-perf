# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-08 10:46 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,687 | -53.46% | -228.27% | -96.18% | 79.28% | -0.10 | -0.09 | -2.88 | 85.5d | $-7,219.33 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,373 | +8.62% | +37.25% | +42.95% | 7.55% | +1.45 | +1.44 | +4.94 | 84.5d | $+588.43 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,483 | +4.64% | +24.38% | +26.90% | 4.68% | +1.60 | +1.43 | +5.21 | 69.5d | $+141.40 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,227 | -14.84% | -64.13% | -50.05% | 22.16% | -2.04 | -1.58 | -2.89 | 84.5d | $-793.03 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $3,081 | +34.53% | +133.46% | +214.69% | 10.23% | +2.31 | +3.29 | +13.05 | 94.4d | $+456.83 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,956 | -1.40% | -10.74% | -10.25% | 1.71% | -1.99 | -1.65 | -6.27 | 47.5d | $-43.86 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,844 | -19.85% | -94.70% | -65.20% | 60.35% | -0.02 | -0.02 | -1.57 | 76.5d | $-728.19 |
| 8 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $2,803 | -93.42% | — | — | — | — | — | — | 79.5d | $-17,538.43 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,355 | -8.29% | -34.98% | -30.59% | 47.44% | +0.63 | +0.74 | -0.74 | 86.5d | $+153.94 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -60.42% | -47.34% | 22.12% | -1.19 | -1.48 | -2.73 | 68.5d | $-464.90 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
