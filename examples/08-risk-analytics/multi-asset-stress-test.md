# How does my portfolio perform if Bitcoin drops 40% and altcoins follow?

Specify exact percentages per asset using the structured input format.

## Prompt

```
Stress test my portfolio: BTC drops 30%, ETH drops 40%, SOL drops 50%.
Show me the before/after and which position takes the most damage.
```

## Tools Used

- `run_scenario` — assets: structured array

## Structured Input Format

```json
{
  "assets": [
    { "asset": "BTC", "changePct": -30 },
    { "asset": "ETH", "changePct": -40 },
    { "asset": "SOL", "changePct": -50 }
  ]
}
```

The structured `assets` array takes precedence over a free-text scenario string — use this
when you need precise control over each asset's move.

## Auth Required

Yes

## Credit Cost

0

## Expected Response Shape

```json
{
  "scenario": "Custom multi-asset scenario",
  "before": { "totalValue": 0.0, "riskScore": 0 },
  "after": {
    "totalValue": 0.0,
    "changePct": 0.0,
    "changeUsdt": 0.0
  },
  "byAsset": [
    {
      "asset": "...",
      "appliedChange": 0.0,
      "currentValue": 0.0,
      "scenarioValue": 0.0
    }
  ],
  "worstPosition": { "asset": "...", "lossUsdt": 0.0 }
}
```

## Variations

```
Simulate only BTC and ETH crashing, with LINK unchanged.
```

```
What if everything drops 20% uniformly?
```

```
Run a recovery scenario: BTC +50%, ETH +70%.
```

## See Also

- [portfolio-scenario-crash.md](portfolio-scenario-crash.md) — free-text scenario string
- [research/portfolio-construction.md](../../research/portfolio-construction.md) — correlation matrix used to interpret results
