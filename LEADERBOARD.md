# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-16 08:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,108 | -2.28% | -13.31% | -12.60% | 50.72% | +0.71 | +0.67 | -0.26 | 62.4d | $-901.11 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,980 | -81.46% | -527.44% | -100.00% | 83.26% | -3.31 | -3.04 | -6.34 | 56.4d | $-12,436.84 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,895 | +1.18% | +7.00% | +7.21% | 10.75% | +0.46 | +0.39 | +0.65 | 61.4d | $-130.01 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,890 | -1.12% | -6.63% | -6.45% | 7.55% | -0.23 | -0.22 | -0.88 | 61.4d | $+106.71 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -91.18% | -62.00% | 22.12% | -1.45 | -1.81 | -4.12 | 45.4d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,596 | +7.98% | +62.79% | +82.96% | 2.43% | +5.87 | +6.48 | +25.83 | 46.4d | $+252.73 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,858 | +11.52% | +66.32% | +87.32% | 43.59% | +1.18 | +1.49 | +1.52 | 63.4d | $+664.39 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,528 | -31.35% | -214.30% | -92.36% | 52.13% | -1.85 | -1.57 | -4.11 | 53.4d | $-1,156.38 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,309 | +35.74% | +182.82% | +377.35% | 10.23% | +2.98 | +4.49 | +17.87 | 71.4d | $+494.94 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,973 | +34.85% | +221.74% | +570.19% | 14.86% | +3.81 | +3.91 | +14.92 | 57.4d | $+510.23 |
| 40 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
