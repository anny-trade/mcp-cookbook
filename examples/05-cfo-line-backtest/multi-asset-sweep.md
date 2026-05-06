# Multi-Asset Sweep

Run CFO Line backtests on DOT, XRP, and DOGE — the three strongest OOS performers from
the overnight research session.

## Prompt

```
Backtest the CFO Line on DOT, XRP, and DOGE — all on the daily chart over 1 year.
Rank them by out-of-sample return.
```

## Tools Used (3 calls)

- `run_cfo_line_backtest` — asset: `DOT`, interval: `1d`, period: `1y`, mode: `long`
- `run_cfo_line_backtest` — asset: `XRP`, interval: `1d`, period: `1y`, mode: `long`
- `run_cfo_line_backtest` — asset: `DOGE`, interval: `1d`, period: `1y`, mode: `long`

## Auth Required

Yes

## Credit Cost

300 credits (100 per asset)

## What Anny Returns

Three separate backtest results. Ask Anny to rank by OOS return and summarize the
consistency of results.

## Research Baseline

From the overnight research (1d/2y, validated with train/test split):

| Asset | In-Sample Return | OOS Return | Sharpe | Max DD |
|-------|-----------------|------------|--------|--------|
| DOT | +303.19% | +25.44% | 1.35 | — |
| XRP | +81.16% | +23.94% | 0.78 | — |
| DOGE | +76.74% | +14.41% | 0.84 | — |

DOT was the standout performer — 303% in-sample with the strongest OOS validation of any
asset tested. XRP's high flip frequency (69 flips over 902 candles) provides good parameter
tuning opportunity. DOGE had the highest walk-forward confidence (77%) in separate analysis.

## Variations

```
Also run BTC and ETH for comparison — which 5-asset portfolio makes the most sense?
```

```
Run the sweep in long_short mode to include short trades.
```

## See Also

- [research/oos-validation-results.md](../../research/oos-validation-results.md) — complete OOS table for all 8 validated assets
- [examples/07-strategy-optimization/optimizer-workflow.md](../07-strategy-optimization/optimizer-workflow.md) — optimize the best performers
- [scripts/backtest/cfo_line_multi_asset.py](../../scripts/backtest/cfo_line_multi_asset.py) — automate this sweep programmatically
