# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-15 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $12,263 | -3.56% | -40.79% | -33.99% | 24.37% | +0.66 | +0.59 | -1.67 | 31.9d | $-518.04 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,921 | +12.91% | +152.49% | +319.64% | 4.89% | +3.63 | +7.08 | +31.15 | 30.9d | $+185.84 |
| 3 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,861 | -17.42% | -427.80% | -99.09% | 11.93% | -6.55 | -6.46 | -35.87 | 14.9d | $-901.35 |
| 4 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** † | $4,646 | +11.40% | +167.28% | +387.51% | 10.73% | +2.39 | +2.18 | +15.60 | 24.9d | $+262.44 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` † | $3,871 | +9.36% | +149.17% | +316.17% | 10.24% | +2.76 | +2.43 | +14.57 | 22.9d | $+316.52 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` ✂ | $3,637 | -17.04% | -231.36% | -92.08% | 43.59% | -2.35 | -1.86 | -5.31 | 26.9d | $-1,081.02 |
| 7 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,411 | +1.00% | +22.96% | +25.67% | 1.05% | +2.58 | +3.76 | +21.97 | 15.9d | $+24.95 |
| 8 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` † | $3,265 | -58.87% | -830.51% | -100.00% | 69.24% | -5.69 | -4.00 | -11.99 | 25.9d | $-5,097.48 |
| 9 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $2,823 | +3.63% | +42.87% | +52.37% | 2.37% | +2.85 | +2.70 | +18.11 | 30.9d | $+23.52 |
| 10 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,186 | +19.04% | +170.08% | +374.41% | 10.23% | +2.42 | +4.47 | +16.63 | 40.9d | $+212.22 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
