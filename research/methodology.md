# Methodology

## Overview

The research session ran 5 phases over a single overnight session (2026-04-26), testing 702
strategy/asset/variant combinations across 12 assets.

**Assets tested:** BTC, ETH, SOL, BNB, XRP, DOGE, ADA, AVAX, LINK, DOT (+ MATIC skipped —
Binance renamed to POL)

---

## Phase 1: Strategy Discovery

**Tool:** `run_cfo_line_backtest` across 3 timeframe/period combos
**Scope:** 12 assets × 3 combos = 36 backtests
**OOS split:** Final 20% of each period held out as unseen validation data

Validation criteria:
- VALID: OOS return > 0
- CAUTION: OOS return negative but small (-5%) or very few trades (<3)
- INVALID: OOS return significantly negative or 0 trades in test period

---

## Phase 2: QuantSearch Deep Dives

**Tool:** `run_optimizer` (CFO Line variant testing)
**Scope:** 5,000+ candidate parameter combinations per asset on 1h
**Focus assets:** BTC, ETH, SOL, XRP, LINK

QuantSearch exhaustively tests confirmation candles (1–8), equity curve SMA (4–32), ATR
period/multiplier, and spread threshold combinations. Ranks by Sharpe-weighted profit rate
on holdout data.

---

## Phase 3: MultiAssetQuant Portfolio

**Scope:** 3,000 samples per asset across 10 assets on 1h with leverage
**Portfolio construction:** Correlation filter (<85% signal correlation), then Sharpe-weighted,
inverse-volatility, and equal-weight allocation

---

## Phase 4: Walk-Forward Regime Diagnostics

**Scope:** 5 assets (DOT, XRP, DOGE, BTC, ETH) with per-regime optimization
**Method:** Segment data by CFO Line regime (Accumulate / Wait / Distribute), optimize each
regime separately, validate on out-of-segment data

Confidence scoring formula:
- DOGE/1d: 77% (HIGH) — distribute regime validated
- DOT/1d: 67% (MODERATE) — wait regime validated
- XRP/1d: 55% (MODERATE) — no regime validated
- ETH/1h: 55% (MODERATE) — no regime validated
- BTC/1h: 43% (LOW) — signal fires too rarely on 1h

---

## Phase 5: Multi-Strategy Research (10 Types)

**Tool:** `backtest_custom_strategy` across 10 strategy types
**Scope:** 702 total combinations
**Comparison baseline:** Buy-and-hold return for each asset/period

### Strategy Types Tested

| # | Strategy | Signal Logic |
|---|----------|-------------|
| 1 | RSI Mean Reversion | RSI(7/14/21) cross below 30/25/20 |
| 2 | EMA Crossover | Fast EMA crosses above slow EMA |
| 3 | MACD Momentum | MACD histogram crosses zero |
| 4 | Bollinger Squeeze | BB bandwidth contracts, then breakout |
| 5 | ADX Trend Strength | ADX crosses 20/25/30 + DI direction |
| 6 | StochRSI Reversal | K/D crossover in extreme zones |
| 7 | Multi-Indicator Confluence | RSI + EMA trend + MACD aligned |
| 8 | Bollinger + RSI Combo | Price at BB band AND RSI extreme |
| 9 | ATR Volatility Breakout | Price moves >N×ATR with trend filter |
| 10 | CFO Anny Line | SMMA band state transitions |

---

## Transaction Cost Model

All backtests include:
- **Fee:** 0.1% per side (taker model)
- **Slippage:** 0.1% for major assets (BTC, ETH, SOL, BNB, XRP, ADA, DOGE, AVAX), 0.3% alts
- **Entry:** Next bar open (no look-ahead bias)
- **SL priority:** If stop-loss and take-profit hit in the same bar, stop-loss wins (pessimistic)
