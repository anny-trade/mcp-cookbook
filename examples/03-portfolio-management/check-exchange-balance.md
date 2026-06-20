# How do I check my crypto balances across all connected exchanges?

Ask Anny for your balances and it queries every exchange you've connected to your account at once,
then returns them in a single combined view. "All connected exchanges" means each exchange you've
linked in Anny — both Full-mode exchanges (where you can also place orders) and Portfolio-mode
exchanges (balance view only). For each one, `get_exchange_balance` reports your **free** balance
(available to trade or withdraw) and your **locked** balance (reserved by open orders), so you
know exactly how much you can actually deploy. Pass an asset filter like `USDT` to see one coin
across every exchange, or omit it to get all non-zero balances. The response also rolls up a
`totalFreeUsdt` figure so you can see your total available buying power without adding it up by
hand.

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
