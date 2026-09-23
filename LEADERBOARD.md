# buoy.finance — top 10 vaults by TVL

_Generated 2026-09-23 08:50 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $20,444 | +66.63% | +617.11% | +11219.33% | 24.43% | +4.37 | +4.29 | +25.26 | 39.4d | $+7,653.80 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $8,043 | -39.50% | -431.78% | -99.59% | 69.24% | -1.27 | -1.21 | -6.24 | 33.4d | $-3,541.53 |
| 3 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $5,338 | +49.68% | +448.45% | +3712.02% | 43.59% | +2.89 | +3.58 | +10.29 | 40.4d | $+1,849.89 |
| 4 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` † | $4,850 | -6.84% | -111.51% | -68.50% | 13.68% | +0.13 | +0.20 | -8.15 | 22.4d | $-362.09 |
| 5 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $4,764 | +36.57% | +438.86% | +4110.84% | 10.24% | +6.92 | +7.23 | +42.86 | 30.4d | $+1,266.54 |
| 6 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,659 | -5.06% | -48.10% | -38.96% | 6.64% | -2.19 | -1.90 | -7.25 | 38.4d | $-88.49 |
| 7 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $4,116 | -0.38% | -4.23% | -4.15% | 14.68% | +0.33 | +0.29 | -0.29 | 32.4d | $-228.43 |
| 8 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $3,997 | +7.63% | +72.48% | +101.08% | 2.90% | +4.03 | +4.43 | +24.97 | 38.4d | $+182.94 |
| 9 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` † | $3,540 | +5.35% | +83.40% | +125.35% | 1.18% | +8.06 | +12.89 | +70.73 | 23.4d | $+171.28 |
| 10 | `0x6e8075CF5f840067a3d82453677Db2C0D88dB51e` † | $2,502 | +0.01% | +1.18% | +1.19% | 0.02% | +5.73 | +14.06 | +51.40 | 1.9d | $+0.08 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
