# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-14 10:56 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,169 | +4.70% | +18.97% | +20.37% | 7.55% | +0.78 | +0.76 | +2.51 | 90.5d | $+394.52 |
| 2 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $4,602 | -63.47% | -253.21% | -98.20% | 82.47% | -0.19 | -0.16 | -3.07 | 91.5d | $-8,447.76 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,261 | -2.38% | -11.52% | -11.00% | 10.19% | -0.72 | -0.61 | -1.13 | 75.5d | $-92.57 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,950 | -22.14% | -89.31% | -63.56% | 29.02% | -3.03 | -2.37 | -3.08 | 90.5d | $-1,069.60 |
| 5 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,878 | -4.06% | -27.73% | -24.66% | 4.40% | -4.65 | -3.74 | -6.30 | 53.5d | $-123.80 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,760 | +20.08% | +72.97% | +94.44% | 18.46% | +1.33 | +1.79 | +3.95 | 100.5d | $+125.66 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,607 | -27.82% | -123.10% | -76.37% | 60.35% | -0.20 | -0.22 | -2.04 | 82.5d | $-1,014.01 |
| 8 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,593 | -0.17% | -30.52% | -26.32% | 0.41% | -7.90 | -7.05 | -74.51 | 2.1d | $-4.49 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -55.55% | -44.54% | 22.12% | -1.14 | -1.43 | -2.51 | 74.5d | $-464.92 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,983 | +35.55% | +150.08% | +261.14% | 14.86% | +3.08 | +3.40 | +10.10 | 86.5d | $+520.53 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
