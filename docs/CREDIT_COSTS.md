# Credit Costs

Authoritative credit cost table for all 66 Anny MCP tools.

## Monthly Credit Allocations

| Tier | Price | Monthly Credits |
|------|-------|----------------|
| FREE | $0 | 1,000 |
| PRO | $19 | 5,000 |
| PRO+ | $49 | 50,000 |

Additional credit packs: $1.99 (5k) · $4.99 (15k) · $9.99 (30k) · $19.99 (60k) · $39.99 (150k)

## Free Tools (0 credits)

All read-only and mutation tools are free:

**Technical Analysis (guest OK):**
`get_technical_analysis` · `get_anny_line_status` · `get_flip_intelligence` · `compare_assets` ·
`get_institutional_intelligence`

**Market Intelligence:**
`get_market_state` · `get_market_analysis` · `run_scenario` · `find_historical_pattern`

**Tax & Holdings:**
`get_tax_status` · `get_tax_holdings`

**Signal Management (all 11 tools):**
`get_signal` · `list_active_signals` · `get_signal_automation_config` · `analyze_signal_with_cfo` ·
`toggle_auto_invest` · `toggle_auto_stop` · `toggle_auto_sell` · `toggle_auto_trailing` ·
`update_signal_target` · `cancel_pending_order` · `place_take_profit` · `place_trailing_stop`

**Bot Management:**
`list_bots` · `get_bot_config` · `get_bot_fires` · `pause_bot` · `restart_bot` · `create_bot_from_strategy`

**Community:**
`list_communities` · `get_community_pnl` · `allocate_community_investment`

**Portfolio Management:**
`check_symbol_availability` · `get_exchange_balance` · `get_open_orders` · `execute_market_order` · `cancel_order`

**Trading Ideas:**
`get_trading_idea_analysis`

**Custom Strategy (scan is free; backtest is billed as LLM usage):**
`scan_custom_signals` · `prescan_custom_strategy`

**Support & Knowledge:**
`ask_agent` · `check_user_health` · `create_support_ticket` · `get_ticket_status` ·
`record_resolution_feedback` · `claim_welcome_bonus` · `get_exchange_setup_guide` ·
`log_skill_gap` · `submit_skill_request` · `submit_bug_report`

## Paid Tools

| Tool | Credits | Min Tier | Notes |
|------|---------|----------|-------|
| `run_cfo_line_backtest` | **100** | FREE | Per run |
| `backtest_custom_strategy` | Included in message cost | FREE | Billed as LLM usage (~100 cr equivalent) |
| `run_optimizer` | **900** | PRO | CFO Line optimizer |
| `optimize_custom_strategy` | **900** | PRO | Custom strategy optimizer |

## LLM-Billed Tools

Ask Anny conversations are billed based on actual token usage:

| Model | Approx Range | Production Average |
|-------|-------------|-------------------|
| Haiku | 80–200 credits | ~152 cr |
| Sonnet | 200–600 credits | ~414 cr |
| Opus | 1,000–3,000 credits | ~2,370 cr |

`backtest_custom_strategy` is included in the conversation message cost when called via chat.

## FREE Tier Limits

- 5 Ask Anny conversations per day (`ASKANNY_FREE_DAILY_LIMIT`)
- No backtesting (CFO Line or custom)
- No optimizer
- 1,000 credits/month for LLM usage

## Source of Truth

Credit costs are defined in `anny-lib-utils/src/config/pricing.config.js` in the Anny platform.
If this document disagrees with the live platform, the platform is correct.
