# How do I check my crypto balances across all connected exchanges?

Query available balances across all connected exchanges.

## Prompt

```
How much USDT do I have available across all my exchanges?
```

## Tools Used

- `get_exchange_balance` — asset: `USDT`

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

Available (free) and locked (in open orders) balance for the specified asset on each
connected exchange. If no asset filter is provided, returns all non-zero balances.

## Expected Response Shape

```json
{
  "balances": [
    {
      "exchange": "...",
      "asset": "USDT",
      "free": 0.0,
      "locked": 0.0,
      "total": 0.0
    }
  ],
  "totalFreeUsdt": 0.0
}
```

## Variations

```
Show all my exchange balances.
```

```
How much BTC do I hold on Binance?
```

```
What's my total portfolio value across all exchanges?
```

## See Also

- [check-symbol-availability.md](check-symbol-availability.md) — confirm asset is tradeable before buying
- [execute-buy-order.md](execute-buy-order.md) — buy after checking you have enough USDT
