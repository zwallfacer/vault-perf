# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-09 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,136 | +37.48% | +244.73% | +699.22% | 24.43% | +2.46 | +2.53 | +10.02 | 55.9d | $+4,040.69 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $13,451 | -68.89% | -504.14% | -99.98% | 73.12% | -2.29 | -2.18 | -6.89 | 49.9d | $-7,000.99 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,013 | +3.60% | +23.93% | +26.50% | 5.74% | +1.42 | +1.33 | +4.17 | 54.9d | $-12.86 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,914 | -0.62% | -4.15% | -4.08% | 7.55% | -0.16 | -0.15 | -0.55 | 54.9d | $+131.04 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -81.09% | -57.17% | 19.75% | -1.13 | -1.45 | -4.11 | 38.9d | $-347.93 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,557 | +6.90% | +63.10% | +84.07% | 2.12% | +6.35 | +7.86 | +29.76 | 39.9d | $+216.61 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,411 | -6.46% | -50.28% | -40.53% | 36.90% | -0.12 | -0.11 | -1.36 | 46.9d | $-240.88 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,139 | +20.47% | +131.23% | +230.00% | 43.59% | +1.53 | +1.97 | +3.01 | 56.9d | $+894.78 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,287 | +34.47% | +193.98% | +429.49% | 10.23% | +3.07 | +4.73 | +18.96 | 64.9d | $+473.33 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,976 | +34.65% | +248.67% | +745.78% | 14.86% | +4.09 | +4.24 | +16.73 | 50.9d | $+507.37 |
| 35 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
