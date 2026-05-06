# Scripts

Standalone Python scripts that call the Anny MCP API directly via PAT.
No Anthropic SDK dependency — these use `requests` and call the HTTP endpoint.

## Setup

```bash
cd scripts
pip install -r requirements.txt
cp ../.env.example .env   # then fill in ANNY_PAT
```

## .env

```
ANNY_PAT=pat_YOUR_TOKEN_HERE
ANNY_MCP_URL=https://mcp.anny.trade/mcp
```

## Scripts

| Script | Run | What It Does |
|--------|-----|--------------|
| `auth/pat_client.py` | `python auth/pat_client.py --test` | Base client, connection test |
| `auth/oauth_client.py` | `python auth/oauth_client.py` | PKCE flow for headless environments |
| `market/technical_analysis_sweep.py` | `python market/technical_analysis_sweep.py --assets BTC ETH SOL` | TA sweep → ranked table |
| `market/market_state_monitor.py` | `python market/market_state_monitor.py --alert-below 25` | Poll Fear & Greed |
| `backtest/cfo_line_multi_asset.py` | `python backtest/cfo_line_multi_asset.py` | Multi-asset backtest → Sharpe table |
| `backtest/custom_strategy_runner.py` | `python backtest/custom_strategy_runner.py --strategy ema_cross.json` | JSON strategy → backtest |
| `portfolio/balance_checker.py` | `python portfolio/balance_checker.py` | Exchange balances |
| `portfolio/order_manager.py` | `python portfolio/order_manager.py --cancel ORDER_ID --confirm` | Order list + cancel |
