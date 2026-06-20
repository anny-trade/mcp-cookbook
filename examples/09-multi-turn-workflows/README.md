# How do I chain Anny's MCP tools into an end-to-end workflow?

The real value of Anny's MCP comes from combining tools across several turns, where each step's
output feeds the next. This section documents three complete sessions: a research-to-deploy pipeline
(scan → backtest → optimize → deploy a live bot), a zero-credit morning briefing (market state →
CFO scans → signal review), and a monthly portfolio review (signals → scenario stress test →
synthesis). Each workflow lists the exact tools, turn count, and credit cost so you can reproduce it
in your own AI client. They assume a connected account; the deploy workflow also needs PRO tier for
the backtest and optimizer steps.

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

## See Also

- [../06-custom-strategy-builder/README.md](../06-custom-strategy-builder/) — build the strategies the deploy workflow validates
- [../07-strategy-optimization/README.md](../07-strategy-optimization/) — the diagnose step inside the research-to-deploy pipeline
- [../02-market-intelligence/README.md](../02-market-intelligence/) — the market-state call that opens the morning briefing
