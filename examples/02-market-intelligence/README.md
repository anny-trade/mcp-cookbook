# How do I check current crypto market conditions with Anny?

Anny's market intelligence tools give you a real-time read on the whole market in one call.
`get_market_state` returns a comprehensive snapshot — Fear & Greed index, derivatives funding
rates, on-chain metrics like MVRV, and spot ETF flows. `get_market_analysis` adds the BTC regime
and cross-market correlations to the S&P 500 and Gold, and `get_institutional_intelligence`
breaks down ETF flows, corporate treasuries, and whale activity. Use these to ground any trade
or portfolio decision in current macro context rather than a single asset's chart in isolation.

## Auth Required

Yes — these tools require a connected account.

## Tools in This Section

- `get_market_state` — comprehensive snapshot including Fear & Greed, derivatives, on-chain
- `get_market_analysis` — BTC regime, S&P/Gold correlations (also available guest)
- `get_institutional_intelligence` — ETF flows, corporate treasuries (also available guest)

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [market-state-snapshot.md](market-state-snapshot.md) | Full market state: F&G, funding rates, ETF flows, MVRV |
| [cross-market-correlations.md](cross-market-correlations.md) | BTC vs S&P/Gold correlations with interpretation |
| [etf-flow-analysis.md](etf-flow-analysis.md) | Per-issuer 7d + YTD ETF flow breakdown |
| [fear-greed-context.md](fear-greed-context.md) | Multi-turn: current state → historical parallel |

## See Also

- [../01-guest-no-auth/README.md](../01-guest-no-auth/) — `get_market_analysis` and institutional intelligence are also guest-accessible
- [../08-risk-analytics/README.md](../08-risk-analytics/) — stress-test your portfolio against the conditions you just read
- [../09-multi-turn-workflows/README.md](../09-multi-turn-workflows/) — chain market state into a full morning briefing
