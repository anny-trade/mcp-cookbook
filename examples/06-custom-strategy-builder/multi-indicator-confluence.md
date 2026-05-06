# Multi-Indicator Confluence

RSI + EMA trend + MACD histogram all aligned. The highest alpha strategy found in research
(+104% delta on ADA, +27% on BNB).

## Prompt

```
Backtest a confluence strategy on ADA daily: enter long when RSI(14) crosses above 50,
confirm price is above EMA(50), and MACD histogram is positive. Stop-loss 4%, take-profit 8%.
Last year of data.
```

## Tools Used

- `backtest_custom_strategy`

## Condition JSON

```json
{
  "name": "Multi-Indicator Confluence",
  "asset": "ADA",
  "interval": "1d",
  "direction": "long",
  "lookback_period": "1y",
  "trigger": {
    "indicator": "RSI",
    "params": { "period": 14 },
    "field": "value",
    "operator": "crosses_above",
    "compare_to": 50
  },
  "confirmations": [
    {
      "indicator": "PRICE",
      "field": "close",
      "operator": "above",
      "compare_to": {
        "indicator": "EMA",
        "params": { "period": 50 },
        "field": "value"
      }
    },
    {
      "indicator": "MACD",
      "params": { "fast": 12, "slow": 26, "signal": 9 },
      "field": "histogram",
      "operator": "above",
      "compare_to": 0
    }
  ],
  "stop_loss": { "type": "percent", "value": 4 },
  "take_profit": { "type": "percent", "value": 8 }
}
```

Note: Multiple confirmations require PRO tier (up to 2) or PRO+ (up to 4).

## Auth Required

Yes (PRO for confirmations)

## Credit Cost

Included in message cost

## Research Baseline

Multi-Indicator Confluence was the 2nd-ranked strategy type on 1d/1y:
- **ADA/1d:** +35.34% return, **+104.09% delta** vs B&H, 50% win rate, Sharpe 6.44, DD 8.22%
- **BNB/1d:** +38.15% return, +31.69% delta, 80% win rate, Sharpe 22.40, DD 4.96%

ADA's 104% delta is the highest single-asset alpha found in the entire 702-combination study.
The strategy works because ADA trends strongly but needs multiple confirmations to avoid
false signals in its volatile periods.

## Expected Response Shape

```json
{
  "name": "Multi-Indicator Confluence",
  "asset": "ADA",
  "performance": {
    "totalReturn": 0.0,
    "delta": 0.0,
    "winRate": 0.0,
    "profitFactor": 0.0,
    "sharpeRatio": 0.0,
    "maxDrawdown": 0.0,
    "tradeCount": 0
  },
  "oos": { "return": 0.0, "validated": true },
  "warnings": [],
  "signalStatus": "..."
}
```

## Variations

```
Use EMA(100) instead of EMA(50) for a stronger trend filter.
```

```
Add ADX > 25 as a fourth confirmation to only trade strong trends.
```

```
Test the same confluence on LINK and BNB.
```

## See Also

- [ema-crossover-strategy.md](ema-crossover-strategy.md) — simpler entry, lower confirmation overhead
- [research/strategy-rankings-1d.md](../../research/strategy-rankings-1d.md) — full strategy type rankings
- [research/asset-personality-map.md](../../research/asset-personality-map.md) — which strategies fit which assets
