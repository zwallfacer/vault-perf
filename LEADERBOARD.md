# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-14 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,175 | +4.59% | +18.44% | +19.76% | 7.55% | +0.76 | +0.75 | +2.44 | 90.9d | $+389.13 |
| 2 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,958 | -10.71% | -51.48% | -41.99% | 17.78% | -1.88 | -1.36 | -2.90 | 76.0d | $-370.03 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,930 | -22.70% | -91.11% | -64.42% | 29.83% | -3.10 | -2.42 | -3.05 | 90.9d | $-1,090.63 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,845 | -5.02% | -34.01% | -29.46% | 5.26% | -5.08 | -3.95 | -6.47 | 53.9d | $-152.62 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,576 | -0.81% | -117.81% | -69.36% | 0.81% | -31.94 | -17.60 | -145.63 | 2.5d | $-21.01 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,494 | +9.78% | +35.39% | +40.17% | 25.33% | +0.66 | +0.76 | +1.40 | 100.9d | $-110.37 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,287 | -11.33% | -55.22% | -44.35% | 22.12% | -1.14 | -1.43 | -2.50 | 74.9d | $-464.92 |
| 8 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,985 | +35.52% | +149.17% | +258.39% | 14.86% | +3.08 | +3.40 | +10.04 | 86.9d | $+519.99 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,902 | -43.81% | -192.80% | -92.09% | 60.35% | -0.72 | -0.73 | -3.20 | 82.9d | $-1,586.74 |
| 10 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,354 | -9.68% | -64.92% | -49.48% | 10.89% | -4.83 | -4.29 | -5.96 | 54.4d | $-145.17 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
