# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-16 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,284 | -16.20% | -93.99% | -64.14% | 50.72% | +0.09 | +0.09 | -1.85 | 62.9d | $-2,631.72 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,711 | -82.23% | -527.70% | -100.00% | 83.26% | -3.41 | -3.13 | -6.34 | 56.9d | $-12,766.34 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,937 | -0.17% | -0.99% | -0.99% | 7.55% | -0.01 | -0.01 | -0.13 | 61.9d | $+153.57 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,753 | -1.76% | -10.40% | -9.96% | 10.75% | -0.41 | -0.34 | -0.97 | 61.9d | $-272.28 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -90.18% | -61.60% | 22.12% | -1.45 | -1.81 | -4.08 | 45.9d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,575 | +7.34% | +57.08% | +73.47% | 2.43% | +5.32 | +5.97 | +23.48 | 46.9d | $+231.16 |
| 7 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,685 | -27.32% | -185.04% | -88.48% | 52.13% | -1.50 | -1.26 | -3.55 | 53.9d | $-1,008.27 |
| 8 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,650 | +4.03% | +23.00% | +25.29% | 43.59% | +0.95 | +1.18 | +0.53 | 63.9d | $+471.28 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,276 | +34.44% | +174.94% | +349.64% | 10.23% | +2.88 | +4.26 | +17.10 | 71.9d | $+472.84 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,975 | +35.06% | +221.12% | +565.62% | 14.86% | +3.83 | +3.93 | +14.88 | 57.9d | $+513.24 |
| 40 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
