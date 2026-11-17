# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-17 12:28 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,224 | +5.56% | +21.69% | +23.50% | 7.55% | +0.89 | +0.87 | +2.87 | 93.6d | $+436.83 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,222 | -2.81% | -13.05% | -12.40% | 18.94% | -0.22 | -0.19 | -0.69 | 78.6d | $-106.80 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,943 | -22.34% | -87.16% | -62.71% | 30.27% | -2.94 | -2.33 | -2.88 | 93.5d | $-1,077.16 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,852 | -4.86% | -31.38% | -27.51% | 5.86% | -4.40 | -3.44 | -5.36 | 56.5d | $-147.73 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,684 | +17.45% | +61.51% | +76.30% | 26.04% | +1.08 | +1.26 | +2.36 | 103.5d | $+65.24 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,570 | -1.04% | -73.67% | -52.31% | 1.37% | -5.06 | -5.02 | -53.60 | 5.1d | $-26.89 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,399 | -31.16% | -132.92% | -79.66% | 66.51% | -0.17 | -0.17 | -2.00 | 85.6d | $-1,133.50 |
| 8 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -53.35% | -43.24% | 22.12% | -1.11 | -1.39 | -2.41 | 77.5d | $-464.92 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,985 | +35.35% | +144.12% | +243.53% | 14.86% | +3.00 | +3.36 | +9.70 | 89.5d | $+517.59 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $1,505 | -39.16% | -149.53% | -85.00% | 77.96% | +0.16 | +0.17 | -1.92 | 95.6d | $-622.31 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
