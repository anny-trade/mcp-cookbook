# What are the current crypto market conditions and sentiment?

A single call that covers Fear & Greed, funding rates, ETF flows, and on-chain metrics.

## Prompt

```
What's the current state of the crypto market? Give me Fear & Greed, funding rates,
BTC ETF flows, and on-chain signals.
```

## Tools Used

- `get_market_state` — no parameters

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

Fear & Greed Index (0–100 with classification: Extreme Fear / Fear / Neutral / Greed /
Extreme Greed), risk summary (market risk, on-chain risk, macro risk scores), BTC overview
(price, RSI 14, EMA 20/50/200, dominance, golden/death cross status), derivatives data
(BTC and ETH 8-hour funding rates and annualised, 24-hour liquidations), Bitcoin ETF flows
(daily, 7-day net, streak), and on-chain metrics (MVRV Z-Score, NUPL, Coinbase Premium,
exchange netflow).

## Expected Response Shape

```json
{
  "fearGreed": { "value": 0, "classification": "..." },
  "risk": { "market": 0, "onChain": 0, "macro": 0 },
  "btc": {
    "price": 0.0,
    "rsi14": 0.0,
    "ema20": 0.0,
    "ema50": 0.0,
    "ema200": 0.0,
    "dominance": 0.0,
    "signal": "..."
  },
  "derivatives": {
    "btcFundingRate8h": 0.0,
    "btcFundingRateAnnualized": 0.0,
    "ethFundingRate8h": 0.0,
    "liquidations24h": "..."
  },
  "etfFlows": {
    "daily": 0.0,
    "7dNet": 0.0,
    "streak": "..."
  },
  "onChain": {
    "mvrvZScore": 0.0,
    "nupl": 0.0,
    "coinbasePremium": 0.0,
    "exchangeNetflow": "..."
  }
}
```

## Variations

```
Are funding rates elevated right now?
```

```
Is the market overheated? Check MVRV and NUPL.
```

```
What's the Coinbase Premium doing?
```

## See Also

- [fear-greed-context.md](fear-greed-context.md) — historical pattern matching for current F&G reading
- [etf-flow-analysis.md](etf-flow-analysis.md) — per-issuer ETF breakdown
