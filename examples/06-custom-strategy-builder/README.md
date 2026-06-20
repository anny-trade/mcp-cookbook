# How do I build and test a custom crypto trading strategy with Anny?

You describe a strategy as a set of indicator conditions and Anny backtests it for you. An entry
is a trigger (a condition that fires on transition, like RSI crossing below 30) plus optional
confirmations (persistent conditions, like price above EMA 200), with a stop-loss and take-profit
for risk management. Build it from indicators such as RSI, EMA, SMA, MACD, ADX, ATR, BBANDS, and
StochRSI, then run `backtest_custom_strategy` to score it against history, or
`scan_custom_signals` to check whether your conditions are firing right now. Validated strategies
can be deployed as a live bot — see the deploy example below.

## How It Works

Define entry rules as conditions:

1. **Trigger** — fires when condition transitions (e.g., RSI crosses below 30)
2. **Confirmations** — persistent conditions (e.g., price is above EMA 200)
3. **Stop-loss and take-profit** — risk management per trade

Available indicators: `RSI`, `EMA`, `SMA`, `MACD`, `ADX`, `ATR`, `BBANDS`, `STOCHRSI`, `PRICE`

Operators: `crosses_above`, `crosses_below` (triggers), `above`, `below` (confirmations)

## Research-Validated Strategy Types

From testing 702 combinations across 12 assets:

| Strategy | Best For | 1d Profitable | Avg Delta |
|----------|---------|--------------|-----------|
| EMA Crossover (9/21) | BTC, ETH, AVAX | 93% | +38% |
| Multi-Indicator Confluence | ADA, DOT, bear markets | 90% | +41% |
| ADX Trend Strength | BNB, DOGE | 90% | +38% |
| StochRSI Reversal | XRP, DOGE | 85% | +37% |
| RSI Mean Reversion | DOT, general | 82% | +33% |

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [rsi-oversold-strategy.md](rsi-oversold-strategy.md) | RSI(14) < 30 with EMA(200) filter |
| [ema-crossover-strategy.md](ema-crossover-strategy.md) | EMA 9/21 — THE validated workhorse (93% profitable) |
| [multi-indicator-confluence.md](multi-indicator-confluence.md) | RSI + EMA + MACD aligned — best alpha found |
| [scan-live-conditions.md](scan-live-conditions.md) | Check if conditions are met right now (0 credits) |
| [deploy-strategy-as-bot.md](deploy-strategy-as-bot.md) | Research → backtest → deploy pipeline |

## Transaction Costs

Backtests include: 0.1% fee per side + 0.1% slippage (major assets) or 0.3% (alts).
Entry at next bar open. Stop-loss priority over take-profit on same-bar conflicts.

## See Also

- [../07-strategy-optimization/README.md](../07-strategy-optimization/) — diagnose and fix a losing custom strategy
- [../05-cfo-line-backtest/README.md](../05-cfo-line-backtest/) — compare your strategy against the CFO Line baseline
- [../09-multi-turn-workflows/README.md](../09-multi-turn-workflows/) — the research → backtest → optimize → deploy pipeline
