# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-13 13:38 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` † | $13,380 | +5.64% | +69.49% | +96.61% | 21.13% | +1.06 | +0.95 | +3.29 | 29.6d |
| 2 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,949 | -14.58% | -423.32% | -98.97% | 9.05% | -5.43 | -5.79 | -46.77 | 12.6d |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` † | $4,937 | +12.54% | +159.93% | +351.19% | 4.89% | +3.67 | +7.10 | +32.67 | 28.6d |
| 4 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $4,785 | -37.76% | -584.23% | -99.93% | 52.81% | -4.79 | -3.39 | -11.06 | 23.6d |
| 5 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,671 | +12.12% | +195.80% | +534.81% | 10.73% | +2.62 | +2.51 | +18.25 | 22.6d |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,847 | -12.39% | -183.91% | -85.96% | 35.61% | -3.17 | -2.31 | -5.16 | 24.6d |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $3,724 | +6.80% | +120.40% | +220.55% | 10.11% | +2.96 | +2.39 | +11.90 | 20.6d |
| 8 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,405 | +1.26% | +33.69% | +39.76% | 0.84% | +4.06 | +8.00 | +39.94 | 13.6d |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` † | $2,870 | +5.32% | +67.93% | +93.83% | 1.80% | +4.46 | +4.16 | +37.77 | 28.6d |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,271 | +18.04% | +170.71% | +380.41% | 10.23% | +2.37 | +4.53 | +16.69 | 38.6d |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
