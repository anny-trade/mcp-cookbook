# Anny MCP Cookbook

> EMA 9/21 crossover was profitable on 93% of assets tested. DOT out-of-sample: +25.44%.
> All results are reproducible with the tools in this repo.

Anny is a crypto portfolio intelligence platform with **66 tools** available over the
**Model Context Protocol (MCP)**. Connect your AI assistant — Claude, Cursor, or any
MCP-compatible client — and ask natural-language questions about Bitcoin, Ethereum, and
altcoin markets, run backtests on trading strategies, stress-test your portfolio, and
execute orders — all through plain English.

**MCP server endpoint:** `https://mcp.anny.trade/mcp`
**Auth:** OAuth 2.1 + PKCE (browser) or Personal Access Token (CLI / Claude Code)
**Exchanges:** Binance, Bybit, OKX, Kraken, KuCoin, Gate.io, MEXC, and 70+ more via CCXT

> **Disclaimer:** Examples and research in this repo are for educational purposes only.
> Nothing here is financial advice. Backtests are simulations — past performance does not
> predict future results. Full terms: [DISCLAIMER.md](DISCLAIMER.md)

> **CFO Anny Line** is Anny's proprietary trend-state indicator. It classifies any asset as
> Accumulate, Wait, or Distribute — and every flip event is timestamped and explainable.

---

## Is It Free?

**Yes, for most things.**

- 10 tools work with zero account — no signup, no API key, no credits
- All 56 non-backtest tools are free (0 credits) with any account tier
- The FREE tier (no card required) gives 1,000 credits/month for AI conversations
- Backtesting (`run_cfo_line_backtest`) and optimization (`run_optimizer`) require PRO ($19/mo)

See [docs/CREDIT_COSTS.md](docs/CREDIT_COSTS.md) for the full table.

---

## Quick Connect

### Zero setup — works right now (no account)

Paste this URL in your client's MCP settings:

```
https://mcp.anny.trade/mcp
```

Then try:

```
What's the CFO Line reading for Bitcoin right now?
```

You'll get Accumulate / Wait / Distribute state, recent flip events, and confidence score.
No login. No API key.

### Claude Desktop / Cursor

Add the URL under Settings → MCP Servers. On first authenticated use, a browser window opens for OAuth login.

### Claude Code (`~/.claude/settings.json`)

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

