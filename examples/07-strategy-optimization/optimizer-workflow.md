# Optimizer Workflow

3-turn workflow: backtest to see the problem → optimize to get the prescription →
validate to confirm the improvement is real.

## Turn 1: Baseline Backtest

### Prompt

```
Backtest the CFO Line on BTC daily over the last year — long mode only.
```

### Tools Used

- `run_cfo_line_backtest` — 100 credits

### What to Look For

- If total return < 10% and OOS return is negative: optimization may help
- If trade count < 5: strategy fires too rarely — optimization won't help much
- If win rate < 35%: likely a whipsaw problem — optimizer will target this

---

## Turn 2: Optimize

### Prompt

```
Optimize the CFO Line on BTC daily. Diagnose the losing trades and prescribe the best
filter settings.
```

### Tools Used

- `run_optimizer` — 900 credits (PRO required)

### What to Look For

- Significant improvement in Sharpe ratio (>0.5 increase) confirms the prescription is useful
- If optimized maxDrawdown increased: the filter over-concentrates into fewer, bigger trades
- Whipsaw as the dominant loss category → confirmation candles filter is most impactful
- Counter-trend as dominant → equity curve SMA filter will help most

---

## Turn 3: Validate the Improvement

### Prompt

```
Now run the CFO Line backtest again on BTC with these optimized settings — use 2 confirmation
candles and equityCurveSMA of 20. Show me the out-of-sample result.
```

### Tools Used

- `run_cfo_line_backtest` — 100 credits

### What to Look For

- OOS return positive: prescription validated on unseen data
- Improved Sharpe vs baseline: risk-adjusted return genuinely improved
- Trade count not reduced to 0: filters aren't too restrictive

---

## Total Cost

1,100 credits (100 + 900 + 100)

## See Also

- [diagnose-losing-strategy.md](diagnose-losing-strategy.md) — use prescan (free) before Step 2
- [research/oos-validation-results.md](../../research/oos-validation-results.md) — validation benchmarks from the overnight session
