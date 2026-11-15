# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-15 00:10 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,147 | +4.07% | +16.32% | +17.35% | 7.55% | +0.68 | +0.67 | +2.16 | 91.1d | $+363.27 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,996 | -9.84% | -47.22% | -39.17% | 18.94% | -1.51 | -1.09 | -2.49 | 76.1d | $-341.00 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,920 | -22.97% | -92.09% | -64.87% | 29.83% | -3.13 | -2.45 | -3.09 | 91.0d | $-1,100.96 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,842 | -5.21% | -35.17% | -30.32% | 5.53% | -4.92 | -3.77 | -6.36 | 54.0d | $-158.08 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,579 | -0.68% | -94.55% | -61.27% | 0.81% | -16.31 | -11.31 | -116.87 | 2.6d | $-17.61 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,542 | +11.14% | +40.26% | +46.48% | 26.04% | +0.74 | +0.83 | +1.55 | 101.0d | $-79.25 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -55.14% | -44.30% | 22.12% | -1.13 | -1.42 | -2.49 | 75.0d | $-464.92 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,165 | -39.08% | -171.75% | -88.68% | 60.35% | -0.50 | -0.51 | -2.85 | 83.1d | $-1,417.27 |
| 9 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,985 | +35.71% | +149.80% | +259.98% | 14.86% | +3.07 | +3.38 | +10.08 | 87.0d | $+522.87 |
| 10 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $1,567 | -87.20% | -345.76% | -99.97% | 93.68% | -0.75 | -0.61 | -3.69 | 92.0d | $-11,359.75 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
