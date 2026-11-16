# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-16 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,220 | +5.56% | +21.83% | +23.67% | 7.55% | +0.90 | +0.87 | +2.89 | 92.9d | $+436.79 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,146 | -5.02% | -23.51% | -21.43% | 18.94% | -0.53 | -0.46 | -1.24 | 78.0d | $-180.44 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,977 | -21.45% | -84.24% | -61.25% | 30.27% | -2.81 | -2.23 | -2.78 | 92.9d | $-1,043.30 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,852 | -4.76% | -31.08% | -27.27% | 5.86% | -4.34 | -3.38 | -5.31 | 55.9d | $-144.75 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,663 | +16.78% | +59.53% | +73.38% | 26.04% | +1.05 | +1.23 | +2.29 | 102.9d | $+50.02 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,569 | -1.07% | -86.29% | -58.00% | 1.26% | -5.78 | -6.54 | -68.52 | 4.5d | $-27.67 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -53.79% | -43.50% | 22.12% | -1.12 | -1.40 | -2.43 | 76.9d | $-464.92 |
| 8 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,982 | +35.26% | +144.77% | +245.57% | 14.86% | +3.01 | +3.34 | +9.74 | 88.9d | $+516.27 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,958 | -45.02% | -193.47% | -92.35% | 66.51% | -0.76 | -0.77 | -2.91 | 84.9d | $-1,630.18 |
| 10 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $1,462 | -40.65% | -156.24% | -86.54% | 77.96% | +0.08 | +0.09 | -2.00 | 95.0d | $-659.47 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
