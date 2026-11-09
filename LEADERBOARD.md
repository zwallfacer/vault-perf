# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-09 12:08 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,351 | +8.25% | +35.19% | +40.23% | 7.55% | +1.38 | +1.38 | +4.66 | 85.6d | $+569.78 |
| 2 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $4,249 | -63.82% | -269.14% | -98.63% | 82.47% | -0.53 | -0.45 | -3.26 | 86.5d | $-8,490.06 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,448 | +3.72% | +19.26% | +20.82% | 5.24% | +1.26 | +1.10 | +3.68 | 70.6d | $+110.81 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,160 | -16.68% | -71.18% | -54.10% | 24.75% | -2.30 | -1.79 | -2.88 | 85.5d | $-862.67 |
| 5 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $3,027 | -92.87% | — | — | — | — | — | — | 80.5d | $-17,301.32 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,988 | +30.75% | +117.53% | +178.64% | 12.06% | +2.05 | +2.87 | +9.75 | 95.5d | $+370.18 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,944 | -1.79% | -13.46% | -12.70% | 2.13% | -2.51 | -2.12 | -6.32 | 48.5d | $-55.63 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,588 | -27.21% | -128.06% | -77.57% | 60.35% | -0.27 | -0.29 | -2.12 | 77.5d | $-991.94 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -59.50% | -46.82% | 22.12% | -1.18 | -1.48 | -2.69 | 69.5d | $-464.90 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,986 | +35.63% | +159.54% | +291.43% | 14.86% | +3.19 | +3.40 | +10.74 | 81.5d | $+521.67 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
