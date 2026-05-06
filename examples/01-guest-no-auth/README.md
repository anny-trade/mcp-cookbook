# Guest Examples — No Auth Required

These examples work in any MCP-compatible AI client without signing in or creating an account.
Zero setup required beyond adding the MCP URL.

## Tools in This Section

All guest tools: `get_technical_analysis`, `get_anny_line_status`, `get_flip_intelligence`,
`compare_assets`, `get_institutional_intelligence`, `get_market_analysis`, `ask_agent`,
`get_trading_idea_analysis`

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
