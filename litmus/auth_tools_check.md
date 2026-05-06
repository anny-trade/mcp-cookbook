# Auth Tools Litmus Check

4 checks requiring authentication. Connect with OAuth or PAT before running.

---

## Check 1: get_market_state

**Prompt:**
```
What's the current market state — Fear & Greed, funding rates, and ETF flows?
```

**Pass criteria:**
- `fearGreed.value` is a number between 0 and 100
- `fearGreed.classification` is one of the expected labels
- `derivatives.btcFundingRate8h` is a number
- `etfFlows.daily` is a number

**Fail signal:** `fearGreed` object missing, or `value` is null.

---

## Check 2: run_scenario

**Prompt:**
```
What happens to my portfolio if BTC drops 30%?
```

**Pass criteria:**
- `before.totalValue` is a number (may be 0 if no portfolio)
- `after.changePct` is a negative number
- `byAsset` is an array

**Fail signal:** `before` or `after` objects missing. Note: empty portfolio returns valid
structure with 0 values — this is a pass, not a fail.

---

## Check 3: run_cfo_line_backtest (optional — costs 100 credits)

**Note:** This check consumes 100 credits. Only run if you want to verify the backtest tool.

**Prompt:**
```
Backtest the CFO Line on BTC daily over the last 3 months.
```

**Pass criteria:**
- `performance.totalReturn` is a number
- `performance.tradeCount` is an integer ≥ 0
- `performance.sharpeRatio` is a number
- `oos.return` is a number

**Fail signal:** `performance` object missing, or `oos` object absent.

---

## Check 4: list_active_signals

**Prompt:**
```
List my active signals.
```

**Pass criteria:**
- `signals` is an array (may be empty — valid if account has no open signals)
- `total` is an integer ≥ 0
- If `signals` is non-empty: each item has `id`, `asset`, `direction`, `pnlPct`

**Fail signal:** Response is not an object, or `signals` field is absent.
