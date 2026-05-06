# List Active Signals

Get all active trading signals and positions with P&L and automation state.

## Prompt

```
What signals do I have open right now? Show me the P&L and automation status for each.
```

## Tools Used

- `list_active_signals` — limit: 20

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

All active signals with: signal ID, asset, direction (long/short), entry price, current price,
unrealized P&L (percentage and USDT), stop-loss and target prices, exchange, and automation
flags (auto-invest, auto-stop, auto-sell enabled/disabled).

## Expected Response Shape

```json
{
  "signals": [
    {
      "id": "...",
      "asset": "...",
      "direction": "...",
      "entryPrice": 0.0,
      "currentPrice": 0.0,
      "pnlPct": 0.0,
      "pnlUsdt": 0.0,
      "stopLoss": 0.0,
      "target1": 0.0,
      "exchange": "...",
      "automation": {
        "autoInvest": false,
        "autoStop": false,
        "autoSell": false
      }
    }
  ],
  "total": 0
}
```

## Variations

```
Show my active signals on Binance only.
```

```
Which signals are most profitable right now?
```

```
List my 50 most recent signals.
```

## See Also

- [analyze-signal-with-cfo.md](analyze-signal-with-cfo.md) — overlay CFO analysis on any signal
- [toggle-automation.md](toggle-automation.md) — enable auto-buy after reviewing the list
