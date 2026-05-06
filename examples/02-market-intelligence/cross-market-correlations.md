# How is Bitcoin correlating with the S&P 500 and Gold right now?

How BTC is correlated with traditional markets — interpretation guide included.

## Prompt

```
How is BTC correlating with the S&P 500 and Gold over the last 30 days?
Interpret what this means for the current market environment.
```

## Tools Used

- `get_market_analysis` — no parameters

## Auth Required

No (guest accessible)

## Credit Cost

0

## What Anny Returns

30-day Pearson correlations between BTC and the S&P 500 and between BTC and Gold.
S&P 500 and Gold prices with 7-day changes. BTC 30-day price range and total crypto
market cap. BTC regime (SMA20/SMA50 crossover).

**Correlation interpretation guide:**
- Above +0.7: strong risk-on correlation — macro events dominate
- +0.3 to +0.7: moderate correlation — mixed drivers
- Below +0.3: decoupling — crypto-specific factors dominate
- Negative: BTC acting as alternative/hedge asset

Historically, high BTC-Gold correlation with low BTC-S&P 500 correlation signals that
BTC is being treated as a macro hedge (store of value narrative).

## Expected Response Shape

```json
{
  "btcRegime": "...",
  "correlations": {
    "btc_sp500_30d": 0.0,
    "btc_gold_30d": 0.0,
    "interpretation": "..."
  },
  "traditionalMarkets": {
    "sp500": { "price": 0.0, "7dChange": 0.0 },
    "gold": { "price": 0.0, "7dChange": 0.0 }
  },
  "btc": {
    "30dLow": 0.0,
    "30dHigh": 0.0,
    "totalMarketCap": "..."
  }
}
```

## Variations

```
Is Bitcoin decoupling from equities?
```

```
Is BTC acting more like gold or like tech stocks right now?
```

## See Also

- [market-state-snapshot.md](market-state-snapshot.md) — full market conditions including on-chain
- [examples/08-risk-analytics/portfolio-scenario-crash.md](../08-risk-analytics/portfolio-scenario-crash.md) — stress test using correlation context
