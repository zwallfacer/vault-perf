# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-02 11:41 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,612 | +11.07% | +50.79% | +61.89% | 57.56% | +1.20 | +1.07 | +0.88 | 79.5d | $+701.55 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,607 | -86.85% | -431.25% | -100.00% | 92.09% | -1.23 | -1.45 | -4.68 | 73.5d | $-14,734.55 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,325 | +7.69% | +35.75% | +41.12% | 7.55% | +1.35 | +1.35 | +4.74 | 78.5d | $+542.36 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,663 | -5.79% | -26.89% | -24.20% | 13.87% | -0.99 | -0.82 | -1.94 | 78.5d | $-451.08 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,517 | +5.60% | +32.15% | +36.73% | 4.68% | +2.36 | +2.15 | +6.87 | 63.5d | $+173.25 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,267 | +26.81% | +121.49% | +193.38% | 47.44% | +1.45 | +1.85 | +2.56 | 80.6d | $+1,058.26 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,972 | -0.88% | -7.73% | -7.47% | 1.37% | -2.18 | -1.86 | -5.65 | 41.5d | $-28.33 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,830 | +38.70% | +159.63% | +285.50% | 10.23% | +2.72 | +4.18 | +15.61 | 88.5d | $+523.71 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,681 | -27.21% | -140.81% | -80.67% | 60.35% | -0.39 | -0.43 | -2.33 | 70.5d | $-1,004.04 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -66.18% | -50.46% | 22.12% | -1.24 | -1.55 | -2.99 | 62.5d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
