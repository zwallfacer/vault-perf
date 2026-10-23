# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-23 08:50 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,516 | -14.10% | -74.13% | -55.02% | 57.56% | +0.42 | +0.37 | -1.29 | 69.4d | $-2,387.13 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,552 | -82.10% | -472.73% | -100.00% | 92.09% | -1.05 | -1.34 | -5.13 | 63.4d | $-12,708.36 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,036 | +1.82% | +9.69% | +10.08% | 7.55% | +0.40 | +0.39 | +1.28 | 68.4d | $+251.72 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,869 | -0.48% | -2.57% | -2.54% | 13.59% | +0.02 | +0.01 | -0.19 | 68.4d | $-244.91 |
| 5 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,577 | +7.43% | +50.76% | +63.18% | 2.43% | +4.53 | +4.65 | +20.88 | 53.4d | $+234.28 |
| 6 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,241 | -11.74% | -70.92% | -52.97% | 55.42% | +0.09 | +0.09 | -1.28 | 60.4d | $-435.03 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,993 | -0.22% | -2.50% | -2.48% | 0.97% | -0.70 | -0.61 | -2.59 | 31.4d | $-8.11 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,927 | +43.30% | +201.66% | +434.16% | 10.23% | +3.24 | +4.78 | +19.71 | 78.4d | $+617.66 |
| 9 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,587 | +0.84% | +4.36% | +4.43% | 44.13% | +0.83 | +0.97 | +0.10 | 70.4d | $+389.19 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -78.97% | -56.75% | 22.12% | -1.35 | -1.67 | -3.57 | 52.4d | $-464.90 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
