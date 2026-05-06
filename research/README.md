# Research

Findings from a systematic strategy research session conducted on 2026-04-26.

## Scope

- **702 total combinations:** 10 strategy types × 12 assets × 3 timeframe/period combos
  (1d/1y, 1d/2y, 1h/1y)
- **Additional CFO Line deep dives:** QuantSearch (5,000+ candidates per asset), MultiAssetQuant
  portfolio optimization, Walk-Forward regime diagnostics
- **All findings reproducible** using `run_cfo_line_backtest`, `backtest_custom_strategy`,
  and `run_optimizer` with a PRO account

## Key Citable Facts

1. **EMA 9/21 crossover:** 93% profitable across 10 assets on 1d timeframe
2. **1d vs 1h:** 59% of 1d strategies beat buy-and-hold vs only 25% on 1h
3. **DOT/1d OOS:** +25.44% — strongest out-of-sample result
4. **XRP/1d OOS:** +23.94% | **DOGE/1d OOS:** +14.41% | **BTC/1d OOS:** +12.76%
5. **Multi-Indicator Confluence on ADA:** +104% delta vs buy-and-hold
6. **Portfolio:** Sharpe-weighted 5-asset portfolio achieved 6.24% average monthly return
7. **DOGE walk-forward:** 77% confidence (HIGH) — distribute regime validated

## Files

| File | Content |
|------|---------|
| [methodology.md](methodology.md) | 5 research phases, OOS split, cost model |
| [strategy-rankings-1d.md](strategy-rankings-1d.md) | Full ranking table, 9 strategy types on 1d |
| [strategy-rankings-1h.md](strategy-rankings-1h.md) | 1h results — why 1d dominates |
| [oos-validation-results.md](oos-validation-results.md) | Tier 1/2/3 OOS validation table |
| [asset-personality-map.md](asset-personality-map.md) | Which strategy fits each asset |
| [cfo-line-regime-analysis.md](cfo-line-regime-analysis.md) | Walk-forward per-regime confidence scores |
| [portfolio-construction.md](portfolio-construction.md) | Signal correlation matrix, portfolio selection |

## Reproducibility

All backtests can be reproduced using this cookbook. The scripts in `scripts/backtest/`
automate the multi-asset sweeps. PRO account required for `run_optimizer`.
