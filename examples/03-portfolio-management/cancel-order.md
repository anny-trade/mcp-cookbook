# Cancel an Order

Cancel a specific pending order. Always get the order ID from `get_open_orders` first.

> **WARNING:** This cancels a real order on your exchange. The action is immediate and
> irreversible. Always run `get_open_orders` first to confirm the correct order ID.

## Step 1: Get the Order ID

### Prompt

```
Show me my pending orders for BTC/USDT.
```

### Tools Used

- `get_open_orders` — symbol: `BTC/USDT`

Note the `orderId` from the response before proceeding.

---

## Step 2: Cancel the Order

### Prompt

```
Cancel order 987654321 for BTC/USDT on Binance.
```

### Tools Used

- `cancel_order` — orderId: `987654321`, symbol: `BTC/USDT`, exchangeCode: `BINANCE`

### Auth Required

Yes — `/v1/full` endpoint required (exchange mutation)

### Credit Cost

0

### What Anny Returns

Confirmation that the order was cancelled, including the order ID, symbol, and cancellation
timestamp. If the order was already filled or doesn't exist, an error is returned.

### Expected Response Shape

```json
{
  "cancelled": true,
  "orderId": "...",
  "symbol": "...",
  "exchange": "...",
  "cancelledAt": "..."
}
```

---

## Variations

```
Cancel all my pending DOGE orders.
```

```
Cancel my limit buy order for ETH — order ID 112233445.
```

## See Also

- [list-open-orders.md](list-open-orders.md) — always run this first to get the correct orderId
- [examples/04-signal-management/cancel-order.md](../04-signal-management/) — cancel signal-linked orders via `cancel_pending_order`
