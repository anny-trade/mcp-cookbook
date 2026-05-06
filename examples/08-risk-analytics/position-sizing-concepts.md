# How should I size positions to manage risk in a crypto portfolio?

Position sizing tools are on the roadmap. This file covers the concepts and how to use
current tools as a bridge.

## Current Capability (Available Now)

Use `run_scenario` in reverse: estimate how much of an asset you can hold such that a
worst-case scenario stays within your risk tolerance.

**Prompt example:**

```
I want to buy SOL but only risk $500 total if SOL drops 30%.
Check if my current USDT balance covers a $1,667 position.
```

This is manual position sizing: risk_amount / drop_pct = position_size → $500 / 0.30 = $1,667.

## Planned Tools (Roadmap)

The following tools are not yet available:

- `calculate_position_size` — Kelly criterion and fixed-fractional sizing based on win rate
  and R:R from your backtest results
- `calculate_stop_loss` — ATR-based stop levels and structure-based levels from recent S/R

These will be added as native MCP tools once the risk module ships.

## Research Context

The overnight research found that stop-loss / take-profit ratios matter more than entry
signal in most strategy types. Strategies with 5% SL / 10% TP (2:1 R:R) consistently
outperformed tighter 3%/6% across all strategy types tested. When position sizing tools
ship, they will be pre-populated with the validated R:R ratios from the research.

## See Also

- [portfolio-scenario-crash.md](portfolio-scenario-crash.md) — current stress test capability
- [examples/06-custom-strategy-builder/rsi-oversold-strategy.md](../06-custom-strategy-builder/rsi-oversold-strategy.md) — 2:1 R:R in practice
