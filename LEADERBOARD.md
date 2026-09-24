# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-24 08:45 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $19,736 | +59.66% | +538.96% | +6749.23% | 24.43% | +4.01 | +4.02 | +22.06 | 40.4d | $+6,799.26 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,588 | -45.30% | -480.84% | -99.83% | 69.24% | -1.64 | -1.57 | -6.94 | 34.4d | $-4,090.57 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +437.66% | +3392.35% | 43.59% | +2.86 | +3.62 | +10.04 | 41.4d | $+1,849.89 |
| 4 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,815 | +39.39% | +457.76% | +4644.19% | 10.24% | +7.22 | +7.47 | +44.71 | 31.4d | $+1,365.18 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,784 | -8.61% | -134.44% | -75.48% | 13.68% | -0.35 | -0.53 | -9.83 | 23.4d | $-453.96 |
| 6 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,768 | -3.04% | -28.11% | -24.83% | 6.64% | -1.20 | -1.14 | -4.24 | 39.4d | $+11.77 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,429 | +10.06% | +110.02% | +185.26% | 14.68% | +1.68 | +1.53 | +7.49 | 33.4d | $+206.66 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,974 | +7.02% | +65.09% | +87.58% | 2.90% | +3.66 | +4.10 | +22.43 | 39.4d | $+160.65 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,501 | +3.74% | +55.94% | +73.19% | 1.65% | +4.96 | +6.60 | +33.81 | 24.4d | $+117.16 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,255 | +29.35% | +217.00% | +570.44% | 10.23% | +3.20 | +5.39 | +21.22 | 49.4d | $+386.52 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
