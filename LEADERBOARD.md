# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-13 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $5,644 | -54.67% | -219.43% | -95.82% | 82.47% | +0.13 | +0.12 | -2.66 | 90.9d | $-7,367.18 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,155 | +4.13% | +16.76% | +17.85% | 7.55% | +0.70 | +0.69 | +2.22 | 89.9d | $+366.18 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,338 | +0.01% | +0.05% | +0.05% | 9.12% | +0.00 | +0.00 | +0.01 | 75.0d | $-12.83 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,013 | -20.49% | -83.17% | -60.57% | 29.02% | -2.79 | -2.17 | -2.87 | 89.9d | $-1,007.11 |
| 5 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,892 | -3.71% | -25.60% | -22.96% | 3.98% | -4.31 | -3.46 | -6.42 | 52.9d | $-113.23 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,845 | +23.64% | +86.37% | +117.12% | 17.50% | +1.56 | +2.11 | +4.94 | 99.9d | $+207.11 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,750 | -22.04% | -98.16% | -67.01% | 60.35% | +0.01 | +0.01 | -1.63 | 81.9d | $-806.70 |
| 8 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,590 | -0.29% | -71.21% | -50.99% | 0.41% | — | — | -173.88 | 1.5d | $-7.63 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -55.97% | -44.79% | 22.12% | -1.14 | -1.43 | -2.53 | 73.9d | $-464.91 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,985 | +35.48% | +150.76% | +263.37% | 14.86% | +3.09 | +3.44 | +10.14 | 85.9d | $+519.51 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
