# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-24 08:24 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $9,500 | -22.40% | -116.14% | -73.15% | 57.56% | +0.04 | +0.03 | -2.02 | 70.4d | $-3,406.09 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,305 | -82.86% | -469.87% | -100.00% | 92.09% | -1.19 | -1.48 | -5.10 | 64.4d | $-13,035.39 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,074 | +2.55% | +13.42% | +14.16% | 7.55% | +0.54 | +0.53 | +1.78 | 69.4d | $+288.04 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,747 | -3.57% | -18.79% | -17.41% | 13.59% | -0.67 | -0.56 | -1.38 | 69.4d | $-365.02 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,539 | +6.30% | +42.29% | +50.70% | 2.43% | +3.83 | +4.05 | +17.40 | 54.4d | $+196.76 |
| 6 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,988 | -0.36% | -4.09% | -4.01% | 0.97% | -1.22 | -1.11 | -4.22 | 32.4d | $-12.52 |
| 7 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,832 | +38.67% | +177.85% | +349.81% | 10.23% | +2.92 | +4.39 | +17.39 | 79.4d | $+523.03 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,658 | -27.36% | -162.65% | -85.05% | 55.42% | -0.68 | -0.67 | -2.94 | 61.4d | $-1,009.51 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,329 | -9.25% | -47.27% | -39.11% | 45.16% | +0.49 | +0.58 | -1.05 | 71.4d | $+129.22 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -77.52% | -56.08% | 22.12% | -1.34 | -1.68 | -3.50 | 53.4d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
