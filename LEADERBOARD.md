# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-12 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $15,749 | +26.70% | +165.46% | +333.42% | 24.82% | +1.95 | +1.90 | +6.67 | 58.9d | $+2,700.64 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $12,916 | -70.11% | -484.00% | -99.98% | 73.12% | -2.31 | -2.17 | -6.62 | 52.9d | $-7,531.11 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,031 | +3.99% | +25.15% | +27.97% | 5.74% | +1.49 | +1.38 | +4.38 | 57.9d | $+6.00 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,892 | -1.08% | -6.82% | -6.63% | 7.55% | -0.24 | -0.23 | -0.90 | 57.9d | $+108.40 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -75.27% | -54.49% | 19.75% | -1.09 | -1.37 | -3.81 | 41.9d | $-347.93 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,584 | +7.59% | +64.57% | +86.33% | 2.12% | +6.44 | +7.81 | +30.45 | 42.9d | $+239.63 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,578 | -2.82% | -20.60% | -18.85% | 36.90% | +0.18 | +0.16 | -0.56 | 49.9d | $-106.82 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,091 | +20.00% | +121.82% | +203.59% | 43.59% | +1.48 | +1.86 | +2.79 | 59.9d | $+882.75 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,330 | +37.18% | +200.00% | +447.68% | 10.23% | +3.20 | +4.82 | +19.55 | 67.9d | $+519.41 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,973 | +34.83% | +235.98% | +657.46% | 14.86% | +3.97 | +4.12 | +15.88 | 53.9d | $+509.88 |
| 39 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
