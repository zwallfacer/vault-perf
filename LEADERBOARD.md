# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-18 08:29 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $15,314 | +18.42% | +195.46% | +501.39% | 24.43% | +2.20 | +2.01 | +8.00 | 34.4d | $+2,357.00 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $10,226 | -16.84% | -216.65% | -90.67% | 69.24% | +0.04 | +0.04 | -3.13 | 28.4d | $-1,035.04 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $5,805 | +36.91% | +458.69% | +4859.89% | 43.59% | +2.22 | +2.48 | +10.52 | 29.4d | $+1,195.43 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,709 | -3.37% | -36.81% | -31.23% | 5.63% | -2.06 | -1.66 | -6.54 | 33.4d | $-61.20 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,703 | +13.03% | +173.75% | +412.06% | 10.73% | +2.48 | +2.43 | +16.20 | 27.4d | $+330.41 |
| 6 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,541 | -12.43% | -261.39% | -93.87% | 13.68% | -2.17 | -2.68 | -19.11 | 17.4d | $-652.09 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $4,482 | +28.19% | +405.15% | +3448.71% | 10.24% | +6.01 | +6.88 | +39.57 | 25.4d | $+974.11 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,891 | +5.67% | +62.05% | +82.85% | 2.51% | +4.01 | +3.67 | +24.70 | 33.4d | $+85.45 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,477 | +3.41% | +67.60% | +94.40% | 1.18% | +6.50 | +10.56 | +57.33 | 18.4d | $+105.96 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,025 | +18.19% | +153.11% | +308.25% | 10.23% | +2.22 | +4.13 | +14.97 | 43.4d | $+194.89 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
