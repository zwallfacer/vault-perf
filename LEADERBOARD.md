# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-05 10:51 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $20,699 | +66.25% | +469.60% | +3571.30% | 24.43% | +3.71 | +3.87 | +19.22 | 51.5d | $+7,617.40 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,495 | -57.96% | -465.26% | -99.90% | 73.12% | -2.06 | -2.05 | -6.36 | 45.5d | $-4,942.81 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,181 | +7.06% | +51.06% | +63.78% | 3.02% | +3.00 | +2.99 | +16.88 | 50.5d | $+154.71 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,713 | -4.72% | -34.09% | -29.47% | 7.55% | -1.39 | -1.26 | -4.52 | 50.5d | $-71.36 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $4,281 | -1.29% | -13.70% | -12.88% | 18.67% | +0.05 | +0.08 | -0.73 | 34.5d | $-29.80 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,926 | +57.86% | +402.09% | +2287.08% | 43.59% | +2.67 | +3.50 | +9.22 | 52.5d | $+1,842.46 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,850 | +4.76% | +40.90% | +49.12% | 36.90% | +0.74 | +0.60 | +1.11 | 42.5d | $+171.88 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,525 | +5.81% | +59.77% | +78.78% | 2.12% | +5.66 | +7.38 | +28.19 | 35.5d | $+180.48 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,270 | +33.75% | +203.78% | +478.82% | 10.23% | +3.13 | +4.86 | +19.92 | 60.5d | $+461.15 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,805 | +22.79% | +179.05% | +401.78% | 14.86% | +2.76 | +2.66 | +12.05 | 46.5d | $+333.71 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
