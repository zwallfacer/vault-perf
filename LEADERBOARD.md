# buoy.finance — top 11 vaults by TVL

_Generated 2026-09-28 10:10 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,318 | +46.54% | +382.01% | +2202.57% | 24.43% | +3.23 | +3.32 | +15.64 | 44.5d | $+5,166.83 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,332 | -64.55% | -612.89% | -99.99% | 73.12% | -3.31 | -3.17 | -8.38 | 38.4d | $-6,119.32 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $4,883 | +39.77% | +319.11% | +1368.13% | 43.59% | +2.40 | +3.23 | +7.32 | 45.5d | $+1,504.33 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,734 | +8.32% | +69.89% | +95.68% | 2.90% | +4.02 | +4.28 | +24.08 | 43.5d | $+207.97 |
| 5 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,716 | -4.66% | -39.09% | -32.99% | 7.55% | -1.56 | -1.42 | -5.18 | 43.5d | $-68.35 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,444 | +20.16% | +207.50% | +562.10% | 10.29% | +3.36 | +3.62 | +20.16 | 35.5d | $+738.33 |
| 7 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,294 | -17.14% | -228.04% | -91.80% | 13.68% | -2.35 | -3.05 | -16.67 | 27.4d | $-895.93 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,497 | +3.98% | +51.04% | +64.95% | 2.12% | +4.74 | +6.24 | +24.07 | 28.5d | $+125.20 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,231 | +30.20% | +206.31% | +506.68% | 10.23% | +3.11 | +5.13 | +20.17 | 53.4d | $+401.06 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,824 | +24.71% | +228.69% | +671.89% | 6.34% | +4.90 | +5.10 | +36.08 | 39.4d | $+361.74 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
