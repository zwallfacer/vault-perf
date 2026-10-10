# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-10 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $17,768 | +42.99% | +275.80% | +891.67% | 24.43% | +2.65 | +2.70 | +11.29 | 56.9d | $+4,726.18 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $13,515 | -68.76% | -493.32% | -99.98% | 73.12% | -2.25 | -2.12 | -6.75 | 50.9d | $-6,946.26 |
| 3 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $5,041 | +4.18% | +27.32% | +30.69% | 5.74% | +1.62 | +1.51 | +4.76 | 55.9d | $+15.44 |
| 4 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,839 | -2.20% | -14.36% | -13.51% | 7.55% | -0.56 | -0.52 | -1.90 | 55.9d | $+53.16 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,961 | -8.63% | -79.05% | -56.25% | 19.75% | -1.11 | -1.41 | -4.00 | 39.9d | $-347.93 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,590 | +7.80% | +69.63% | +95.52% | 2.12% | +6.96 | +8.67 | +32.84 | 40.9d | $+246.77 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $3,549 | -3.17% | -24.15% | -21.76% | 36.90% | +0.14 | +0.12 | -0.65 | 47.9d | $-119.83 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $3,282 | +26.61% | +167.65% | +342.18% | 43.59% | +1.70 | +2.17 | +3.85 | 57.9d | $+1,052.94 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,308 | +36.02% | +199.63% | +450.12% | 10.23% | +3.16 | +4.84 | +19.52 | 65.9d | $+499.66 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,970 | +34.41% | +242.15% | +701.30% | 14.86% | +4.00 | +4.25 | +16.29 | 51.9d | $+503.77 |
| 35 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
