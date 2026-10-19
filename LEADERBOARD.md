# buoy.finance — top 11 vaults by TVL

_Generated 2026-10-19 20:30 UTC. Time-weighted, net of fees and funding._

Ranked by TVL. Vaults are identified by address only.

| # | Address | TVL | TWR | APR | APY | Max DD | Sharpe | Sortino | Calmar | Window | Net P&L |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `0x8d76B763Ce5D6815a8C6F26BF1A595E39eba62Dd` | $10,862 | -11.87% | -65.74% | -50.33% | 57.56% | +0.33 | +0.30 | -1.14 | 65.9d | $-2,113.44 |
| 2 | `0x5616C9f81163AbE21eE986248AB95F37840CB02a` | $7,889 | -81.48% | -496.72% | -100.00% | 87.42% | -2.79 | -2.59 | -5.68 | 59.9d | $-12,445.77 |
| 3 | `0x3C8535595a962B8578647BDF7Ce4C7320af91b14` | $4,996 | +1.15% | +6.49% | +6.66% | 7.55% | +0.27 | +0.26 | +0.86 | 64.9d | $+218.94 |
| 4 | `0xad9EC77a455F25860F050DABFDb9FcFE547e1689` | $4,646 | -3.96% | -22.28% | -20.33% | 13.59% | -1.01 | -0.84 | -1.64 | 64.9d | $-378.57 |
| 5 | `0x11a000f5cbbB9E97f18a03da189E88AA4c849aD9` | $3,844 | -11.33% | -84.65% | -59.28% | 22.12% | -1.41 | -1.75 | -3.83 | 48.9d | $-464.89 |
| 6 | `0xE18544A0DB06301f75bde5ea8b4EAAFf134726a8` | $3,565 | +7.05% | +51.58% | +64.62% | 2.43% | +4.88 | +5.53 | +21.22 | 49.9d | $+221.75 |
| 7 | `0xD2D28B042a99eD1e8Be3e3F5197Cc3327Dd03248` | $2,529 | -1.15% | -6.26% | -6.10% | 44.13% | +0.76 | +0.95 | -0.14 | 66.9d | $+337.96 |
| 8 | `0x3Bc0dc0F79421388aA10A9fDE393F73cE92B1dDE` | $2,513 | -31.38% | -201.30% | -91.07% | 55.42% | -1.74 | -1.48 | -3.63 | 56.9d | $-1,157.46 |
| 9 | `0x38C820BC1776d759527050ad0bfb953eF2B39AA0` ✂ | $2,313 | +36.04% | +175.73% | +348.50% | 10.23% | +2.91 | +4.39 | +17.18 | 74.9d | $+500.02 |
| 10 | `0x87F76a7e6C346904192c884d48C02D3AC640DE1E` | $1,974 | +35.04% | +210.11% | +505.76% | 14.86% | +3.72 | +3.92 | +14.14 | 60.9d | $+512.97 |
| 41 | `0x7c9bbcfd592dcf4b76F75219DDfd2C9F2188bAc5` **ML Yield Hunter** | $0 | -2.05% | -20.29% | -18.53% | 16.21% | +0.10 | +0.10 | -1.25 | 36.9d | $-298.23 |

† window shorter than 30 days — annualised figures are fragile at that length.

✂ earlier history contained an impossible period return, so the figures are computed on the clean trailing window only; the Window column shows its length.

⚠ chain invalid or unavailable — annualised columns suppressed rather than printed from an impossible period return (usually a deposit landing between two API samples).

Net P&L is the realised dollar result over the same window as the other columns -- net of fees and funding, deposits and withdrawals excluded. It is a total, not a rate, so it is shown even where the annualised columns are suppressed: it never divides by an equity figure.

Returns are time-weighted: per-period returns chained over Hyperliquid's `pnlHistory`, which excludes deposits and withdrawals. TVL rank says nothing about performance — that is what the other columns are for.

A sortable version of this table is published at [the GitHub Pages site](https://zwallfacer.github.io/vault-perf/).
