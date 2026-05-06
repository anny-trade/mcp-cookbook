# How confident should I be in a Bitcoin CFO Line flip signal?

When BTC or any asset flips state, a confidence score (0–100) tells you whether to act or wait.

## Prompt

```
BTC just flipped to Accumulate — should I trust it? What's the confidence score?
```

## Tools Used

- `get_flip_intelligence` — asset: `BTC`, timeframe: `1d`

## Auth Required

No — guest access

## Credit Cost

0

## What Anny Returns

A confidence score from 0 to 100 with a label (Low / Medium / High / Very High). Three
sub-scores explain the rating: band gap score (how far the bands have separated — larger gap
= more conviction), duration score (how long the prior state lasted — short-lived states flip
back more often), and historical score (how this setup has resolved in the past for this asset).

Also returns a contrarian flag — if BTC just flipped to Accumulate but 80% of all tracked
assets are still in Distribute, this flip is contrarian. Contrarian flips at key support levels
can be high-value; contrarian flips in a broad downtrend are riskier.

Returns `null` if no recent flip was detected (asset has been in the same state for a while).

## Expected Response Shape

```json
{
  "asset": "BTC",
  "timeframe": "1d",
  "confidence": 0,
  "confidenceLabel": "...",
  "subScores": {
    "bandGap": 0,
    "duration": 0,
    "historical": 0
  },
  "contrarian": false,
  "marketContext": {
    "accumulate": 0.0,
    "wait": 0.0,
    "distribute": 0.0
  },
  "detectedAt": "..."
}
```

Returns `null` if no recent flip detected.

## Variations

```
Why did ETH flip to Distribute? How confident is the signal?
```

```
Is this BTC flip contrarian or going with the market?
```

```
Check flip confidence for SOL on the 1h chart.
```

## See Also

- [examples/05-cfo-line-backtest/btc-daily-backtest.md](../05-cfo-line-backtest/btc-daily-backtest.md) — historical performance of these flips
- [examples/05-cfo-line-backtest/README.md](../05-cfo-line-backtest/README.md) — what the CFO Line is and how it was validated
