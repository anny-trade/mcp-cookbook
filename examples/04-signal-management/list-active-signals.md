# What trading signals do I have active right now?

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

The unrealized P&L is marked to the current price, so it moves with the market between calls — a
positive number means the position is in profit at this moment, not that it has been closed. The
automation flags tell you, per signal, whether Anny will act on its own: auto-invest controls
entry, auto-stop the stop-loss, and auto-sell the take-profit. Use the signal ID to drill into
one position with `get_signal` or to change its targets with `update_signal_target`.

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
