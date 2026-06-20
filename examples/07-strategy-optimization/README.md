# How do I find out why my crypto strategy is losing money?

When a backtest shows losses, Anny's optimizer tells you why and prescribes a fix. It tests 10–15
filter combinations on your strategy and identifies which category of losses is doing the most
damage — whipsaws, weak conviction, counter-trend entries, or revenge trades — then prescribes a
concrete filter for each (confirmation candles, an ATR multiplier, an equity-curve SMA, or a
spread threshold). Run the free `prescan_custom_strategy` first (0 credits) to see the loss-pattern
breakdown, then spend 900 credits on `optimize_strategy` for the full prescription only if the
pre-scan shows a fixable pattern.

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

`optimize_strategy`: **900 credits** per run | Requires PRO tier

## Free Pre-Scan

`prescan_custom_strategy` shows the loss pattern breakdown without revealing the prescription.
Use this (0 credits) to decide if optimization is worth 900 credits before paying.

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [diagnose-losing-strategy.md](diagnose-losing-strategy.md) | Run optimizer with loss category explanation |
| [optimizer-workflow.md](optimizer-workflow.md) | 3-turn: backtest → diagnose → validate |
| [interpret-loss-diagnosis.md](interpret-loss-diagnosis.md) | Educational: what each loss category means |

## See Also

- [../06-custom-strategy-builder/README.md](../06-custom-strategy-builder/) — build the strategy you're optimizing
- [../05-cfo-line-backtest/README.md](../05-cfo-line-backtest/) — backtest before deciding to optimize
- [../09-multi-turn-workflows/README.md](../09-multi-turn-workflows/) — backtest → diagnose → validate → deploy end-to-end
