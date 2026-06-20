# Strategy Optimization

Diagnose why a strategy is losing money and get a prescription to fix it.

## What the Optimizer Does

The optimizer tests 10–15 filter combinations on your strategy and identifies which category
of losses is causing the most damage:

- **Whipsaw losses** — entered on a signal that immediately reversed
- **Weak conviction** — entered when trend strength was insufficient (low ADX, thin bands)
- **Counter-trend entries** — entered against the dominant regime (e.g., long in a downtrend)
- **Revenge trades** — entered too quickly after a loss (equity curve slope negative)

For each category, it prescribes a filter: confirmation candles, ATR multiplier, equity curve
SMA, or spread threshold.

## Cost

`optimize_strategy` and `optimize_strategy`: **900 credits** each | Requires PRO tier

## Free Pre-Scan

`prescan_custom_strategy` shows the loss pattern breakdown without revealing the prescription.
Use this (0 credits) to decide if optimization is worth 900 credits before paying.

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [diagnose-losing-strategy.md](diagnose-losing-strategy.md) | Run optimizer with loss category explanation |
| [optimizer-workflow.md](optimizer-workflow.md) | 3-turn: backtest → diagnose → validate |
| [interpret-loss-diagnosis.md](interpret-loss-diagnosis.md) | Educational: what each loss category means |
