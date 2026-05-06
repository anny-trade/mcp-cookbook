# Portfolio Management

Check balances, preview orders, and execute trades — safely.

## Safety First

**All exchange mutation tools place real orders on your connected exchange.** Follow this
two-step flow for every order:

1. Call with `confirm=false` (default) — Anny shows a preview including estimated price,
   quantity, fees, and total cost
2. Review the preview
3. Call again with `confirm=true` only if the preview looks correct

A `MAX_CHAT_ORDER_USDT` cap is enforced server-side — the platform will reject orders
above this threshold regardless of what you ask. SPOT market only — no futures, no margin.

## Auth Required

Yes — exchange mutation tools require OAuth (not just PAT). Use the `/v1/full` endpoint
or the standard `/mcp` endpoint (which is an alias for `/v1/full`).

## Tools in This Section

- `get_exchange_balance` — check balances across all connected exchanges
- `check_symbol_availability` — confirm an asset is tradeable before buying
- `execute_market_order` — buy or sell at market price (2-step confirm)
- `get_open_orders` — list all pending orders
- `cancel_order` — cancel a pending order

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [check-exchange-balance.md](check-exchange-balance.md) | Query USDT and asset balances |
| [check-symbol-availability.md](check-symbol-availability.md) | Verify asset is tradeable before buying |
| [execute-buy-order.md](execute-buy-order.md) | 2-step preview → execute buy |
| [list-open-orders.md](list-open-orders.md) | List pending orders with filter examples |
| [cancel-order.md](cancel-order.md) | Cancel a specific order (requires orderId from list first) |
