# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-28 01:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,242 | +5.83% | +20.44% | +21.97% | 7.55% | +0.87 | +0.84 | +2.71 | 104.1d | $+450.20 |
| 2 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $4,881 | -3.53% | -82.34% | -56.76% | 6.32% | -4.63 | -3.82 | -13.04 | 15.7d | $-91.67 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,087 | -18.54% | -65.03% | -51.29% | 30.27% | -2.14 | -1.73 | -2.15 | 104.1d | $-933.19 |
| 4 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,909 | -12.74% | -52.18% | -42.77% | 30.76% | -1.18 | -0.93 | -1.70 | 89.1d | $-437.44 |
| 5 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,781 | -7.28% | -39.65% | -33.74% | 9.66% | -4.69 | -3.59 | -4.10 | 67.1d | $-220.39 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,574 | +4.45% | +14.24% | +14.95% | 43.98% | +0.35 | +0.35 | +0.32 | 114.0d | $-41.45 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,992 | +35.75% | +130.43% | +204.98% | 14.86% | +2.85 | +3.22 | +8.78 | 100.1d | $+523.45 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,867 | -48.03% | -182.45% | -91.68% | 76.93% | -0.47 | -0.45 | -2.37 | 96.1d | $-1,737.83 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,365 | -9.05% | -48.90% | -40.10% | 14.33% | -3.18 | -2.75 | -3.41 | 67.6d | $-135.77 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,309 | -12.74% | -71.42% | -53.42% | 14.76% | -6.00 | -4.93 | -4.84 | 65.1d | $-191.03 |
| 57 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
