# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-29 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $16,100 | +32.74% | +157.38% | +290.17% | 57.56% | +1.77 | +1.59 | +2.73 | 75.9d | $+3,361.96 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,761 | -84.95% | -443.49% | -99.99% | 92.09% | -1.16 | -1.40 | -4.82 | 69.9d | $-13,925.37 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,189 | +5.88% | +28.63% | +32.08% | 7.55% | +1.10 | +1.11 | +3.80 | 74.9d | $+452.67 |
| 4 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,893 | +60.32% | +286.05% | +837.78% | 47.44% | +2.06 | +2.81 | +6.03 | 77.0d | $+1,921.42 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,802 | -2.01% | -9.77% | -9.40% | 13.59% | -0.29 | -0.25 | -0.72 | 74.9d | $-304.14 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,505 | +5.13% | +31.20% | +35.57% | 3.20% | +2.63 | +2.37 | +9.76 | 60.0d | $+157.52 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,984 | -0.59% | -5.67% | -5.53% | 0.97% | -1.72 | -1.56 | -5.85 | 37.9d | $-19.62 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,854 | +39.21% | +168.59% | +314.70% | 10.23% | +2.85 | +4.33 | +16.48 | 84.9d | $+534.23 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,445 | -29.61% | -161.46% | -85.26% | 56.06% | -0.73 | -0.73 | -2.88 | 66.9d | $-1,092.38 |
| 10 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -70.21% | -52.54% | 22.12% | -1.28 | -1.58 | -3.17 | 58.9d | $-464.88 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