Get your PAT at [anny.trade](https://anny.trade) → Settings → API Keys.
Full setup guides: [setup/](setup/)

---

## 66 Tools at a Glance

| Category | Tools | Auth | Credits | Example Question |
|---|---|---|---|---|
| Technical Analysis | 5 | Guest OK | Free | Show me RSI and MACD for Ethereum on the 4h chart |
| CFO Anny Line | 3 | Guest OK | Free | Why did Bitcoin flip to Accumulate? Should I trust it? |
| Institutional Intelligence | 1 | Guest OK | Free | What are the latest Bitcoin ETF flows? |
| Market Intelligence | 4 | Required | Free | What's the Fear & Greed Index right now? |
| Tax & Holdings | 2 | Required | Free | Do I need to pay DARF this month? |
| Signal Management | 11 | Required | Free | Enable auto-buy for signal #12345 |
| Bot Management | 7 | Required | Free | How is my EMA crossover trading bot performing? |
| Community Signals | 3 | Required | Free | Show the P&L for my signal community |
| CFO Line Backtest | 2 | Required | 100 / 900 cr | Backtest CFO Line on DOT daily over 1 year |
| Custom Strategy Builder | 4 | Required | Free / 100 cr | Backtest RSI(14) < 30 + EMA(200) filter on BTC |
| Portfolio Management | 5 | Required | Free | Buy $200 of ETH — show me a preview first |
| Trading Ideas | 1 | Guest OK | Free | Tell me about the Bitcoin EMA crossover strategy |
| Support & Knowledge | 9 | Varies | Free | How do I connect my Binance API key? |

---

## Research Findings

Validated across 702 strategy/asset/variant combinations on real Binance data (12 assets,
multiple timeframe/period combos). All findings are reproducible using the tools in this
cookbook. Full methodology: [research/methodology.md](research/methodology.md)

- **EMA 9/21 crossover:** 93% profitability across 10 assets on 1d — most consistent strategy found
- **1d beats 1h significantly:** 59% of 1d strategies beat buy-and-hold vs only 25% on 1h
- **DOT/1d out-of-sample:** +25.44% on unseen test data — strongest single-asset OOS result
- **XRP/1d OOS:** +23.94% | **DOGE/1d OOS:** +14.41% | **BTC/1d OOS:** +12.76%
- **Multi-Indicator Confluence** (RSI + EMA + MACD aligned): +104% delta on ADA — highest alpha
- **Portfolio diversification:** 5-asset Sharpe-weighted portfolio achieved 6.24% avg monthly return (leveraged strategies, 3× average; 58% of months were negative — see [research/portfolio-construction.md](research/portfolio-construction.md))
- **DOGE walk-forward confidence:** 77% (HIGH) — distribute regime validated on unseen data

---

## Example Gallery

| Folder | What You Learn |
|---|---|
| [01-guest-no-auth](examples/01-guest-no-auth/) | Zero-setup examples — works in any MCP client without signing in |
| [02-market-intelligence](examples/02-market-intelligence/) | Fear & Greed, funding rates, ETF flows, cross-market correlations |
| [03-portfolio-management](examples/03-portfolio-management/) | Check balances, preview orders, execute buys/sells safely |
| [04-signal-management](examples/04-signal-management/) | List signals, toggle automation, update targets |
| [05-cfo-line-backtest](examples/05-cfo-line-backtest/) | CFO Anny Line performance across assets and timeframes |
| [06-custom-strategy-builder](examples/06-custom-strategy-builder/) | Build RSI, EMA, MACD algorithmic trading strategies and scan live conditions |
| [07-strategy-optimization](examples/07-strategy-optimization/) | Diagnose losing strategies, interpret loss categories |
| [08-risk-analytics](examples/08-risk-analytics/) | Portfolio stress tests: Bitcoin -40%, 2022-style crash, custom scenarios |
| [09-multi-turn-workflows](examples/09-multi-turn-workflows/) | Flagship: scan → backtest → optimize → deploy trading bot in one session |

---

## Credit Reference

### Free Tools (0 credits)

All 56 non-backtest tools are free:
`get_technical_analysis`, `get_anny_line_status`, `get_flip_intelligence`, `compare_assets`,
`get_institutional_intelligence`, `get_market_state`, `get_market_analysis`, `run_scenario`,
`get_exchange_balance`, `get_open_orders`, `check_symbol_availability`, `execute_market_order`,
`cancel_order`, `list_active_signals`, `toggle_auto_invest`, `scan_custom_signals`, and 40+ more.

### Paid Tools

| Tool | Credits | Min Tier | Notes |
|---|---|---|---|
| `run_cfo_line_backtest` | 100 | PRO | Per run |
| `backtest_custom_strategy` | Included in message cost | PRO | Billed as LLM usage |
| `run_optimizer` | 900 | PRO | Diagnoses + prescribes |
| `optimize_custom_strategy` | 900 | PRO | Same as optimizer |

Monthly allocations: FREE 1,000 cr · PRO $19 5,000 cr · PRO+ $49 50,000 cr

---

## Python Scripts

All scripts use only `requests` + `python-dotenv`. No Anthropic SDK dependency — they call the
MCP HTTP API directly.

| Script | What It Does | Run |
|---|---|---|
| `scripts/auth/pat_client.py` | Base HTTP client with retry + backoff | `python pat_client.py --test` |
| `scripts/backtest/cfo_line_multi_asset.py` | Multi-asset CFO Line backtest → ranked Sharpe table | `python cfo_line_multi_asset.py` |
| `scripts/backtest/custom_strategy_runner.py` | JSON strategy file → backtest + live scan | `python custom_strategy_runner.py --strategy ema_cross.json` |
| `scripts/market/technical_analysis_sweep.py` | Sweep assets → ranked TA table / CSV export | `python technical_analysis_sweep.py --assets BTC ETH SOL` |
| `scripts/market/market_state_monitor.py` | Poll + alert on Fear & Greed thresholds | `python market_state_monitor.py --alert-below 25` |
| `scripts/portfolio/balance_checker.py` | `get_exchange_balance` → formatted table | `python balance_checker.py` |
| `scripts/portfolio/order_manager.py` | List orders + cancel with `--confirm` guard | `python order_manager.py --cancel ORDER_ID --confirm` |

---

## Litmus Test

Run this to verify the MCP server is healthy before using Anny for important decisions:

```
Check if Anny's MCP tools are responding correctly: call get_anny_line_status for BTC,
then get_market_analysis, then get_technical_analysis for BTCUSDT on 1d.
Report which tools responded and what fields were present.
```

Pass/fail criteria and expected JSON schemas: [litmus/](litmus/)
Full health check guide: [docs/LITMUS_TEST.md](docs/LITMUS_TEST.md)

---

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for the required format.
Each example must include: Prompt, Tools Used, Auth Required, Credit Cost,
What Anny Returns, Expected Response Shape, Variations, and See Also.

Issues: [github.com/anny-trade/mcp-cookbook/issues](https://github.com/anny-trade/mcp-cookbook/issues)

---

## Get Started

- **Zero setup:** paste `https://mcp.anny.trade/mcp` in your MCP client and ask about Bitcoin
- **Guided:** follow [QUICKSTART.md](QUICKSTART.md) — live data in 2 minutes, first backtest in 10
- **Full reference:** [docs.anny.trade](https://docs.anny.trade)
- **Platform:** [anny.trade](https://anny.trade)
