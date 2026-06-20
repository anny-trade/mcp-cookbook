# Do these crypto strategies hold up out-of-sample?

> Published: 2026-04-26 — backtest data as of the 2026-04-26 strategy run (702 combinations, 12 assets on Binance spot).

All OOS results use a strict train/test split: 80% in-sample for optimization, 20% held out
for validation. A positive OOS return means the strategy generalized to unseen data — the
gold standard for avoiding overfitting.

## Tier 1 — Strong Validation (1d strategies)

| Asset | TF | In-Sample Return | OOS Return | Sharpe | Win Rate | Trades | Strategy |
|-------|----|-----------------|------------|--------|----------|--------|---------|
| DOT | 1d | +303.19% | **+25.44%** | 1.35 | 63.64% | 11 | CFO Line |
| XRP | 1d | +81.16% | **+23.94%** | 0.78 | 30.43% | 23 | CFO Line |
| DOGE | 1d | +76.74% | **+14.41%** | 0.84 | 20% | 5 | CFO Line |
| BTC | 1d | +5.01% | **+12.76%** | 0.25 | 33.33% | 21 | CFO Line |

Note: XRP and DOGE have low win rates but positive OOS — they succeed through R:R management,
not by being right more than 50% of the time.

## Tier 2 — Moderate Validation

| Asset | TF | In-Sample Return | OOS Return | Sharpe | Trades | Strategy |
|-------|----|-----------------|------------|--------|--------|---------|
| AVAX | 1d | +39.43% | **+8.13%** | 0.62 | 7 | CFO Line |
| LINK | 1h | +15.18% | **+8.90%** | 0.66 | 2 | CFO Line |
| ETH | 1d | +18.57% | **+6.85%** | 0.42 | 18 | CFO Line |
| XRP | 1h | -5.09% | **+3.24%** | -0.28 | 2 | CFO Line |

LINK/1h and XRP/1h have only 2 trades in the test period — very low statistical significance.
Treat as directional but not statistically robust.

## Tier 3 — Failed Validation

| Asset | TF | OOS Return | Reason |
|-------|----|------------|--------|
| ADA | 1d | 0% | Filters too restrictive — 0 trades in test period |
| BNB | 1d | 0% | Same — confirmation candles filtered all entries |
| SOL | 1d | 0% | Same |
| ETH | 1h | -10.79% | Heavy overfit in training period |
| AVAX | 1h | -21.98% | CFO Line strategy overfit on 1h intraday noise |
| ADA | 1h | -27.75% | Severely negative — 1h unsuitable for ADA CFO Line |

## Custom Strategy Validations (Multi-Strategy Phase)

Selected validated results from the 702-combination study:

| Asset | Strategy | In-Sample Return | OOS Return | Sharpe |
|-------|----------|-----------------|------------|--------|
| BTC | EMA Crossover (9/21) | +42.25% | Validated | 9.42 |
| ADA | Multi-Indicator Confluence | +35.34% | Validated | 6.44 |
| BNB | ADX Trend Strength | +40.59% | Validated | 22.17 |
| DOGE | StochRSI Reversal | +53.65% | Validated | 7.84 |
| XRP | StochRSI Reversal | +55.20% | Validated | 7.95 |

Custom strategy OOS validation uses the same 80/20 split built into `backtest_custom_strategy`.

## How to Reproduce

```
Backtest the CFO Line on DOT daily over 1 year. Show me the out-of-sample return
and whether the strategy validated.
```

The backtest response includes `oos.return` and `oos.validated` fields.
For the multi-strategy results, use `backtest_custom_strategy` with matching parameters from
[strategy-rankings-1d.md](strategy-rankings-1d.md).
