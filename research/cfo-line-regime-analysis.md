# CFO Line Regime Analysis

Walk-forward analysis breaks the dataset into market regimes (Accumulate / Wait / Distribute)
and optimizes each regime separately, then validates on out-of-regime data.

## Confidence Scores

| Asset | TF | Confidence | Label | Validated Regime | Current Regime |
|-------|----|-----------|-------|-----------------|----------------|
| DOGE | 1d | **77%** | HIGH | Distribute | DISTRIBUTE |
| DOT | 1d | **67%** | MODERATE | Wait | DISTRIBUTE |
| XRP | 1d | **55%** | MODERATE | None | DISTRIBUTE |
| ETH | 1h | **55%** | MODERATE | None | WAIT |
| BTC | 1h | **43%** | LOW | None | WAIT |

## DOGE/1d — Highest Confidence (77%)

**Data:** 902 candles, 55 flips, 2023-11 to 2026-04

| Regime | Candles | Train Return | OOS Return | Validated? |
|--------|---------|-------------|------------|-----------|
| Accumulate | 224 | +61.28% | -30.74% | No |
| Wait | 497 | +149.90% | -32.39% | No |
| **Distribute** | 181 | -7.82% | **+0.50%** | **YES** |

Current regime is DISTRIBUTE — and the distribute filter is the validated one. The distribute
filter is conservative: conf=4, ATR=1.5×, equityCurveSMA=20. It doesn't try to profit in
distribution — it avoids losses. This is the correct approach for a bear market asset.

## DOT/1d — Moderate Confidence (67%)

**Data:** 902 candles, 56 flips

| Regime | Candles | Train Return | OOS Return | Validated? |
|--------|---------|-------------|------------|-----------|
| Accumulate | 171 | +7.26% | -27.28% | No |
| **Wait** | 234 | +26.83% | **+109.10%** | **YES** |
| Distribute | 497 | +75.10% | -28.06% | No |

Wait regime filter (conf=3, spread=0.8, SMA=50, equityCurveSMA=20) is extremely robust.
The standout 109% OOS return in the wait regime is driven by capturing regime transitions —
the wait regime is when the market is choosing direction, and DOT's transitions produce
outsized moves.

## XRP/1d — Moderate Confidence (55%)

All 3 regimes optimized but none validated. XRP's strong discovery result (+81.16%) works as
an aggregate across regimes but falls apart under per-regime optimization. The distribute
regime (184 candles, 7 flips) has insufficient trade density for meaningful optimization.

## BTC/1h — Low Confidence (43%)

BTC spends 96.5% of time in the WAIT regime on 1h (83.7% of all candles). Only 67 accumulate
candles and 242 distribute candles. Even the dominant wait regime failed OOS validation
(Train -17.54%, Test -8.44%).

**Conclusion:** BTC/1h is fundamentally unsuitable for CFO Line trading — the signal fires
too rarely. Use BTC on 1d (see [oos-validation-results.md](oos-validation-results.md) for
+12.76% OOS on 1d).

## Parameter Sensitivity Insights

Universal findings across all QuantSearch runs on 1h:

| Parameter | Optimal Range | Effect |
|-----------|--------------|--------|
| equityCurveSMA | 16–32 | Most impactful single filter (40–60% profit rate) |
| confirmationCandles | 2–3 | Reduces whipsaw; ETH prefers conf=8 |
| ATR period/multiplier | 8–14 / 1.5–2.5 | Marginal improvement; can be set to 0 |
| Mode | Asset-dependent | Bear assets: short; bull: long or long_short |
