# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-30 21:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $14,095 | +14.36% | +68.14% | +89.02% | 57.56% | +1.31 | +1.16 | +1.18 | 76.9d | $+1,106.08 |
| 2 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,305 | +7.27% | +34.94% | +40.11% | 7.55% | +1.31 | +1.34 | +4.63 | 75.9d | $+521.43 |
| 3 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $4,723 | -88.91% | -457.63% | -100.00% | 92.09% | -1.51 | -1.78 | -4.97 | 70.9d | $-15,614.78 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,753 | -3.47% | -16.69% | -15.62% | 13.59% | -0.57 | -0.46 | -1.23 | 75.9d | $-361.17 |
| 5 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,697 | +43.62% | +204.20% | +444.50% | 47.44% | +1.81 | +2.25 | +4.30 | 78.0d | $+1,491.23 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,513 | +5.69% | +34.08% | +39.30% | 4.68% | +2.54 | +2.17 | +7.28 | 61.0d | $+176.37 |
| 7 | `0x754eaF74Dee8DAF61E75FE778007202f8Fd8F9F6` | $2,964 | -1.10% | -10.28% | -9.82% | 1.37% | -2.85 | -2.44 | -7.51 | 38.9d | $-34.82 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,743 | +34.60% | +147.01% | +253.44% | 10.23% | +2.52 | +3.87 | +14.37 | 85.9d | $+439.92 |
| 9 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $2,322 | -11.33% | -69.04% | -51.94% | 22.12% | -1.27 | -1.57 | -3.12 | 59.9d | $-464.88 |
| 10 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,017 | -45.02% | -241.89% | -95.98% | 60.35% | -1.50 | -1.41 | -4.01 | 67.9d | $-1,659.27 |
| 42 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
