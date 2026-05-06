# CFO Line Backtest

The CFO Anny Line is a proprietary trend indicator based on smoothed moving average bands.
Each asset is always in one of three states: **Accumulate** (strength), **Wait** (neutral),
or **Distribute** (weakness). State transitions are the trade signals.

## Validated Research Findings

The research in this cookbook tested the CFO Line across 12 assets over multiple timeframes.
Key findings (all reproducible using `run_cfo_line_backtest` and `run_optimizer`):

| Asset | Timeframe | OOS Return | Verdict |
|-------|-----------|-----------|---------|
| DOT | 1d | +25.44% | Strong validation |
| XRP | 1d | +23.94% | Strong validation |
| DOGE | 1d | +14.41% | Strong validation |
| BTC | 1d | +12.76% | Strong validation |
| AVAX | 1d | +8.13% | Moderate validation |
| ETH | 1d | +6.85% | Moderate validation |
| LINK | 1h | +8.90% | Moderate validation |

OOS = out-of-sample test on the final 20% of the lookback period — data the strategy never
trained on.

**Key insight:** The 1d timeframe significantly outperforms 1h. On 1d, 59% of strategies beat
buy-and-hold. On 1h, only 25% do. Default to daily unless you have a specific reason for intraday.

## Cost

`run_cfo_line_backtest`: **100 credits** per run
`run_optimizer`: **900 credits** per run (PRO tier required)

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [btc-daily-backtest.md](btc-daily-backtest.md) | Full response shape documented, BTC/1d/1y |
| [eth-4h-backtest.md](eth-4h-backtest.md) | Non-default interval and period |
| [multi-asset-sweep.md](multi-asset-sweep.md) | DOT + XRP + DOGE — ties to OOS research |
| [long-vs-long-short-comparison.md](long-vs-long-short-comparison.md) | Compare modes on the same asset |
