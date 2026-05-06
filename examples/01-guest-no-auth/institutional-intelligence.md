# What are the latest Bitcoin ETF flows and institutional whale activity?

ETF flows, corporate treasury holdings, whale activity — the smart money view.

## Prompt

```
What are the latest Bitcoin ETF flows and which issuer is leading?
```

## Tools Used

- `get_institutional_intelligence` — coin: `BTC`

## Auth Required

No — guest access

## Credit Cost

0

## What Anny Returns

Bitcoin and Ethereum ETF flows: daily net flow, 7-day flow, 30-day flow, and YTD flow,
with a per-issuer breakdown (BlackRock IBIT, Fidelity FBTC, ARK 21Shares, Invesco, Bitwise,
and others). Corporate treasury holdings across 154+ companies — MicroStrategy, MARA,
Metaplanet, and others. On-chain metrics: whale activity, stablecoin supply, bitcoin mined
vs bought ratio. ETF approval status per coin.

Sustained positive ETF flows (especially from institutional issuers like BlackRock) have
historically preceded price appreciation by 2–4 weeks. Negative flows combined with rising
funding rates is a historically bearish setup.

## Expected Response Shape

```json
{
  "btcEtf": {
    "dailyFlow": 0.0,
    "7dFlow": 0.0,
    "30dFlow": 0.0,
    "ytdFlow": 0.0,
    "flowStreak": "...",
    "byIssuer": [
      { "name": "...", "ticker": "...", "7dFlow": 0.0, "ytdFlow": 0.0 }
    ]
  },
  "corporateTreasury": [
    { "company": "...", "btcHeld": 0, "lastUpdated": "..." }
  ],
  "onChain": {
    "whaleActivity": "...",
    "stablecoinSupply": "...",
    "minedVsBought": "..."
  }
}
```

## Variations

```
What are the latest ETF flows?
```

```
How much Bitcoin does MicroStrategy hold?
```

```
Is there smart money accumulation happening right now?
```

```
Show me ETH ETF flows and approval status.
```

## See Also

- [examples/02-market-intelligence/etf-flow-analysis.md](../02-market-intelligence/etf-flow-analysis.md) — deeper ETF breakdown
- [compare-two-assets.md](compare-two-assets.md) — includes ETF status in fundamentals
