# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-11 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $18,270 | +46.39% | +292.46% | +1005.23% | 24.43% | +2.74 | +2.77 | +11.97 | 57.9d | $+5,148.55 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $14,069 | -67.28% | -473.39% | -99.96% | 73.12% | -2.09 | -1.95 | -6.47 | 51.9d | $-6,306.52 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,113 | +5.65% | +36.26% | +42.29% | 5.74% | +2.09 | +1.96 | +6.32 | 56.9d | $+86.43 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,762 | -3.63% | -23.27% | -21.10% | 7.55% | -0.91 | -0.85 | -3.08 | 56.9d | $-17.50 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -77.12% | -55.36% | 19.75% | -1.10 | -1.37 | -3.90 | 40.9d | $-347.93 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,702 | +0.52% | +3.91% | +3.97% | 36.90% | +0.42 | +0.37 | +0.11 | 48.9d | $+15.99 |
| 7 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,604 | +8.18% | +71.28% | +98.40% | 2.12% | +7.21 | +8.86 | +33.62 | 41.9d | $+259.41 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,395 | +31.13% | +192.86% | +436.02% | 43.59% | +1.82 | +2.30 | +4.42 | 58.9d | $+1,169.59 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,319 | +36.32% | +198.30% | +442.82% | 10.23% | +3.16 | +4.80 | +19.39 | 66.9d | $+504.80 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,969 | +34.84% | +240.54% | +687.58% | 14.86% | +4.02 | +4.08 | +16.19 | 52.9d | $+510.08 |
| 35 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
