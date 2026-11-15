# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-15 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,212 | +4.83% | +19.16% | +20.58% | 7.55% | +0.79 | +0.77 | +2.54 | 91.9d | $+400.60 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,179 | -5.17% | -24.53% | -22.26% | 18.94% | -0.59 | -0.49 | -1.29 | 77.0d | $-185.44 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,902 | -23.43% | -93.05% | -65.36% | 30.11% | -3.20 | -2.51 | -3.09 | 91.9d | $-1,118.60 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,853 | -4.88% | -32.44% | -28.29% | 5.86% | -4.53 | -3.53 | -5.54 | 54.9d | $-148.31 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,667 | +15.97% | +57.19% | +69.99% | 26.04% | +1.01 | +1.17 | +2.20 | 101.9d | $+31.30 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,588 | -0.34% | -35.06% | -29.62% | 0.81% | -4.75 | -5.58 | -43.34 | 3.5d | $-8.75 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -54.49% | -43.92% | 22.12% | -1.13 | -1.42 | -2.46 | 75.9d | $-464.92 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,135 | -41.27% | -179.44% | -90.11% | 60.35% | -0.61 | -0.61 | -2.97 | 83.9d | $-1,495.57 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,984 | +35.83% | +148.77% | +256.63% | 14.86% | +3.09 | +3.39 | +10.01 | 87.9d | $+524.59 |
| 10 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $1,759 | -85.72% | -336.64% | -99.95% | 93.68% | -0.56 | -0.46 | -3.59 | 92.9d | $-11,178.09 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
