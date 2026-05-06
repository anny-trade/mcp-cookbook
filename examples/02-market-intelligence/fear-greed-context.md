# Fear & Greed Context

Multi-turn: get the current reading, then find historical periods with similar conditions.

## Prompt

Turn 1:
```
What's the current Fear & Greed reading and how long has it been at this level?
```

Turn 2:
```
Has this happened before? Find historical periods with similar market conditions.
```

## Tools Used

- `get_market_state` — Fear & Greed value, classification, and streak
- `find_historical_pattern` — cosine similarity matching on current conditions

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

**Turn 1:** Fear & Greed score (0–100), classification (Extreme Fear / Fear / Neutral / Greed /
Extreme Greed), and how many consecutive days the market has been in this zone.

**Turn 2:** Historical periods with similar Fear & Greed scores, RSI levels, EMA positioning,
and on-chain metrics. For each matched period: the date, the conditions at the time, and what
BTC did in the following 7 days, 30 days, and 90 days.

Note: `find_historical_pattern` requires sufficient historical data for the conditions you query.
For best results, ask about well-documented periods (extreme fear/greed) rather than narrow
specific parameter combinations. The pattern library grows as more market cycles complete.

## Expected Response Shape

Turn 1:
```json
{
  "fearGreed": {
    "value": 0,
    "classification": "...",
    "streakDays": 0,
    "streakDirection": "..."
  }
}
```

Turn 2:
```json
{
  "matchedPeriods": [
    {
      "date": "...",
      "fearGreed": 0,
      "btcRsi": 0.0,
      "btcEmaPosition": "...",
      "outcome": {
        "7d": 0.0,
        "30d": 0.0,
        "90d": 0.0
      }
    }
  ],
  "summary": "..."
}
```

## Variations

```
The market is in Extreme Fear. When has this happened before and what came next?
```

```
We've had 10 consecutive days of Greed. What does history say?
```

## See Also

- [market-state-snapshot.md](market-state-snapshot.md) — full market conditions snapshot
- [examples/08-risk-analytics/portfolio-scenario-crash.md](../08-risk-analytics/portfolio-scenario-crash.md) — act on the context with a stress test
