# How does CFO Line perform on Ethereum 4h?

Non-default interval and period — 4-hour chart over 9 months.

## Prompt

```
How does the CFO Line perform on ETH using the 4-hour chart over the last 9 months?
```

## Tools Used

- `backtest_custom_strategy` — asset: `ETH`, interval: `4h`, period: `9m`, mode: `long`

## Auth Required

Yes

## Credit Cost

100 credits

## What Anny Returns

Same metrics as the daily backtest, but on the 4h interval. The 4h chart generates more
signals than daily (more flips between states) but with more noise. For ETH specifically,
the research showed that 1d validated with +6.85% OOS while 1h showed negative OOS results —
the 4h sits in between and is worth testing.

## Expected Response Shape

```json
{
  "asset": "ETH",
  "interval": "4h",
  "period": "9m",
  "mode": "long",
  "performance": {
    "totalReturn": 0.0,
    "buyHoldReturn": 0.0,
    "delta": 0.0,
    "winRate": 0.0,
    "profitFactor": 0.0,
    "sharpeRatio": 0.0,
    "maxDrawdown": 0.0,
    "tradeCount": 0
  },
  "oos": {
    "return": 0.0,
    "validated": true
  }
}
```

## Research Context

ETH at 1d/2y in the research showed MACD Momentum (8/21/5 settings) outperforming CFO Line
with +110% return and +150% delta over buy-and-hold. However, CFO Line's strength is its risk
management — lower drawdown (typically <10%) vs MACD's 16-17% drawdown on ETH.

If you primarily care about drawdown control, CFO Line wins. If you want raw return, test
custom MACD strategies using `backtest_custom_strategy`.

## Variations

```
Run CFO Line on ETH 4h in long_short mode.
```

```
Compare ETH performance on 1h vs 4h vs 1d.
```

## See Also

- [btc-daily-backtest.md](btc-daily-backtest.md) — daily reference for comparison
- [examples/06-custom-strategy-builder/ema-crossover-strategy.md](../06-custom-strategy-builder/ema-crossover-strategy.md) — EMA alternative for ETH
