# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-12 11:20 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,393 | +38.17% | +238.09% | +651.38% | 24.43% | +2.41 | +2.44 | +9.75 | 58.5d | $+4,126.57 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $13,342 | -69.15% | -480.81% | -99.97% | 73.12% | -2.23 | -2.10 | -6.58 | 52.5d | $-7,114.04 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,139 | +6.24% | +39.59% | +46.83% | 5.74% | +2.28 | +2.12 | +6.90 | 57.5d | $+114.85 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,788 | -2.71% | -17.19% | -15.99% | 7.55% | -0.66 | -0.61 | -2.28 | 57.5d | $+27.91 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -75.97% | -54.82% | 19.75% | -1.09 | -1.37 | -3.85 | 41.5d | $-347.93 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,742 | -2.61% | -19.28% | -17.74% | 36.90% | +0.20 | +0.18 | -0.52 | 49.5d | $-99.45 |
| 7 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,602 | +8.10% | +69.53% | +95.14% | 2.12% | +7.03 | +8.86 | +32.79 | 42.5d | $+256.64 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,420 | +30.47% | +186.76% | +410.53% | 43.59% | +1.78 | +2.28 | +4.28 | 59.5d | $+1,152.39 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,345 | +37.94% | +205.24% | +469.72% | 10.23% | +3.26 | +4.91 | +20.07 | 67.5d | $+532.28 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,974 | +34.82% | +237.63% | +668.25% | 14.86% | +3.97 | +4.12 | +15.99 | 53.5d | $+509.79 |
| 39 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
