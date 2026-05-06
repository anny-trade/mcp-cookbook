# Scan Live Conditions

Check if your strategy conditions are met right now against live market data — for free.

## Prompt

```
Is RSI(14) below 30 on BTC right now? Is price above EMA(200)?
```

## Tools Used

- `scan_custom_signals` — asset: `BTCUSDT`, interval: `1d`

## Auth Required

Yes

## Credit Cost

0 — live scanning is always free

## What Anny Returns

Per-condition status: MET / NOT_MET / APPROACHING. For APPROACHING, the indicator value
is within 5% of the threshold — useful for setting alerts manually. Overall signal status:
ACTIVE (all conditions met), APPROACHING (at least one approaching), or INACTIVE.

Always scan before spending 100 credits on a backtest — if the conditions aren't even close
to firing right now, the backtest will show 0 recent trades and you'll know to adjust the
thresholds.

## Condition JSON for Scan

```json
{
  "asset": "BTCUSDT",
  "interval": "1d",
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
  ]
}
```

## Expected Response Shape

```json
{
  "asset": "BTCUSDT",
  "interval": "1d",
  "overallStatus": "...",
  "conditions": [
    {
      "indicator": "RSI(14)",
      "currentValue": 0.0,
      "threshold": 30,
      "status": "...",
      "description": "..."
    },
    {
      "indicator": "PRICE vs EMA(200)",
      "currentValue": 0.0,
      "threshold": 0.0,
      "status": "..."
    }
  ],
  "checkedAt": "..."
}
```

## Variations

```
Is EMA(9) above EMA(21) on BTC right now?
```

```
Check if MACD histogram is positive on ETH daily.
```

```
Scan for my ADA confluence strategy conditions.
```

## See Also

- [ema-crossover-strategy.md](ema-crossover-strategy.md) — backtest the conditions you just scanned
- [deploy-strategy-as-bot.md](deploy-strategy-as-bot.md) — deploy a bot to run automatically
