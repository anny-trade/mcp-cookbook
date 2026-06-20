# How do I go from strategy research to a live trading bot in one session?

The flagship workflow: scan live conditions → backtest → optimize → validate → deploy.
This is the pipeline used to generate the validated strategies in the research section.

## Total Credits: ~1,100 (PRO tier)

---

## Turn 1: Market Context

**Prompt:**
```
What's the current market regime and Fear & Greed? Is it a good environment to deploy a
new long-only strategy?
```

**Tools:** `get_market_state`, `get_market_analysis`
**Credits:** 0

**What you learn:** Whether macro conditions support a new long entry. High Fear & Greed
(>70) with BTC in a bullish regime = favorable. Extreme Fear + BTC below EMA(200) = wait.

---

## Turn 2: Live Scan

**Prompt:**
```
Scan BTC daily for EMA(9) above EMA(21), RSI above 50, and MACD histogram positive.
Are all three conditions met right now?
```

**Tools:** `scan_custom_signals`
**Credits:** 0

**What you learn:** If conditions are INACTIVE, the market isn't set up yet — adjust
thresholds or pick a different asset. If APPROACHING, the setup is forming.

---

## Turn 3: Backtest

**Prompt:**
```
Backtest the EMA 9/21 crossover on BTC daily with RSI > 50 and MACD histogram positive
as confirmations. 3% stop-loss, 6% take-profit, 1 year of data.
```

**Tools:** `backtest_custom_strategy`
**Credits:** ~100 (included in message cost)

**What you learn:** Win rate, Sharpe, max drawdown, and OOS validation. If OOS is positive
and Sharpe > 1.0, proceed to optimization.

---

## Turn 4: Diagnose (Free)

**Prompt:**
```
Show me the loss pattern breakdown for this strategy — what category of losses is largest?
Don't run the full optimizer yet.
```

**Tools:** `prescan_custom_strategy`
**Credits:** 0

**What you learn:** If whipsaw dominates (>40% of losses), confirmation candles will help.
If the improvement potential is LOW, optimization may not be worth 900 credits.

---

## Turn 5: Optimize (conditional — only if prescan shows HIGH potential)

**Prompt:**
```
Run the full optimizer on this strategy. Diagnose and prescribe the best filter settings.
```

**Tools:** `optimize_strategy`
**Credits:** 900

**What you learn:** Optimized Sharpe vs baseline. The prescription (specific filter values).
If optimized OOS return is positive, you have a validated strategy.

---

## Turn 6: Deploy

**Prompt:**
```
Deploy this strategy as a bot on Binance SPOT with $300 USDT per trade, using the
optimized settings.
```

**Tools:** `deploy_strategy_as_bot`
**Credits:** 0

**Result:** Bot created in paused state with your validated settings. Activate from
the dashboard when ready.

---

## See Also

- [morning-briefing-workflow.md](morning-briefing-workflow.md) — daily monitoring after deployment
- [research/oos-validation-results.md](../../research/oos-validation-results.md) — benchmarks to compare your results against
