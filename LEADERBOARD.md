# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-10 11:47 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $6,200 | -85.45% | — | — | — | — | — | — | 81.5d | $-14,139.75 |
| 2 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,567 | -54.58% | -227.61% | -96.28% | 82.47% | +0.02 | +0.02 | -2.76 | 87.5d | $-7,356.61 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,230 | +5.77% | +24.32% | +26.68% | 7.55% | +0.97 | +0.96 | +3.22 | 86.5d | $+447.09 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,444 | +3.39% | +17.30% | +18.55% | 5.24% | +1.13 | +1.00 | +3.30 | 71.5d | $+99.75 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,106 | -18.07% | -76.23% | -56.87% | 25.14% | -2.50 | -1.95 | -3.03 | 86.5d | $-915.35 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,946 | +28.55% | +108.00% | +158.59% | 12.57% | +1.90 | +2.65 | +8.59 | 96.5d | $+319.74 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,944 | -1.81% | -13.37% | -12.62% | 2.13% | -2.50 | -2.10 | -6.27 | 49.5d | $-56.33 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,756 | -23.21% | -107.87% | -70.70% | 60.35% | -0.07 | -0.08 | -1.79 | 78.5d | $-848.74 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -58.67% | -46.35% | 22.12% | -1.17 | -1.47 | -2.65 | 70.5d | $-464.91 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,988 | +35.86% | +158.65% | +287.98% | 14.86% | +3.19 | +3.44 | +10.68 | 82.5d | $+525.02 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
