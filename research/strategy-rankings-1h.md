# Which crypto trading strategies ranked best on the 1h timeframe?

> Published: 2026-04-26 — backtest data as of the 2026-04-26 strategy run (702 combinations, 12 assets on Binance spot).

The 1h timeframe tells a different story. Most trend-following strategies degrade sharply
when applied to intraday data.

## Key Finding: 1d vs 1h

| Metric | 1d/1y | 1h/1y |
|--------|-------|-------|
| Strategies beating B&H | **59%** | **25%** |
| EMA Crossover profitable% | 93% | 48% |
| MACD Momentum profitable% | 93% | 30% |
| Best avg Sharpe strategy | CFO Line 5.74 | BB+RSI 7.97 (SOL only) |

**The 1h timeframe has more noise, wider spreads relative to signal, and transaction costs
eat returns 4× faster.** Trend-following strategies that dominate on 1d collapse on 1h.

## CFO Line on 1h (Discovery Results)

| Asset | Total Return | OOS Return | Sharpe | Trades | Verdict |
|-------|-------------|------------|--------|--------|---------|
| DOGE | +67.40% | -2.64% | 1.51 | 10 | CAUTION |
| DOT | +67.50% | -8.21% | 2.08 | 7 | CAUTION |
| ETH | +57.39% | -10.79% | 1.53 | 6 | INVALID |
| AVAX | +50.32% | -21.98% | 1.45 | 4 | INVALID |
| NEAR | +46.07% | -4.63% | 1.21 | 11 | CAUTION |
| ADA | +41.45% | -27.75% | 1.24 | 5 | INVALID |
| SOL | +18.79% | -2.25% | 0.70 | 6 | CAUTION |
| **LINK** | +15.18% | **+8.90%** | 0.66 | 2 | VALID |
| BNB | +6.52% | -3.04% | 0.53 | 2 | CAUTION |
| BTC | +3.84% | -2.67% | 1.16 | 1 | CAUTION |
| **XRP** | -5.09% | **+3.24%** | -0.28 | 2 | VALID |

Only LINK and XRP passed OOS validation on 1h — both with just 2 trades (low statistical
significance).

## Best Strategy Per Asset on 1h

| Asset | Best Strategy | Return | Delta | Sharpe | Trades |
|-------|--------------|--------|-------|--------|--------|
| BTC | MACD Momentum (12/26/9) | +12.63% | +3.43% | 6.13 | 6 |
| ETH | RSI Mean Rev (RSI 21, OS=35) | +21.28% | +9.91% | 5.32 | 18 |
| SOL | BB + RSI Combo | +17.34% | +18.54% | 7.97 | 9 |
| ADA | EMA Crossover (9/21) | +25.99% | +30.29% | 7.41 | 13 |
| DOT | ADX Trend (thresh=25) | +20.04% | +31.02% | 10.57 | 5 |

## Strategy Consistency Across Timeframes

| Strategy | 1d/1y Profitable% | 1h/1y Profitable% | Verdict |
|----------|------------------|------------------|---------|
| EMA Crossover | 93% | 48% | Best on 1d, degrades sharply on 1h |
| MACD Momentum | 93% | 30% | Needs volume of trades (2y data) |
| ADX Trend | 90% | 44% | Consistent direction but fewer trades on 1h |
| CFO Anny Line | 90% | 38% | Conservative, needs longer lookback |
| BB + RSI Combo | 80% | **63%** | Surprise winner on 1h |
| RSI Mean Reversion | 82% | 56% | Better on 1h (mean-reversion suits intraday) |

**Key insight:** If you must use 1h, mean-reversion strategies (BB+RSI, RSI) perform better
than trend-following. The opposite is true on 1d.
