# How do I use Anny's crypto MCP tools without signing in?

You can run a subset of Anny Trade's MCP tools as a guest — no account, no API key, no OAuth.
Add the MCP URL to any MCP-compatible AI client and you immediately get read-only market
intelligence: technical analysis, CFO Anny Line states, asset comparisons, institutional flows,
and `ask_anny`. Guest access is rate-limited (5 requests/minute, 50/day) and excludes anything
that touches your portfolio or places orders. Sign in for higher limits and the full tool set.
The examples below all use guest-accessible tools, so they work with zero setup.

## Tools in This Section

All guest tools: `get_technical_analysis`, `get_anny_line_status`, `get_flip_intelligence`,
`compare_assets`, `get_institutional_intelligence`, `get_market_analysis`, `ask_anny`,
`get_trading_idea_detail`

## Prerequisites

- MCP URL added: `https://mcp.anny.trade/mcp`
- No PAT required
- Rate limit: 5 requests/minute, 50/day as guest

## Examples in This Folder

| File | What It Demonstrates |
|------|---------------------|
| [btc-technical-analysis.md](btc-technical-analysis.md) | RSI, MACD, ADX, EMA, volume indicators — zero setup |
| [market-overview.md](market-overview.md) | Cross-market analysis: BTC regime, S&P correlation, Fear & Greed |
| [compare-two-assets.md](compare-two-assets.md) | Head-to-head: CFO states, performance spread, fundamentals |
| [institutional-intelligence.md](institutional-intelligence.md) | ETF flows, corporate treasuries, whale activity |
| [cfo-line-flip-confidence.md](cfo-line-flip-confidence.md) | Confidence score for a recent state flip |

## Rate Limit Note

Guest users get 5 requests/minute and 50/day. Sign in for 10 requests/minute (FREE tier).
All examples in this folder use guest-accessible tools only.

## See Also

- [../02-market-intelligence/README.md](../02-market-intelligence/) — fuller market state once you connect an account
- [../05-cfo-line-backtest/README.md](../05-cfo-line-backtest/) — backtest the CFO Line you just explored as a guest
- [../03-portfolio-management/README.md](../03-portfolio-management/) — check balances and place orders after signing in
