# Asset Personality Map

Each asset has a distinct strategy profile. No single strategy type dominates across all assets.
Use this map to choose the right starting strategy when setting up backtests.

## Large Caps — Trend-Following

**BTC and ETH** prefer momentum strategies. Their deep liquidity means trend signals have
genuine follow-through. Mean-reversion strategies underperform because BTC trends for weeks
at a time before reversing.

| Asset | Best Strategy | Runner-Up | Avoid |
|-------|--------------|-----------|-------|
| BTC | EMA Crossover (9/21) | ADX Trend | Bollinger strategies |
| ETH | EMA Crossover (12/26) | MACD Momentum | RSI Mean Reversion |

## Mid Caps — Confirmation-Heavy

**BNB and DOGE** need multiple confirmations to filter the noise. Single-indicator strategies
generate too many false signals. ADX filters out the low-conviction entries that dominate BNB.

| Asset | Best Strategy | Runner-Up | Avoid |
|-------|--------------|-----------|-------|
| BNB | ADX Trend Strength | Multi-Indicator Confluence | Pure RSI |
| DOGE | ADX Trend Strength | StochRSI Reversal | Bollinger Squeeze |

## Volatile Alts — Mean Reversion / Reversal

**XRP and DOGE** (particularly on longer lookbacks) benefit from reversal strategies. Their
high volatility creates extreme swings that mean-revert predictably. XRP's reversal alpha
(+93.79% delta) is the second-highest single result found.

| Asset | Best Strategy | Insight |
|-------|--------------|---------|
| XRP | StochRSI Reversal | Volatile enough for quick reversals; poor trend-follower |
| DOGE | StochRSI / ADX | Works as either reversal or trend depending on regime |

## Bear Market Performers — Confluence

**ADA, DOT, and LINK** performed best with confluence strategies requiring multiple
confirmations. These assets spend extended time in downtrends — single-indicator strategies
generate too many counter-trend longs.

| Asset | Best Strategy | Research Note |
|-------|--------------|--------------|
| ADA | Multi-Indicator Confluence | +104% delta — highest alpha in the entire study |
| DOT | RSI Mean Reversion / CFO Line | Most consistent across all timeframes |
| LINK | CFO Anny Line | CFO Line is uniquely effective for LINK (ranks #1) |

## Problematic Assets

**SOL and AVAX** showed inconsistent results across timeframes and strategy types. SOL spent
most of 1h in a heavy downtrend (-41.84% B&H), making long strategies unreliable. AVAX was
the only asset where the short-mode CFO strategy worked well in the QuantSearch deep dive.

**XRP on 2y data:** No strategy achieved positive risk-adjusted delta over the full
bear+bull cycle on 2 years of data — XRP is genuinely un-tradeable with systematic strategies
over longer periods.

## Quick Reference

| Asset | Personality | Primary Strategy |
|-------|------------|-----------------|
| BTC | Trend | EMA Crossover |
| ETH | Trend | EMA Crossover / MACD |
| SOL | Short-bias / volatile | ATR Breakout (1d only) |
| BNB | Confirmation-heavy | ADX Trend |
| XRP | Reversal | StochRSI |
| DOGE | Trend + Reversal | ADX Trend |
| ADA | Confluence | Multi-Indicator |
| AVAX | Mixed | EMA Crossover |
| LINK | CFO-aligned | CFO Anny Line |
| DOT | Consistent across types | RSI Mean Rev / CFO Line |
