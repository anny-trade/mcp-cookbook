# Diagnose a Losing Strategy

The optimizer tests your strategy across 10–15 filter combinations and identifies the root
cause of losses.

## Step 1: Free Pre-Scan

### Prompt

```
Before I spend credits, show me the loss pattern breakdown for CFO Line on ETH daily.
What category of losses is dominating?
```

### Tools Used

- `prescan_custom_strategy` — same parameters as backtest, 0 credits

### What Anny Returns

Loss pattern categories with counts: trend misalignment, overextended entry, high volatility,
revenge entry, equity drawdown. And an improvement potential rating: LOW / MEDIUM / HIGH.

---

## Step 2: Full Optimization (900 credits)

### Prompt

```
Optimize the CFO Line on ETH daily over the last year. Diagnose losing trades and
recommend the best filter settings.
```

### Tools Used

- `run_optimizer` — asset: `ETH`, interval: `1d`, period: `1y`, mode: `long`

### Auth Required

Yes (PRO tier)

### Credit Cost

900 credits

### What Anny Returns

Baseline vs optimized metrics side by side (total return, win rate, Sharpe, drawdown).
Loss diagnosis by category with counts and percentages. The winning prescription: specific
filter settings that produced the best improvement on the holdout data.

### Expected Response Shape

```json
{
  "asset": "ETH",
  "baseline": {
    "totalReturn": 0.0,
    "winRate": 0.0,
    "sharpe": 0.0,
    "maxDrawdown": 0.0
  },
  "optimized": {
    "totalReturn": 0.0,
    "winRate": 0.0,
    "sharpe": 0.0,
    "maxDrawdown": 0.0
  },
  "lossDiagnosis": {
    "whipsaw": { "count": 0, "pct": 0.0 },
    "weakConviction": { "count": 0, "pct": 0.0 },
    "counterTrend": { "count": 0, "pct": 0.0 },
    "revengeTrade": { "count": 0, "pct": 0.0 }
  },
  "prescription": {
    "confirmationCandles": 0,
    "equityCurveSma": 0,
    "atrMultiplier": 0.0,
    "spreadThreshold": 0.0
  }
}
```

## See Also

- [interpret-loss-diagnosis.md](interpret-loss-diagnosis.md) — understand what each loss category means
- [optimizer-workflow.md](optimizer-workflow.md) — full 3-turn workflow
