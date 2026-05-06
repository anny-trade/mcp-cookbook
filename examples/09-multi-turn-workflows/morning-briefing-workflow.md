# Morning Briefing Workflow

A 4-turn daily ritual: market conditions → CFO state check → signal review → decision.

## Total Credits: 0

---

## Turn 1: Market State

**Prompt:**
```
Morning briefing: what's the Fear & Greed, BTC funding rates, and ETF flow status?
```

**Tools:** `get_market_state`

**What to look for:** Funding rates above 0.05% per 8h → overleveraged longs (correction risk).
ETF net outflow streak > 3 days → institutional distribution. Fear & Greed < 20 → potential
bottom formation.

---

## Turn 2: CFO Line Status on Key Assets

**Prompt:**
```
What's the CFO Line state for BTC, ETH, and SOL right now? Any recent flips?
```

**Tools:** `get_anny_line_status` × 3

**What to look for:** All three in Distribute → broad market weakness, hold cash.
BTC Accumulate with ETH/SOL still in Wait → BTC leading, altcoin rotation may follow.

---

## Turn 3: Active Signals Review

**Prompt:**
```
List my active signals. Which are in profit? Which are close to stop-loss?
Highlight any that are in a CFO Distribute regime.
```

**Tools:** `list_active_signals`, `analyze_signal_with_cfo` (for signals near stop)

**What to look for:** Signals that are long in a Distribute regime are misaligned — consider
tightening the stop or disabling auto-invest.

---

## Turn 4: Decision

**Prompt:**
```
Based on market conditions and my signal positions, what's the risk environment today?
Should I be looking to add positions or reduce exposure?
```

**Tools:** Anny synthesizes from conversation context — no new tool call

**Output:** A concise risk assessment for the day based on all data gathered in turns 1–3.

---

## See Also

- [portfolio-review-workflow.md](portfolio-review-workflow.md) — monthly version with deeper analysis
- [research-to-deploy-workflow.md](research-to-deploy-workflow.md) — add new positions if conditions are right
