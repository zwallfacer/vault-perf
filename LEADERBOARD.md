# buoy.finance — top 11 vaults by TVL

_Generated 2026-11-03 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $13,054 | +6.06% | +27.34% | +30.41% | 57.56% | +1.08 | +0.95 | +0.48 | 80.9d | $+87.36 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,344 | +8.07% | +36.84% | +42.51% | 7.55% | +1.41 | +1.40 | +4.88 | 79.9d | $+560.92 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $4,044 | -90.52% | -441.01% | -100.00% | 92.52% | -1.63 | -1.92 | -4.77 | 74.9d | $-16,298.51 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,682 | -5.25% | -23.98% | -21.83% | 17.18% | -0.77 | -0.64 | -1.40 | 79.9d | $-430.31 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,515 | +5.44% | +30.54% | +34.64% | 4.68% | +2.23 | +1.99 | +6.52 | 65.0d | $+167.83 |
| 6 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,300 | +27.90% | +124.26% | +199.22% | 47.44% | +1.46 | +1.83 | +2.62 | 82.0d | $+1,086.42 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,175 | -14.33% | -72.71% | -54.38% | 60.35% | +0.20 | +0.23 | -1.20 | 71.9d | $-530.35 |
| 8 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,972 | -0.87% | -7.40% | -7.16% | 1.43% | -2.01 | -1.72 | -5.17 | 42.9d | $-28.06 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,909 | +42.31% | +171.78% | +318.94% | 10.23% | +2.89 | +4.52 | +16.79 | 89.9d | $+597.46 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -64.72% | -49.69% | 22.12% | -1.23 | -1.53 | -2.93 | 63.9d | $-464.89 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
