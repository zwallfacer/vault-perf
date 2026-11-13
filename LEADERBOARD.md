# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-13 11:34 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $6,235 | -46.56% | -187.72% | -92.00% | 82.47% | +0.38 | +0.34 | -2.28 | 90.5d | $-6,371.39 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,145 | +4.03% | +16.44% | +17.49% | 7.55% | +0.68 | +0.67 | +2.18 | 89.5d | $+361.38 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,345 | +0.53% | +2.61% | +2.63% | 9.12% | +0.17 | +0.15 | +0.29 | 74.5d | $+4.52 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,004 | -20.75% | -84.61% | -61.26% | 29.02% | -2.83 | -2.21 | -2.92 | 89.5d | $-1,016.83 |
| 5 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,896 | -3.44% | -23.90% | -21.59% | 3.98% | -4.16 | -3.38 | -6.00 | 52.5d | $-105.05 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,852 | +24.94% | +91.49% | +126.34% | 17.50% | +1.64 | +2.24 | +5.23 | 99.5d | $+236.89 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,819 | -20.10% | -90.01% | -63.39% | 60.35% | +0.08 | +0.09 | -1.49 | 81.5d | $-737.47 |
| 8 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,597 | +0.00% | +0.00% | +0.00% | 0.00% | — | — | — | 1.1d | $+0.00 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -56.28% | -44.97% | 22.12% | -1.14 | -1.43 | -2.54 | 73.5d | $-464.91 |
| 10 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ✂ | $2,017 | -46.57% | -1837.11% | -100.00% | 80.15% | -1.82 | -1.70 | -22.92 | 9.3d | $-1,740.80 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
