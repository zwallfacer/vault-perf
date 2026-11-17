# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-17 23:36 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,220 | +5.55% | +21.54% | +23.32% | 7.55% | +0.89 | +0.87 | +2.85 | 94.0d | $+436.28 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,265 | -2.14% | -9.87% | -9.49% | 18.94% | -0.13 | -0.11 | -0.52 | 79.0d | $-84.37 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,936 | -22.56% | -87.59% | -62.94% | 30.27% | -2.97 | -2.36 | -2.89 | 94.0d | $-1,085.53 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,852 | -4.89% | -31.33% | -27.48% | 5.86% | -4.43 | -3.47 | -5.35 | 57.0d | $-148.70 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,708 | +18.06% | +63.38% | +79.08% | 26.04% | +1.11 | +1.28 | +2.43 | 104.0d | $+79.22 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,564 | -1.25% | -81.72% | -56.06% | 1.78% | -6.23 | -6.98 | -45.91 | 5.6d | $-32.52 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -53.04% | -43.04% | 22.12% | -1.11 | -1.39 | -2.40 | 78.0d | $-464.92 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,204 | -38.58% | -163.68% | -87.36% | 66.51% | -0.47 | -0.48 | -2.46 | 86.0d | $-1,399.30 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,984 | +35.52% | +144.05% | +243.04% | 14.86% | +3.02 | +3.33 | +9.69 | 90.0d | $+520.01 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $1,562 | -36.67% | -139.36% | -82.38% | 77.96% | +0.23 | +0.25 | -1.79 | 96.1d | $-560.37 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
