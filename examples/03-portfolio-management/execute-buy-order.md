# How do I buy crypto using AI with a preview before executing?

Buy crypto at market price using the mandatory 2-step preview → confirm flow.

> **WARNING:** This places a real order on your exchange. Always review the preview before
> confirming. A server-side `MAX_CHAT_ORDER_USDT` cap is enforced regardless of input.
> SPOT market only — no futures, no margin.

## Step 1: Preview (confirm=false)

### Prompt

```
Buy $200 worth of ETH on my exchange. Show me the preview first — don't execute yet.
```

### Tools Used

- `execute_market_order` — asset: `ETH`, action: `buy`, amount: `200`, confirm: `false`

### What Anny Returns

A preview with estimated execution price, quantity you'll receive, estimated fees, total
USDT cost, and which exchange will execute the order. No order is placed at this step.

### Expected Response Shape

```json
{
  "preview": true,
  "asset": "ETH",
  "action": "buy",
  "amountUsdt": 200.0,
  "estimatedQty": 0.0,
  "estimatedPrice": 0.0,
  "estimatedFee": 0.0,
  "exchange": "...",
  "pair": "ETH/USDT",
  "message": "Review this preview. Reply with confirm=true to execute."
}
```

---

## Step 2: Execute (confirm=true)

### Prompt

```
That looks right, execute the buy.
```

### Tools Used

- `execute_market_order` — asset: `ETH`, action: `buy`, amount: `200`, confirm: `true`

### What Anny Returns

Order confirmation with the actual executed price, quantity received, fees paid, order ID,
and a timestamp.

### Expected Response Shape

```json
{
  "executed": true,
  "orderId": "...",
  "asset": "ETH",
  "action": "buy",
  "qtyReceived": 0.0,
  "executedPrice": 0.0,
  "feePaid": 0.0,
  "timestamp": "..."
}
```

---

## Selling

```
Sell 0.5 SOL — show preview first.
```

For sells, `amount` is the asset quantity (not USDT). Preview first, then confirm.

## See Also

- [check-exchange-balance.md](check-exchange-balance.md) — verify USDT balance before buying
- [check-symbol-availability.md](check-symbol-availability.md) — check minimum order size
- [list-open-orders.md](list-open-orders.md) — see the order after it fills
