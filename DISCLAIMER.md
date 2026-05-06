# Disclaimer

## Not Financial Advice

This repository and everything in it — examples, prompts, research findings, strategy
rankings, backtest results, Python scripts, and all other content — is provided for
**informational and educational purposes only**. Nothing here constitutes financial advice,
investment advice, trading recommendations, or any solicitation to buy or sell any asset.

## Past Performance

Backtest results and research findings in this repository reflect simulated performance
on historical data. **Past performance is not indicative of future results.** A strategy
that performed well in backtesting may lose money when traded live.

Specific factors that make backtests unreliable as forward indicators:

- **Overfitting:** Strategies optimized on historical data often underperform on new data
- **Survivorship bias:** This research tests popular assets that still exist — many assets from the same period lost 90%+ or delisted
- **Market regime change:** A strategy validated in 2023–2026 may be unsuitable in different volatility or liquidity conditions
- **Execution gap:** Backtests assume fills at modeled prices; live fills may differ due to slippage, latency, and partial fills

## Live Trading Risk

The `execute_market_order` and related portfolio management tools **place real orders on your
connected exchange**. Crypto markets are volatile. You can lose your entire investment.

Before using any live trading tools:

- Understand what the order does before confirming it
- Start with small amounts you can afford to lose
- Verify the `MAX_CHAT_ORDER_USDT` cap set on your account
- Review the 2-step preview → confirm flow documented in [examples/03-portfolio-management/](examples/03-portfolio-management/)

## Strategy Research Findings

The research in [research/](research/) reflects one systematic session on 2026-04-26.
All leverage-adjusted results (e.g. the 6.24% avg monthly portfolio figure) used 2–3×
leverage. Returns presented without leverage are substantially lower. 58% of months in
the leveraged portfolio were negative.

The findings are published to enable reproducibility, not as trading recommendations.
Use them as a starting point for your own research, not as signals to act on directly.

## Jurisdiction

Cryptocurrency trading is regulated differently in different jurisdictions. It may be
restricted or prohibited in your country. It is your responsibility to understand and
comply with the laws that apply to you.

## No Warranty

This software and documentation is provided "as is" without warranty of any kind.
The authors and contributors are not liable for any financial losses incurred through
use of these tools, examples, or research findings.
