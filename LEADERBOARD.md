# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-30 10:27 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $14,995 | +23.79% | +113.55% | +176.94% | 57.56% | +1.55 | +1.38 | +1.97 | 76.5d | $+2,263.30 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,305 | +7.27% | +35.15% | +40.40% | 7.55% | +1.31 | +1.34 | +4.66 | 75.5d | $+521.43 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $5,301 | -87.39% | -452.75% | -100.00% | 92.09% | -1.37 | -1.64 | -4.92 | 70.5d | $-14,967.40 |
| 4 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,880 | +53.19% | +250.50% | +645.32% | 47.44% | +1.99 | +2.47 | +5.28 | 77.5d | $+1,737.84 |
| 5 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,806 | -2.18% | -10.55% | -10.12% | 13.59% | -0.30 | -0.25 | -0.78 | 75.5d | $-310.99 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,494 | +5.04% | +30.38% | +34.50% | 4.68% | +2.31 | +1.92 | +6.49 | 60.5d | $+154.51 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,969 | -0.97% | -9.21% | -8.84% | 1.37% | -2.55 | -2.20 | -6.73 | 38.5d | $-31.06 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,735 | +34.25% | +146.34% | +251.98% | 10.23% | +2.50 | +3.82 | +14.31 | 85.4d | $+432.89 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -69.58% | -52.21% | 22.12% | -1.27 | -1.55 | -3.15 | 59.4d | $-464.88 |
| 10 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,151 | -40.32% | -218.10% | -93.87% | 60.35% | -1.29 | -1.25 | -3.61 | 67.5d | $-1,486.30 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
