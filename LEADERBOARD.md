# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-16 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,676 | -3.03% | -33.59% | -28.90% | 24.43% | +0.70 | +0.62 | -1.37 | 32.9d | $-405.86 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $7,426 | -40.60% | -551.49% | -99.92% | 69.24% | -2.24 | -1.98 | -7.96 | 26.9d | $-3,957.46 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,956 | +12.54% | +143.53% | +286.57% | 4.89% | +3.47 | +6.93 | +29.32 | 31.9d | $+169.79 |
| 4 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,797 | +15.19% | +214.16% | +634.35% | 10.73% | +2.92 | +2.63 | +19.97 | 25.9d | $+420.07 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,703 | -18.88% | -434.47% | -99.19% | 13.49% | -7.23 | -7.06 | -32.20 | 15.9d | $-986.15 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,079 | +21.43% | +327.32% | +1840.77% | 10.24% | +4.92 | +5.79 | +31.97 | 23.9d | $+738.07 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,872 | -8.08% | -105.85% | -66.84% | 43.59% | -1.28 | -1.04 | -2.43 | 27.9d | $-703.29 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,391 | +1.32% | +28.54% | +32.78% | 1.18% | +3.27 | +4.59 | +24.20 | 16.9d | $+35.75 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,817 | +3.51% | +40.21% | +48.47% | 2.51% | +2.65 | +2.58 | +16.01 | 31.9d | $+19.08 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,283 | +20.38% | +177.74% | +404.10% | 10.23% | +2.56 | +4.67 | +17.38 | 41.9d | $+235.73 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
