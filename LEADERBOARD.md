# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-27 01:00 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,296 | +6.91% | +24.47% | +26.69% | 7.55% | +1.03 | +1.00 | +3.24 | 103.1d | $+503.80 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,047 | -19.61% | -69.45% | -53.84% | 30.27% | -2.31 | -1.88 | -2.29 | 103.1d | $-973.72 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,908 | -12.67% | -52.51% | -42.97% | 30.76% | -1.18 | -0.92 | -1.71 | 88.1d | $-435.39 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,794 | -6.81% | -37.64% | -32.28% | 9.66% | -4.42 | -3.38 | -3.90 | 66.1d | $-206.22 |
| 5 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,572 | +4.64% | +14.99% | +15.78% | 43.98% | +0.36 | +0.36 | +0.34 | 113.0d | $-36.70 |
| 6 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,485 | -4.31% | -107.44% | -66.66% | 6.32% | -6.10 | -5.31 | -17.01 | 14.7d | $-112.01 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,988 | +35.80% | +131.91% | +208.80% | 14.86% | +2.87 | +3.26 | +8.88 | 99.1d | $+524.09 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,560 | -56.08% | -215.27% | -95.75% | 76.93% | -0.89 | -0.83 | -2.80 | 95.1d | $-2,026.29 |
| 9 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,358 | -9.42% | -51.65% | -41.87% | 14.33% | -3.36 | -2.93 | -3.61 | 66.6d | $-141.28 |
| 10 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,322 | -11.80% | -67.16% | -51.06% | 14.76% | -5.62 | -4.62 | -4.55 | 64.1d | $-176.88 |
| 56 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
