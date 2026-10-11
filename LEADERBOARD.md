# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-11 10:19 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,675 | +42.32% | +268.79% | +840.67% | 24.43% | +2.60 | +2.68 | +11.00 | 57.5d | $+4,642.91 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $13,596 | -68.51% | -486.05% | -99.97% | 73.12% | -2.21 | -2.06 | -6.65 | 51.4d | $-6,839.84 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,057 | +4.52% | +29.19% | +33.04% | 5.74% | +1.72 | +1.59 | +5.09 | 56.5d | $+31.52 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,793 | -3.08% | -19.89% | -18.29% | 7.55% | -0.78 | -0.73 | -2.64 | 56.5d | $+9.72 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -77.93% | -55.73% | 19.75% | -1.10 | -1.40 | -3.95 | 40.4d | $-347.93 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,586 | +7.64% | +67.26% | +91.19% | 2.12% | +6.74 | +8.56 | +31.72 | 41.5d | $+241.43 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,438 | -6.24% | -46.98% | -38.44% | 36.90% | -0.10 | -0.09 | -1.27 | 48.5d | $-232.75 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,250 | +26.45% | +165.04% | +332.45% | 43.59% | +1.68 | +2.17 | +3.79 | 58.5d | $+1,048.95 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,301 | +35.64% | +195.81% | +433.79% | 10.23% | +3.11 | +4.72 | +19.14 | 66.4d | $+493.21 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,974 | +34.64% | +241.11% | +692.67% | 14.86% | +3.99 | +4.19 | +16.22 | 52.4d | $+507.17 |
| 35 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
