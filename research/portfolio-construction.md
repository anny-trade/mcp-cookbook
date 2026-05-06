# Portfolio Construction

Building a diversified portfolio from CFO Line strategies using signal correlation filtering
and Sharpe-weighted allocation.

## Signal Correlation Matrix (1h, 10 assets)

```
       BTC   ETH   SOL   BNB   XRP   DOGE  ADA   AVAX  LINK  DOT
BTC    100   78%   75%   84%   77%   71%   70%   67%   74%   66%
ETH    78%   100   81%   75%   77%   77%   77%   76%   82%   71%
SOL    75%   81%   100   74%   77%   80%   78%   78%   80%   75%
BNB    84%   75%   74%   100   73%   71%   68%   68%   72%   67%
XRP    77%   77%   77%   73%   100   78%   77%   73%   77%   73%
DOGE   71%   77%   80%   71%   78%   100   83%   81%   82%   79%
ADA    70%   77%   78%   68%   77%   83%   100   82%   83%   82%
AVAX   67%   76%   78%   68%   73%   81%   82%   100   80%   77%
LINK   74%   82%   80%   72%   77%   82%   83%   80%   100   78%
DOT    66%   71%   75%   67%   73%   79%   82%   77%   78%   100
```

**Key diversification pairs:**
- BTC-DOT: 66% — lowest correlation, different regime response
- BNB-DOT: 67% — second lowest
- BTC-AVAX: 67% — third lowest
- Most altcoin pairs: 77–83% — limited diversification within alts

## Portfolio Selection

Correlation filter: reject pairs with >85% signal correlation. Select assets greedily by
descending Sharpe ratio.

**Selected 5-asset portfolio:** DOGE (8.24% avg mo), ADA (7.84%), ETH (6.15%), DOT (5.20%), AVAX (2.81%)

Note: This is the 3× leverage portfolio from MultiAssetQuant. All 5 assets are below 85%
pairwise correlation after filtering.

## Portfolio Performance (3× leveraged strategies, 1h)

| Allocation | Avg Monthly | Total Return | Max DD | Sharpe | Months ≥5% |
|------------|-------------|--------------|--------|--------|------------|
| Inverse-Vol | +6.22% | +60.33% | 29.03% | 0.91 | 5/12 |
| **Sharpe-Weighted** | **+6.24%** | +56.58% | 31.68% | 0.86 | 5/12 |
| Equal Weight | +6.05% | +52.90% | 32.50% | 0.84 | 5/12 |

**Target met:** Sharpe-weighted achieved 6.24% avg monthly. But: 58% of months were negative,
high monthly variance (25% std dev), and strategies use 3× leverage.

## Monthly Return Pattern

Strong months: Q2 2025 (April boom), Oct-Dec 2025.
Weak months: Q3 2025 (July–September brutal drawdowns), Feb–Mar 2026.

## Practical Considerations

1. The leveraged portfolio works in trending markets and struggles in choppy periods
2. Equal-weight is nearly as good as Sharpe-weighted (6.05% vs 6.24%) — simpler to maintain
3. Monthly rebalancing matters: without rebalancing, concentration drifts toward whichever
   asset is running
4. The DOGE-ADA pairing (83% correlation) is technically above threshold but both were kept
   because they have the highest individual alphas — a trade-off in this selection

## How to Reproduce

```
Backtest CFO Line on DOGE, ADA, ETH, DOT, and AVAX on the 1h chart.
Weight by Sharpe ratio. What's the average monthly return across all 5?
```

Credit cost: 5 × 100 = 500 credits
