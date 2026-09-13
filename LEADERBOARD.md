# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-13 13:55 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` † | $13,619 | +7.32% | +90.25% | +138.93% | 21.13% | +1.20 | +1.08 | +4.27 | 29.6d | $+740.49 |
| 2 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,982 | -14.14% | -409.97% | -98.80% | 9.05% | -5.10 | -5.47 | -45.30 | 12.6d | $-711.17 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` † | $4,929 | +12.53% | +159.82% | +350.72% | 4.89% | +3.67 | +7.10 | +32.65 | 28.6d | $+169.36 |
| 4 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $4,870 | -37.37% | -577.93% | -99.93% | 52.52% | -4.75 | -3.37 | -11.00 | 23.6d | $-3,442.64 |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,682 | +12.34% | +199.25% | +554.59% | 10.73% | +2.66 | +2.36 | +18.58 | 22.6d | $+301.62 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,876 | -9.62% | -142.76% | -77.71% | 35.61% | -2.84 | -2.11 | -4.01 | 24.6d | $-783.44 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $3,749 | +7.00% | +123.91% | +231.23% | 9.94% | +3.09 | +2.52 | +12.46 | 20.6d | $+234.23 |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,403 | +1.31% | +35.05% | +41.66% | 0.84% | +4.25 | +8.51 | +41.56 | 13.6d | $+35.33 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` † | $2,869 | +5.32% | +67.86% | +93.70% | 1.80% | +4.46 | +4.16 | +37.73 | 28.6d | $+69.59 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,276 | +18.30% | +173.14% | +390.35% | 10.23% | +2.40 | +4.46 | +16.93 | 38.6d | $+195.24 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
