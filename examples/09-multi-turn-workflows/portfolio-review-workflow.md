# How do I do a complete monthly crypto portfolio review with AI?

Monthly review: active signals → stress test → regime analysis → synthesis.

## Total Credits: 0

---

## Turn 1: Signal Inventory

**Prompt:**
```
List all my active signals. Group them by: profitable (P&L > 5%), at-risk (within 5%
of stop-loss), and neutral. How much total USDT is deployed?
```

**Tools:** `list_active_signals`

**What to look for:** Concentration risk (more than 30% in one asset). Signals that have been
open for >60 days without hitting any target — these are likely dead weight. Signals close to
stop-loss that also have CFO Line in Distribute.

---

## Turn 2: Stress Test

**Prompt:**
```
If BTC drops 30%, what does my portfolio look like? Show per-position impact.
```

**Tools:** `run_scenario` — scenario: `"BTC drops 30%"`

**What to look for:** Total portfolio drawdown above 40% suggests overexposure. Any single
position whose crash value drops below your original USDT allocation → unrealized loss becomes
realized loss if stop is hit during the crash.

---

## Turn 3: Regime Check

**Prompt:**
```
Check the CFO Line for all assets in my active signals. How many are in Accumulate vs
Distribute right now?
```

**Tools:** `analyze_signal_with_cfo` per signal (or `get_anny_line_status` per asset)

**What to look for:** If >60% of your open signals are in Distribute, your book is misaligned
with the current regime. This is a useful forward indicator — these positions are more likely
to hit stop-loss in the next 2–4 weeks.

---

## Turn 4: Synthesis

**Prompt:**
```
Based on this review: my signal inventory, the crash scenario results, and the CFO regime
alignment, give me a 3-point action plan for this month.
```

**Tools:** Synthesis from conversation context

**Output:** Concrete recommendations: which signals to tighten stops on, how much new capital
(if any) to deploy, and which assets to prioritize for the next strategy run.

---

## See Also

- [morning-briefing-workflow.md](morning-briefing-workflow.md) — daily version
- [examples/08-risk-analytics/multi-asset-stress-test.md](../08-risk-analytics/multi-asset-stress-test.md) — finer control over scenario inputs
