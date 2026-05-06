# How do I compare BTC and ETH technical indicators side by side?

Head-to-head comparison: CFO Line states, performance spread, technical indicators, fundamentals.

## Prompt

```
Compare SOL vs ETH — which is showing more strength right now?
```

## Tools Used

- `compare_assets` — base: `SOL`, quote: `ETH`

## Auth Required

No — guest access

## Credit Cost

0

## What Anny Returns

CFO Anny Line state for each asset (Accumulate / Wait / Distribute), a synthetic ratio
CFO Line showing which asset has relative strength, performance spread across 1d / 7d / 30d /
90d / 1y, technical indicators (RSI, MACD, ADX, EMA) for both assets side by side, and
fundamentals (ETF approval status, tokenomics, on-chain TVL/fees/dev activity) when available.

The ratio CFO Line is particularly useful: if SOL/ETH is in Accumulate, SOL is outperforming
ETH on the proprietary band calculation — a rotation signal independent of absolute price direction.

## Expected Response Shape

```json
{
  "base": {
    "symbol": "SOL",
    "cfoPLineState": "...",
    "rsi": 0.0,
    "macd": { "histogram": 0.0 },
    "adx": 0.0,
    "ema200": 0.0
  },
  "quote": {
    "symbol": "ETH",
    "cfoPLineState": "...",
    "rsi": 0.0,
    "macd": { "histogram": 0.0 },
    "adx": 0.0,
    "ema200": 0.0
  },
  "ratioLine": {
    "state": "...",
    "interpretation": "..."
  },
  "performanceSpread": {
    "1d": 0.0,
    "7d": 0.0,
    "30d": 0.0,
    "90d": 0.0
  }
}
```

## Variations

```
Which is better right now, AVAX or LINK?
```

```
Compare BTC vs ETH — is Bitcoin showing relative strength?
```

```
Is XRP outperforming BNB this month?
```

## See Also

- [btc-technical-analysis.md](btc-technical-analysis.md) — single-asset deep dive
- [institutional-intelligence.md](institutional-intelligence.md) — ETF and fundamentals data
