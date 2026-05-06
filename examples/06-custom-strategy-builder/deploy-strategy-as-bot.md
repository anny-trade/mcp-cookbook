# Deploy Strategy as Bot

The full pipeline: research → scan → backtest → optimize → deploy.

## Prompt Sequence

**Step 1 — Scan (free):**
```
Is EMA(9) above EMA(21) on BTC right now?
```

**Step 2 — Backtest:**
```
Backtest a BTC daily strategy: enter long when EMA(9) crosses above EMA(21),
3% stop-loss, 6% take-profit, 1 year of data.
```

**Step 3 — Deploy (after seeing good results):**
```
Deploy this strategy as a bot on Binance SPOT with $200 USDT per trade.
```

## Tools Used

- `scan_custom_signals` — free live check
- `backtest_custom_strategy` — validate historically
- `create_bot_from_strategy` — deploy as a live bot

## Auth Required

Yes

## Credit Cost

Scan: 0 · Backtest: included in message cost · Deploy: 0

## What Anny Returns

**Deploy step:** A new bot created in **paused** state. You receive the bot ID, title,
exchange, investment amount, and a link to activate it from the dashboard. The bot will
not trade until you activate it manually.

## Expected Response Shape (deploy)

```json
{
  "botId": "...",
  "title": "EMA 9/21 Crossover — BTC",
  "status": "paused",
  "exchange": "BINANCE",
  "account": "SPOT",
  "investment": 200.0,
  "quoteAsset": "USDT",
  "message": "Bot created in paused state. Activate from your dashboard when ready."
}
```

## Safety Note

Bots are always created paused. Anny does not auto-activate any bot. Review the bot config
in the dashboard before starting live trading.

## Variations

```
Deploy this strategy on Bybit instead.
```

```
Create the bot with $500 USDT per trade.
```

## See Also

- [scan-live-conditions.md](scan-live-conditions.md) — always scan before backtesting
- [ema-crossover-strategy.md](ema-crossover-strategy.md) — the strategy being deployed
- [examples/09-multi-turn-workflows/research-to-deploy-workflow.md](../09-multi-turn-workflows/research-to-deploy-workflow.md) — full end-to-end pipeline
