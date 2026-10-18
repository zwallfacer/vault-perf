# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-18 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $8,677 | -27.72% | -155.90% | -83.89% | 57.56% | -0.48 | -0.44 | -2.71 | 64.9d | $-4,057.82 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $6,577 | -84.73% | -525.28% | -100.00% | 87.42% | -3.43 | -3.11 | -6.01 | 58.9d | $-13,847.35 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $5,088 | +2.91% | +16.61% | +17.79% | 7.55% | +0.65 | +0.62 | +2.20 | 63.9d | $+305.70 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,578 | -5.37% | -30.68% | -27.05% | 13.59% | -1.39 | -1.13 | -2.26 | 63.9d | $-446.76 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -86.42% | -60.03% | 22.12% | -1.42 | -1.79 | -3.91 | 47.9d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,529 | +6.02% | +44.93% | +54.70% | 2.43% | +4.10 | +4.52 | +18.48 | 48.9d | $+187.34 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,347 | -7.54% | -41.72% | -35.20% | 44.13% | +0.55 | +0.68 | -0.95 | 65.9d | $+173.39 |
| 8 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,201 | +30.22% | +149.34% | +268.73% | 10.23% | +2.50 | +3.71 | +14.60 | 73.9d | $+401.16 |
| 9 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,184 | -37.58% | -245.40% | -95.39% | 55.42% | -2.18 | -1.82 | -4.43 | 55.9d | $-1,385.56 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,982 | +34.87% | +212.60% | +519.55% | 14.86% | +3.73 | +3.87 | +14.31 | 59.9d | $+510.51 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
