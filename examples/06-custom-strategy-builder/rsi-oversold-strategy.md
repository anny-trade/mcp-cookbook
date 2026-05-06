# RSI Oversold Strategy

Enter when RSI dips below 30 (oversold) with price above EMA(200) as a trend filter.

## Prompt

```
Backtest a strategy on BTC daily: buy when RSI(14) crosses below 30 and price is above
EMA(200). Stop-loss 3%, take-profit 2:1 risk-reward. Last year of data.
```

## Tools Used

- `backtest_custom_strategy`

## Condition JSON

```json
{
  "name": "RSI Oversold + EMA200 Filter",
  "asset": "BTC",
  "interval": "1d",
  "direction": "long",
  "lookback_period": "1y",
  "trigger": {
    "indicator": "RSI",
    "params": { "period": 14 },
    "field": "value",
    "operator": "crosses_below",
    "compare_to": 30
  },
  "confirmations": [
    {
      "indicator": "PRICE",
      "field": "close",
      "operator": "above",
      "compare_to": {
        "indicator": "EMA",
        "params": { "period": 200 },
        "field": "value"
      }
    }
  ],
  "stop_loss": { "type": "percent", "value": 3 },
  "take_profit": { "type": "risk_reward", "value": 2 }
}
```

## Auth Required

Yes

## Credit Cost

Included in message cost

## Research Context

RSI Mean Reversion was the 8th-ranked strategy type on 1d (82% profitable, avg +33% delta).
It performed better on assets with high flip frequency — DOT was the best RSI asset with
+16.02% return and +86.71% delta vs buy-and-hold. The EMA(200) filter is the most impactful
single confirmation — removing counter-trend entries improves win rate significantly.

## Expected Response Shape

```json
{
  "name": "RSI Oversold + EMA200 Filter",
  "asset": "BTC",
  "performance": {
    "totalReturn": 0.0,
    "delta": 0.0,
    "winRate": 0.0,
    "sharpeRatio": 0.0,
    "maxDrawdown": 0.0,
    "tradeCount": 0
  },
  "oos": { "return": 0.0, "validated": true },
  "signalStatus": "..."
}
```

## Variations

```
Try RSI(7) < 25 for a more extreme oversold entry.
```

```
Add ADX > 20 confirmation to only enter when trend is present.
```

```
Test the same strategy on DOT — the best RSI asset from research.
```

## See Also

- [multi-indicator-confluence.md](multi-indicator-confluence.md) — combine RSI with EMA trend and MACD
- [scan-live-conditions.md](scan-live-conditions.md) — check if RSI < 30 right now before backtesting
