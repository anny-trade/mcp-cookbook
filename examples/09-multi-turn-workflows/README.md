# Multi-Turn Workflows

End-to-end sessions that combine multiple tools in sequence. These are the most valuable
use cases — each step's output feeds the next.

## Prerequisites

- Connected account (OAuth or PAT)
- PRO tier for the deploy workflow (backtest + optimizer)
- Understanding of examples 01–08

## Workflows

| File | Turns | Tools | Credits | What You Get |
|------|-------|-------|---------|--------------|
| [research-to-deploy-workflow.md](research-to-deploy-workflow.md) | 6 | scan + backtest + optimize + deploy | ~1,100 | Validated live bot |
| [morning-briefing-workflow.md](morning-briefing-workflow.md) | 4 | market state + CFO scans + signals | 0 | Daily market ritual |
| [portfolio-review-workflow.md](portfolio-review-workflow.md) | 4 | signals + scenario + synthesis | 0 | Monthly review |

## Why Multi-Turn

Each tool is powerful alone. The alpha comes from combining them:

- **Scan → Backtest**: Only backtest strategies where conditions are close to firing
- **Backtest → Optimize**: Use backtest results to decide if 900 credits is worth spending
- **Optimize → Deploy**: Create a bot with validated settings, not default parameters
- **Market state → CFO + Signals**: Ground signal analysis in current macro conditions
