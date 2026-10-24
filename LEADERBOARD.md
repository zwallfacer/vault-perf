# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-24 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,678 | -21.45% | -110.46% | -71.16% | 57.56% | +0.08 | +0.07 | -1.92 | 70.9d | $-3,290.36 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,325 | -82.85% | -466.15% | -100.00% | 92.09% | -1.19 | -1.48 | -5.06 | 64.9d | $-13,030.35 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,089 | +2.88% | +15.04% | +15.98% | 7.55% | +0.60 | +0.59 | +1.99 | 69.9d | $+304.36 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,767 | -3.10% | -16.17% | -15.15% | 13.59% | -0.56 | -0.47 | -1.19 | 69.9d | $-346.55 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,538 | +6.18% | +41.09% | +48.99% | 2.72% | +3.75 | +3.95 | +15.10 | 54.9d | $+192.70 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,987 | -0.40% | -4.45% | -4.36% | 0.97% | -1.35 | -1.23 | -4.59 | 32.9d | $-13.67 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,852 | -22.65% | -133.55% | -78.00% | 55.42% | -0.44 | -0.44 | -2.41 | 61.9d | $-836.28 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,836 | +38.67% | +176.73% | +345.56% | 10.23% | +2.92 | +4.39 | +17.28 | 79.9d | $+523.04 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,354 | -9.05% | -45.95% | -38.23% | 47.44% | +0.50 | +0.59 | -0.97 | 71.9d | $+134.25 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -76.79% | -55.74% | 22.12% | -1.34 | -1.68 | -3.47 | 53.9d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
