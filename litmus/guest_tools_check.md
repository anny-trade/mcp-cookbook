# Guest Tools Litmus Check

5 checks requiring no authentication. Run these to verify the MCP server is healthy.

---

## Check 1: get_anny_line_status

**Prompt:**
```
What's the CFO Line state for BTC?
```

**Pass criteria:**
- `state` is present and is one of: `Accumulate`, `Wait`, `Distribute`
- `stateSince` is present (date string)
- `recentFlips` is an array (may be empty)

**Fail signal:** Response is empty, returns an error, or `state` field is missing.

---

## Check 2: get_technical_analysis

**Prompt:**
```
Show me RSI and MACD for ETHUSDT on the 1d chart.
```

**Pass criteria:**
- `momentum.rsi.value` is a non-zero number
- `trend.ema200` is a non-zero number
- `volume` object is present

**Fail signal:** `momentum` or `trend` fields missing, or RSI value is 0 or null.

---

## Check 3: get_market_analysis

**Prompt:**
```
Give me a market overview — BTC regime and correlations.
```

**Pass criteria:**
- `btcRegime` is present (string)
- `correlations.btc_sp500_30d` is present (number)
- `totalMarketCapUsd` is present

**Fail signal:** Any of the three fields absent.

---

## Check 4: compare_assets

**Prompt:**
```
Compare SOL vs ETH.
```

**Pass criteria:**
- `base.symbol` equals `SOL`
- `quote.symbol` equals `ETH`
- `ratioLine.state` is present
- `performanceSpread.7d` is a number

**Fail signal:** Either asset missing from response, or `ratioLine` absent.

---

## Check 5: get_institutional_intelligence

**Prompt:**
```
What are the latest Bitcoin ETF flows?
```

**Pass criteria:**
- `btcEtf.dailyFlow` is a number
- `btcEtf.byIssuer` is a non-empty array
- At least one issuer has `name`, `ticker`, and `7dFlow` fields

**Fail signal:** `btcEtf` missing or `byIssuer` is empty.
