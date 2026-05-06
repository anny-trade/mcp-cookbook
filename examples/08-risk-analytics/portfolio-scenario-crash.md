# Portfolio Scenario: BTC Crash

What happens to your portfolio if BTC drops 40%?

## Prompt

```
What happens to my portfolio if BTC crashes 40% from current price?
```

## Tools Used

- `run_scenario` — scenario: `"BTC drops 40%"`

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

Before and after portfolio values, per-asset impact (BTC's loss + correlated alt losses),
allocation shifts (BTC becomes smaller percentage as it drops), and risk score changes.
The scenario applies BTC's move directly and infers correlated moves for alts based on
typical beta relationships.

Historical context: The research signal correlation matrix showed BTC-DOT at 66% (lowest
pair), meaning DOT typically moves 66% of BTC's move. A BTC -40% implies roughly DOT -26%
in a correlated sell-off.

## Expected Response Shape

```json
{
  "scenario": "BTC -40%",
  "before": {
    "totalValue": 0.0,
    "riskScore": 0
  },
  "after": {
    "totalValue": 0.0,
    "riskScore": 0,
    "changePct": 0.0,
    "changeUsdt": 0.0
  },
  "byAsset": [
    {
      "asset": "...",
      "currentValue": 0.0,
      "scenarioValue": 0.0,
      "impactPct": 0.0,
      "allocationBefore": 0.0,
      "allocationAfter": 0.0
    }
  ]
}
```

## Variations

```
Simulate a 2022-style crash — everything drops 70-80% from peak.
```

```
What if ETH doubles while BTC stays flat?
```

```
Model a scenario where all alts drop 50% but BTC only drops 20%.
```

## See Also

- [multi-asset-stress-test.md](multi-asset-stress-test.md) — specify exact percentages per asset
- [examples/02-market-intelligence/fear-greed-context.md](../02-market-intelligence/fear-greed-context.md) — historical context for crash scenarios
