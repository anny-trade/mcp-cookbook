# What do whipsaw, conviction loss, and counter-trend mean in strategy diagnosis?

What each loss category means and what to do about it.

## Loss Categories

### Whipsaw

**What it means:** The strategy entered on a valid signal that immediately reversed.
Price crossed the trigger level but had no follow-through — the market was choppy.

**Typical cause:** Entering in a low-ADX (low trend strength) environment, or during
consolidation after a volatile move.

**Prescription:** Confirmation candles (wait N bars after the signal before entering).
The research found equityCurveSMA=16-32 dramatically reduces whipsaw on 1h strategies.

---

### Weak Conviction

**What it means:** The signal fired but the underlying trend had insufficient momentum.
Trades entered but quickly hit stop-loss because there was no driving force.

**Typical cause:** Entering when ADX < 20, or when band gap is thin (for CFO Line).
**Prescription:** ADX filter (ADX > 20 or > 25 as confirmation), or ATR multiplier
(require minimum volatility for entry).

---

### Counter-Trend Entry

**What it means:** The strategy entered long in a downtrend, or short in an uptrend.
The indicator triggered but the broader regime was hostile.

**Typical cause:** No higher-timeframe trend filter. EMA(200) is the most effective single
counter-trend prevention filter found in the research.

**Prescription:** Equity curve SMA (skip entries when your own equity is falling —
the system is in a bad regime). Also: add EMA(200) confirmation to custom strategies.

---

### Revenge Trade

**What it means:** The strategy re-entered too quickly after a loss. Consecutive losses
cluster because the market is in a bad regime, not because of bad luck.

**Typical cause:** No cooldown after losses. The equity curve is falling but the system
keeps firing.

**Prescription:** Equity curve SMA (only enter when equity SMA is rising). This is
effectively a meta-filter: "is my own strategy in a good regime right now?"

---

## Parameter Reference

| Filter | Parameter | Research Default | Effect |
|--------|-----------|-----------------|--------|
| Confirmation candles | `confirmationCandles` | 2–3 | Wait N bars before entering |
| Equity curve SMA | `equityCurveSma` | 16–24 | Skip entry if equity below SMA |
| ATR multiplier | `atrMultiplier` | 1.5–2.5 | Require minimum volatility |
| Spread threshold | `spreadThreshold` | 0.5–1.5 | Require minimum band gap (CFO Line) |

## See Also

- [diagnose-losing-strategy.md](diagnose-losing-strategy.md) — run the optimizer to get these numbers
- [research/methodology.md](../../research/methodology.md) — how these categories were defined in the research
