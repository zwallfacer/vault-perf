# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-22 11:59 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,274 | +6.53% | +24.18% | +26.40% | 7.55% | +1.01 | +0.98 | +3.21 | 98.5d | $+484.96 |
| 2 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,083 | -18.64% | -69.07% | -53.44% | 30.27% | -2.23 | -1.78 | -2.28 | 98.5d | $-937.07 |
| 3 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $2,917 | -12.99% | -56.76% | -45.56% | 30.76% | -1.26 | -1.00 | -1.85 | 83.6d | $-446.03 |
| 4 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,799 | -6.57% | -39.01% | -33.20% | 9.66% | -4.55 | -3.57 | -4.04 | 61.5d | $-199.10 |
| 5 | `0x1af42a9937C2E0D0446e3Ea9659725Eff909A14E` † | $2,469 | -4.94% | -178.50% | -83.97% | 6.02% | -10.41 | -8.41 | -29.67 | 10.1d | $-128.40 |
| 6 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,420 | -1.60% | -5.37% | -5.27% | 43.98% | +0.02 | +0.02 | -0.12 | 108.5d | $-190.22 |
| 7 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,995 | +36.18% | +139.71% | +229.54% | 14.86% | +2.99 | +3.30 | +9.40 | 94.5d | $+529.66 |
| 8 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` | $1,354 | -9.64% | -56.73% | -44.93% | 14.23% | -3.87 | -3.48 | -3.99 | 62.0d | $-144.59 |
| 9 | `0xBB36f71abfe80eD10c44e37C69ec8D3359DDD920` | $1,326 | -11.61% | -71.17% | -53.07% | 14.76% | -6.03 | -5.00 | -4.82 | 59.6d | $-174.15 |
| 10 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $1,319 | -63.69% | -256.75% | -98.32% | 75.60% | -1.38 | -1.28 | -3.40 | 90.5d | $-2,298.90 |
| 45 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
