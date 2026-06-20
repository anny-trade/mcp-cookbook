# Is this cryptocurrency available to trade on my exchange?

Confirm an asset is available for trading on your connected exchanges before placing an order.

## Prompt

```
Can I buy DOGE on my connected exchange? What's the minimum order size?
```

## Tools Used

- `check_symbol_availability` — asset: `DOGE`

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

Whether the asset is available for SPOT trading, which exchange(s) support it, the
full trading pair (e.g., `DOGE/USDT`), and the minimum order size in both asset units
and USDT equivalent. When more than one connected exchange lists the asset, the response
shows each so you can pick where to route the order — a coin may trade on one exchange but not
another, and the minimums often differ between them.

Always run this before `execute_market_order` for assets you haven't traded before.
Minimum order sizes vary by exchange and asset — ordering below the minimum will fail, so
checking first turns a rejected order into a clean one. It also catches symbols that aren't
listed at all before you spend a turn on a buy that can't execute.

## Expected Response Shape

```json
{
  "asset": "DOGE",
  "available": true,
  "exchanges": [
    {
      "exchange": "...",
      "pair": "DOGE/USDT",
      "minOrderQty": 0.0,
      "minOrderUsdt": 0.0,
      "spotEnabled": true
    }
  ]
}
```

## Variations

```
Is PEPE available for trading on Binance?
```

```
Can I buy SOL on my exchange? What's the minimum?
```

```
Check if WIF is tradeable on my accounts.
```

## See Also

- [execute-buy-order.md](execute-buy-order.md) — place the order after checking availability
- [check-exchange-balance.md](check-exchange-balance.md) — check you have enough USDT first
