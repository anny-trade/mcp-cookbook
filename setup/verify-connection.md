# Verify Your Connection

Three test prompts with expected response shapes. Run these after initial setup.

---

## Test 1: Guest Tool (No Auth Required)

**Prompt:**

```
What's the CFO Line reading for BTC?
```

**Tools used:** `get_anny_line_status`

**Expected response shape:**

```json
{
  "symbol": "BTC",
  "state": "...",
  "stateSince": "...",
  "recentFlips": [
    { "from": "...", "to": "...", "date": "..." }
  ],
  "bandValues": {
    "fast": 0.0,
    "slow": 0.0
  }
}
```

**Pass criteria:** `state` field is present and equals one of `Accumulate`, `Wait`, or `Distribute`.

---

## Test 2: Market Analysis (No Auth Required)

**Prompt:**

```
Give me a market overview — BTC regime, correlations with S&P and Gold, and Fear & Greed context.
```

**Tools used:** `get_market_analysis`

**Expected response shape:**

```json
{
  "btcRegime": "...",
  "correlations": {
    "btc_sp500_30d": 0.0,
    "btc_gold_30d": 0.0
  },
  "fearGreedStreak": "...",
  "btc30dRange": { "low": 0.0, "high": 0.0 },
  "totalMarketCap": "..."
}
```

**Pass criteria:** `btcRegime`, `correlations.btc_sp500_30d`, and `fearGreedStreak` are present.

---

## Test 3: Technical Analysis (No Auth Required)

**Prompt:**

```
Show me RSI, MACD, and EMA for BTCUSDT on the daily chart.
```

**Tools used:** `get_technical_analysis`

**Expected response shape:**

```json
{
  "symbol": "BTCUSDT",
  "timeframe": "1d",
  "momentum": {
    "rsi": { "value": 0.0, "signal": "..." },
    "macd": { "macd": 0.0, "signal": 0.0, "histogram": 0.0 },
    "adx": { "value": 0.0, "plus_di": 0.0, "minus_di": 0.0 }
  },
  "trend": {
    "ema20": 0.0,
    "ema50": 0.0,
    "ema200": 0.0
  },
  "volume": {
    "obv": "...",
    "vwap": 0.0
  }
}
```

**Pass criteria:** `momentum.rsi.value`, `trend.ema20`, and `trend.ema200` are present with non-zero values.

---

## Full Litmus Suite

For a comprehensive structural health check across all tool categories, see [../litmus/](../litmus/).
