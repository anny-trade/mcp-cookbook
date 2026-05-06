# Quickstart

Live Bitcoin data in 2 minutes. First backtest in 10.

---

## Step 1 — Connect (2 minutes)

### Option A: No account (works right now)

In Claude Desktop, Cursor, or any MCP-compatible client, add this URL:

```
https://mcp.anny.trade/mcp
```

Then paste:

```
What's the CFO Line reading for Bitcoin?
```

You'll get Accumulate / Wait / Distribute state and recent flip events immediately.
No login. No credits consumed.

### Option B: Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "anny": {
      "type": "http",
      "url": "https://mcp.anny.trade/mcp",
      "headers": {
        "Authorization": "Bearer pat_YOUR_TOKEN_HERE"
      }
    }
  }
}
```

Get a PAT: [anny.trade](https://anny.trade) → Settings → API Keys → Create token.

---

## Step 2 — Verify It Works (30 seconds)

```
Call get_anny_line_status for BTC, get_market_analysis, and get_technical_analysis
for BTCUSDT on 1d. Report all three results and flag any missing fields.
```

Expected: three structured responses with no errors. If anything looks wrong,
see [docs/LITMUS_TEST.md](docs/LITMUS_TEST.md).

---

## Step 3 — Live Market Intelligence (2 minutes)

```
What's the current Fear & Greed reading, Bitcoin ETF flows today,
and how is BTC correlating with the S&P 500?
```

This calls `get_market_state` + `get_institutional_intelligence` + `get_market_analysis`.
All free, auth required for the first two.

---

## Step 4 — Technical Analysis on Any Asset (2 minutes)

```
Show me RSI, MACD, and ADX for ETHUSDT on the 4h chart.
What's the trend signal and is there momentum confirmation?
```

Uses `get_technical_analysis`. Guest-accessible, 0 credits.

---

## Step 5 — Your First Backtest (10 minutes, PRO required)

```
Backtest the CFO Line on DOT daily over 1 year.
Show me the in-sample return, out-of-sample return, Sharpe ratio, and win rate.
```

- Costs **100 credits** per run
- Requires PRO tier ($19/mo, 5,000 credits included)
- Expected result: in-sample +303%, OOS +25.44% (as of 2026-04 research)
- Full guide: [examples/05-cfo-line-backtest/btc-daily-backtest.md](examples/05-cfo-line-backtest/btc-daily-backtest.md)

---

## Step 6 — Custom Strategy Backtest (10 minutes, PRO required)

```
Build an EMA crossover strategy: fast EMA 9, slow EMA 21, stop-loss 3%, take-profit 6%.
Backtest it on Bitcoin daily over 1 year.
```

Uses `backtest_custom_strategy`. Included in message cost (LLM billing).
Full guide: [examples/06-custom-strategy-builder/ema-crossover-strategy.md](examples/06-custom-strategy-builder/ema-crossover-strategy.md)

---

## Step 7 — Portfolio Check (requires connected exchange)

```
Show me my current balances across all exchanges.
What positions do I have open right now?
```

Uses `get_exchange_balance` + `get_open_orders`. Free, requires OAuth or PAT.
Safety guide: [examples/03-portfolio-management/](examples/03-portfolio-management/)

---

## Where to Go Next

| Goal | Start Here |
|------|-----------|
| Understand all 66 tools | [anny-docs/docs/mcp/tools.md](https://docs.anny.trade) |
| See what the research found | [research/](research/) |
| Run multi-step workflows | [examples/09-multi-turn-workflows/](examples/09-multi-turn-workflows/) |
| Automate with Python | [scripts/](scripts/) |
| Debug a broken response | [docs/LITMUS_TEST.md](docs/LITMUS_TEST.md) |
