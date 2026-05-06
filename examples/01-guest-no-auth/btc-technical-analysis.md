# How do I get RSI, MACD, and ADX for Bitcoin with no account?

Get momentum, trend, and volume indicators for Bitcoin — no account required.

## Prompt

```
Show me the RSI, MACD, and EMA indicators for BTC on the daily chart.
```

## Tools Used

- `get_technical_analysis` — symbol: `BTCUSDT`, timeframe: `1d`

## Auth Required

No — guest access

## Credit Cost

0

## What Anny Returns

Momentum indicators (RSI 14, MACD 12/26/9, ADX 14 with DI+/DI-), trend indicators
(EMA 20, EMA 50, EMA 200), and volume indicators (OBV direction, VWAP, VROC, ADL,
volume trend classification).

RSI above 70 signals overbought conditions; below 30 signals oversold. MACD histogram
positive and rising indicates strengthening momentum. Price above EMA 200 is the standard
long-term trend filter — the research in this cookbook found it to be the most valuable
single confirmation filter for custom strategies.

## Expected Response Shape

```json
{
  "symbol": "BTCUSDT",
  "timeframe": "1d",
  "momentum": {
    "rsi": { "value": 0.0, "signal": "..." },
    "macd": { "macd": 0.0, "signal": 0.0, "histogram": 0.0, "trend": "..." },
    "adx": { "value": 0.0, "plus_di": 0.0, "minus_di": 0.0, "strength": "..." }
  },
  "trend": {
    "ema20": 0.0,
    "ema50": 0.0,
    "ema200": 0.0,
    "priceVsEma200": "..."
  },
  "volume": {
    "obv": "...",
    "vwap": 0.0,
    "vroc": 0.0,
    "volumeTrend": "..."
  }
}
```

## Variations

```
Is BTC overbought on the 4h chart?
```

```
Show me RSI and MACD for ETHUSDT on the 1h timeframe.
```

```
What do the volume indicators say about SOL on the daily chart?
```

## See Also

- [market-overview.md](market-overview.md) — broader market context
- [compare-two-assets.md](compare-two-assets.md) — side-by-side comparison
- [examples/05-cfo-line-backtest/btc-daily-backtest.md](../05-cfo-line-backtest/btc-daily-backtest.md) — backtest on these conditions
