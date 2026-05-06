# Market Overview

Get a cross-market snapshot: BTC regime, S&P 500 / Gold correlations, Fear & Greed context.

## Prompt

```
Give me a full market overview — what's the current regime, how is BTC correlating with
equities, and what's the Fear & Greed streak?
```

## Tools Used

- `get_market_analysis` — no parameters required

## Auth Required

No — guest access

## Credit Cost

0

## What Anny Returns

BTC regime detection (SMA20/SMA50 crossover: bullish / bearish / neutral), 30-day Pearson
correlations between BTC and the S&P 500 and Gold, S&P 500 and Gold prices with 7-day
changes, BTC 30-day price range, total crypto market cap, and Fear & Greed streak (how many
consecutive days in the current zone).

High BTC-S&P 500 correlation (above 0.7) means crypto is trading as a risk asset — macro
events move both. Low correlation (below 0.3) suggests crypto is decoupling.

## Expected Response Shape

```json
{
  "btcRegime": "...",
  "correlations": {
    "btc_sp500_30d": 0.0,
    "btc_gold_30d": 0.0
  },
  "traditionalMarkets": {
    "sp500Price": 0.0,
    "sp5007dChange": 0.0,
    "goldPrice": 0.0,
    "gold7dChange": 0.0
  },
  "btc30dRange": { "low": 0.0, "high": 0.0 },
  "totalMarketCapUsd": "...",
  "fearGreedStreak": "..."
}
```

## Variations

```
How is BTC correlating with gold right now?
```

```
Is the market in a bull or bear regime?
```

```
What's the 30-day price range for BTC?
```

## See Also

- [examples/02-market-intelligence/fear-greed-context.md](../02-market-intelligence/fear-greed-context.md) — deeper Fear & Greed analysis
- [examples/02-market-intelligence/cross-market-correlations.md](../02-market-intelligence/cross-market-correlations.md) — correlation deep dive
