# BTC Daily CFO Line Backtest

Run the CFO Line on BTC at daily resolution over the last year. Full response shape documented.

## Prompt

```
Backtest the CFO Line on BTC using the daily chart over the last year.
```

## Tools Used

- `run_cfo_line_backtest` — asset: `BTC`, interval: `1d`, period: `1y`, mode: `long`

## Auth Required

Yes

## Credit Cost

100 credits

## What Anny Returns

Performance metrics for the full in-sample period and the out-of-sample 20% holdout split.
Includes total return, comparison against buy-and-hold (delta), win rate, profit factor,
Sharpe ratio, max drawdown, trade count, and filter rejection statistics (how many signals
were filtered vs executed).

## Expected Response Shape

```json
{
  "asset": "BTC",
  "interval": "1d",
  "period": "1y",
  "mode": "long",
  "performance": {
    "totalReturn": 0.0,
    "buyHoldReturn": 0.0,
    "delta": 0.0,
    "winRate": 0.0,
    "profitFactor": 0.0,
    "sharpeRatio": 0.0,
    "maxDrawdown": 0.0,
    "tradeCount": 0
  },
  "oos": {
    "return": 0.0,
    "winRate": 0.0,
    "tradeCount": 0,
    "validated": true
  },
  "filterStats": {
    "totalSignals": 0,
    "executed": 0,
    "rejected": 0
  }
}
```

## Research Context

In the overnight research session, BTC/1d showed **+5.01% total return** with a
**+12.76% out-of-sample return** — meaning the strategy made more on unseen data than
on training data. This is rare and suggests genuine robustness rather than overfitting.

The key insight: BTC on 1d has a 59% profit rate (vs 19% on 1h), making the daily timeframe
far more suitable for CFO Line trading.

## Variations

```
Backtest CFO Line on BTC daily over the last 6 months.
```

```
Run the same backtest in long_short mode to also profit from Distribute flips.
```

```
Backtest BTC on the weekly chart.
```

## See Also

- [multi-asset-sweep.md](multi-asset-sweep.md) — run the same backtest on DOT, XRP, and DOGE
- [examples/07-strategy-optimization/optimizer-workflow.md](../07-strategy-optimization/optimizer-workflow.md) — optimize after seeing results
- [research/oos-validation-results.md](../../research/oos-validation-results.md) — full OOS table
