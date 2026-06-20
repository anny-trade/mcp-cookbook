# How do I see all my open crypto orders?

See all pending (unfilled) orders across connected exchanges, with optional filters.

## Prompt

```
Do I have any open orders? Show all pending orders across my exchanges.
```

## Tools Used

- `get_open_orders` — no filters

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

All pending orders with: order ID, trading pair, side (buy/sell), order type (LIMIT,
STOP_LOSS_LIMIT, etc.), quantity, price, filled quantity, and creation timestamp. Only open
(unfilled or partially filled) orders are listed — fully filled and cancelled orders drop off,
so this is a live view of what is still working on the exchange. Compare `quantity` against
`filled quantity` to see how much of each order has executed so far.

The order ID is required to cancel a specific order — keep note of it if you plan to cancel.
Without a symbol filter the call returns open orders across every connected exchange; pass a
pair to narrow it to one market.

## Expected Response Shape

```json
{
  "orders": [
    {
      "orderId": "...",
      "exchange": "...",
      "symbol": "...",
      "side": "...",
      "type": "...",
      "qty": 0.0,
      "price": 0.0,
      "filled": 0.0,
      "createdAt": "..."
    }
  ],
  "total": 0
}
```

## Variations

```
Show my pending BTC orders on Binance.
```

```
Do I have any open stop-loss orders?
```

```
List all pending orders for ETH/USDT.
```

## See Also

- [cancel-order.md](cancel-order.md) — cancel an order using the orderId from this response
- [execute-buy-order.md](execute-buy-order.md) — place a new order
