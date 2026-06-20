# How do I check balances and place trades through Anny's MCP?

Anny's portfolio tools let you inspect what you hold and act on it from inside your AI client.
`get_exchange_balance` returns free and locked balances across every connected exchange,
`check_symbol_availability` confirms an asset is tradeable before you buy, and
`execute_market_order` places a SPOT market buy or sell using a mandatory two-step preview →
confirm flow. You can also list pending orders with `get_open_orders` and cancel them with
`cancel_order`. Every order is capped server-side and limited to SPOT — no futures, no margin —
so a mistaken prompt can never place an oversized or leveraged trade.

## Safety First

**All exchange mutation tools place real orders on your connected exchange.** Follow this
two-step flow for every order:

1. Call with `confirm=false` (default) — Anny shows a preview including estimated price,
   quantity, fees, and total cost
2. Review the preview
3. Call again with `confirm=true` only if the preview looks correct

A `MAX_CHAT_ORDER_USDT` cap is enforced server-side — the platform will reject orders
above this threshold regardless of what you ask. SPOT market only — no futures, no margin.

## Supported Exchanges

Order placement requires a **Full-mode** exchange: Binance, Bybit, OKX, Kraken, KuCoin,
Gate.io, MEXC, and others. Portfolio-mode exchanges (balance view only) cannot place orders.
Full list and setup guides: [setup/supported-exchanges.md](../../setup/supported-exchanges.md)

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

## See Also

- [../04-signal-management/README.md](../04-signal-management/) — manage signals and automation that drive these orders
- [../08-risk-analytics/README.md](../08-risk-analytics/) — stress-test the portfolio before you add to it
- [../02-market-intelligence/README.md](../02-market-intelligence/) — check market conditions before placing an order
