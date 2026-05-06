# Update Signal Targets

Update a target price, stop-loss, or entry price for a signal. DB-only — no exchange orders.

## Prompt

```
Update the stop-loss for signal #12345 to $45,000.
```

## Tools Used

- `update_signal_target` — signal_id: `12345`, target_field: `tradeStopLossPrice`, price: `45000`

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

Confirmation of the updated field and new price. This is a database-only update — it changes
the price level stored in Anny that the automation engine uses. It does not modify any existing
exchange stop-loss order. If you need to move an actual exchange order, cancel it first and
place a new one.

## Available Fields

| Field | Description |
|-------|-------------|
| `tradeStopLossPrice` | Stop-loss trigger price |
| `tradeEntryPriceMin` | Minimum entry price |
| `tradeEntryPriceMid` | Middle entry price |
| `tradeEntryPriceMax` | Maximum entry price |
| `tradeExitPrice1` | First take-profit target |
| `tradeExitPrice2` | Second take-profit target |
| `tradeExitPrice3` | Third take-profit target |
| `tradeExitPrice4` | Fourth take-profit target |
| `tradeExitPrice5` | Fifth take-profit target |

## Expected Response Shape

```json
{
  "signalId": "...",
  "field": "tradeStopLossPrice",
  "oldPrice": 0.0,
  "newPrice": 45000.0,
  "updated": true
}
```

## Variations

```
Change target 1 for signal #12345 to $52,000.
```

```
Update the entry price range for signal #12345 — min $43,000, max $44,500.
```

## See Also

- [toggle-automation.md](toggle-automation.md) — ensure auto-stop is enabled to act on the new price
- [list-active-signals.md](list-active-signals.md) — view current prices before updating
