# What are today's Bitcoin ETF inflows and outflows by issuer?

Per-issuer 7-day and YTD flow breakdown — who is buying and who is selling.

## Prompt

```
Show me the Bitcoin ETF flows broken down by issuer. Who led inflows this week?
```

## Tools Used

- `get_institutional_intelligence` — coin: `BTC`

## Auth Required

No (guest accessible)

## Credit Cost

0

## What Anny Returns

Net flows for each Bitcoin ETF issuer: BlackRock (IBIT), Fidelity (FBTC), ARK 21Shares
(ARKB), Invesco (BTCO), Bitwise (BITB), WisdomTree (BTCW), and others. Daily, 7-day,
30-day, and YTD flows per issuer. Total aggregate flows with a flow streak indicator
(how many consecutive days of net inflow/outflow). ETF approval status per coin.

IBIT (BlackRock) dominates total AUM — its flows are the most market-moving. Sustained
divergence between IBIT inflows and FBTC outflows often signals institutional rotation
rather than pure buying pressure.

## Expected Response Shape

```json
{
  "btcEtf": {
    "totalAum": "...",
    "dailyFlow": 0.0,
    "7dFlow": 0.0,
    "ytdFlow": 0.0,
    "consecutiveInflowDays": 0,
    "byIssuer": [
      {
        "name": "...",
        "ticker": "...",
        "dailyFlow": 0.0,
        "7dFlow": 0.0,
        "ytdFlow": 0.0,
        "aum": 0.0
      }
    ]
  },
  "internationalEtfs": { "summary": "..." }
}
```

## Variations

```
How much has IBIT accumulated year-to-date?
```

```
Are ETH ETF flows positive or negative this week?
```

```
Show me the full institutional picture for BTC — ETFs and corporate treasuries.
```

## See Also

- [market-state-snapshot.md](market-state-snapshot.md) — aggregate ETF flow inside full market snapshot
- [examples/01-guest-no-auth/institutional-intelligence.md](../01-guest-no-auth/institutional-intelligence.md) — whale activity and corporate treasuries
