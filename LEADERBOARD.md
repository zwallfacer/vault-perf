# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-07 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,896 | +60.10% | +407.03% | +2322.41% | 24.43% | +3.40 | +3.47 | +16.66 | 53.9d | $+6,853.16 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,909 | -55.66% | -424.36% | -99.80% | 73.12% | -1.67 | -1.70 | -5.80 | 47.9d | $-4,531.78 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,173 | +6.91% | +47.66% | +58.54% | 3.02% | +2.87 | +2.88 | +15.76 | 52.9d | $+147.16 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,900 | -1.00% | -6.89% | -6.69% | 7.55% | -0.26 | -0.24 | -0.91 | 52.9d | $+112.48 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $4,168 | -3.86% | -38.20% | -32.26% | 18.67% | -0.37 | -0.49 | -2.05 | 36.9d | $-140.92 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,569 | +38.45% | +255.51% | +768.85% | 43.59% | +2.09 | +2.72 | +5.86 | 54.9d | $+1,356.18 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,542 | -4.09% | -33.27% | -28.81% | 36.90% | +0.04 | +0.04 | -0.90 | 44.9d | $-153.82 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,537 | +6.20% | +59.67% | +78.41% | 2.12% | +5.87 | +7.45 | +28.14 | 37.9d | $+193.23 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,303 | +35.55% | +206.44% | +484.93% | 10.23% | +3.20 | +4.94 | +20.18 | 62.9d | $+491.71 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,970 | +34.95% | +261.08% | +838.39% | 14.86% | +4.23 | +4.34 | +17.57 | 48.9d | $+511.74 |
| 34 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
