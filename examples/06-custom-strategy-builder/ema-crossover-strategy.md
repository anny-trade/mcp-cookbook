# EMA Crossover Strategy

The EMA 9/21 crossover was the most consistently profitable strategy type found in the research —
93% of tests across 10 assets beat buy-and-hold on the daily chart.

## Prompt

```
Backtest a strategy on BTC daily: enter long when EMA(9) crosses above EMA(21),
exit when EMA(9) crosses below EMA(21). Use 3% stop-loss and 6% take-profit over 1 year.
```

## Tools Used

- `backtest_custom_strategy`

## Condition JSON

```json
{
  "name": "EMA 9/21 Crossover",
  "asset": "BTC",
  "interval": "1d",
  "direction": "long",
  "lookback_period": "1y",
  "trigger": {
    "indicator": "EMA",
    "params": { "period": 9 },
    "field": "value",
    "operator": "crosses_above",
    "compare_to": {
      "indicator": "EMA",
      "params": { "period": 21 },
      "field": "value"
    }
  },
  "confirmations": [],
  "stop_loss": { "type": "percent", "value": 3 },
  "take_profit": { "type": "percent", "value": 6 }
}
```

## Auth Required

Yes

## Credit Cost

Included in message cost (billed as LLM usage, equivalent to ~100 credits)

## Research Baseline

Tested across 10 assets on 1d/1y:
- **BTC/1d:** +42.25% return, +51.77% delta vs B&H, 58.8% win rate, Sharpe 9.42, DD 9.13%
- **ETH/1d:** +29.51% return, +23.81% delta, 54.5% win rate, Sharpe 8.00, DD 8.08%
- **AVAX/1d:** +21.69% return, +75.72% delta, 60% win rate, Sharpe 10.70, DD 9.90%

EMA 9/21 outperforms the classic 50/200 golden cross. The faster pair captures more trades
with sufficient signal quality for the daily timeframe.

## Expected Response Shape

```json
{
  "name": "EMA 9/21 Crossover",
  "asset": "BTC",
  "interval": "1d",
  "performance": {
    "totalReturn": 0.0,
    "buyHoldReturn": 0.0,
    "delta": 0.0,
    "winRate": 0.0,
    "profitFactor": 0.0,
    "sharpeRatio": 0.0,
    "maxDrawdown": 0.0,
    "avgHoldDays": 0.0,
    "tradeCount": 0
  },
  "oos": { "return": 0.0, "validated": true },
  "signalStatus": "...",
  "trades": [
    { "entry": "...", "exit": "...", "return": 0.0, "holdDays": 0 }
  ]
}
```

## Variations

```
Try EMA 12/26 instead — does the wider pair perform better?
```

```
Add a confirmation: price must be above EMA(200) to enter long.
```

```
Run the same strategy on ETH and AVAX for comparison.
```

```
Test EMA 50/200 golden cross — the classic version.
```

## See Also

- [multi-indicator-confluence.md](multi-indicator-confluence.md) — add RSI + MACD confirmation for higher alpha
- [deploy-strategy-as-bot.md](deploy-strategy-as-bot.md) — deploy after validation
- [research/strategy-rankings-1d.md](../../research/strategy-rankings-1d.md) — full leaderboard
