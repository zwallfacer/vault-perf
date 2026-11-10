# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-10 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` ⚠ | $5,594 | -86.70% | — | — | — | — | — | — | 81.9d | $-14,669.86 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,159 | +4.54% | +19.07% | +20.50% | 7.55% | +0.78 | +0.76 | +2.53 | 86.9d | $+386.55 |
| 3 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $4,542 | -59.92% | -248.70% | -97.75% | 82.47% | -0.16 | -0.14 | -3.02 | 87.9d | $-8,011.44 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,414 | +2.55% | +12.95% | +13.64% | 5.73% | +0.84 | +0.73 | +2.26 | 72.0d | $+71.81 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,046 | -19.63% | -82.43% | -60.06% | 26.90% | -2.70 | -2.10 | -3.06 | 86.9d | $-974.51 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,981 | -12.28% | -56.76% | -45.42% | 60.35% | +0.33 | +0.36 | -0.94 | 78.9d | $-457.02 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,935 | -1.94% | -14.19% | -13.35% | 2.40% | -2.66 | -2.22 | -5.91 | 49.9d | $-60.15 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,814 | +26.95% | +101.51% | +145.67% | 16.61% | +1.80 | +2.47 | +6.11 | 96.9d | $+282.99 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -58.34% | -46.16% | 22.12% | -1.17 | -1.47 | -2.64 | 70.9d | $-464.91 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,983 | +35.68% | +157.09% | +283.21% | 14.86% | +3.17 | +3.42 | +10.57 | 82.9d | $+522.42 |
| 43 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
