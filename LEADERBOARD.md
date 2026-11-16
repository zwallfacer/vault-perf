# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-16 12:03 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,203 | +5.25% | +20.71% | +22.37% | 7.55% | +0.85 | +0.83 | +2.75 | 92.5d | $+421.62 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,148 | -6.23% | -29.33% | -26.13% | 18.94% | -0.69 | -0.59 | -1.55 | 77.6d | $-220.77 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,973 | -21.55% | -85.02% | -61.62% | 30.27% | -2.83 | -2.24 | -2.81 | 92.5d | $-1,047.39 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,846 | -5.14% | -33.76% | -29.29% | 5.86% | -4.68 | -3.68 | -5.76 | 55.5d | $-155.94 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,620 | +13.62% | +48.49% | +57.56% | 26.04% | +0.87 | +1.01 | +1.86 | 102.5d | $-22.49 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,589 | -0.31% | -27.95% | -24.42% | 0.81% | -2.26 | -3.55 | -34.55 | 4.1d | $-8.18 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -54.06% | -43.66% | 22.12% | -1.12 | -1.41 | -2.44 | 76.5d | $-464.92 |
| 8 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,984 | +35.47% | +146.26% | +249.66% | 14.86% | +3.03 | +3.36 | +9.84 | 88.5d | $+519.27 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,741 | -49.20% | -212.41% | -94.63% | 66.51% | -0.93 | -0.93 | -3.19 | 84.5d | $-1,779.80 |
| 10 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,385 | -7.90% | -51.50% | -41.52% | 10.89% | -3.94 | -3.80 | -4.73 | 56.0d | $-118.57 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
