# Should I use long-only or long-short mode for CFO Line backtesting?

Compare CFO Line in `long` mode vs `long_short` mode on the same asset and timeframe.

## Prompt

```
Run the CFO Line backtest on DOGE daily in both long-only and long-short modes.
Which performs better on risk-adjusted returns?
```

## Tools Used (2 calls)

- `backtest_custom_strategy` — asset: `DOGE`, interval: `1d`, period: `1y`, mode: `long`
- `backtest_custom_strategy` — asset: `DOGE`, interval: `1d`, period: `1y`, mode: `long_short`

## Auth Required

Yes

## Credit Cost

200 credits

## What Anny Returns

Two backtest results for side-by-side comparison. `long` mode only enters trades during
Accumulate flips. `long_short` mode also enters short trades during Distribute flips.

## Choosing Between Modes

| Mode | Use When | Risk |
|------|----------|------|
| `long` | Bull market, assets with positive long-term drift | Lower — no short exposure |
| `long_short` | Bear market or assets with downward drift | Higher — short trades can gap against you |
| `short` | Bear market only (e.g., SOL/DOT in 2025 downturn) | Directional bet against the asset |

Research finding: In the walk-forward analysis, DOGE showed 77% confidence in its current
DISTRIBUTE regime with the conservative distribute filter validating on unseen data. This is
a case where `long_short` mode may outperform pure `long` — the short signals are validated.

## Variations

```
Compare long vs long_short for BTC on the daily chart.
```

```
Test short-only mode on DOT daily — it was the top performer in short mode during the bear market.
```

## See Also

- [btc-daily-backtest.md](btc-daily-backtest.md) — BTC defaults to long mode
- [research/cfo-line-regime-analysis.md](../../research/cfo-line-regime-analysis.md) — regime-specific analysis and confidence scores
