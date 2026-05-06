# Signal Management

List signals, check automation state, toggle auto-invest, and update targets.

## Auth Required

Yes

## Tools in This Section

- `list_active_signals` — list all active signals and positions
- `get_signal` — detailed view of a specific signal
- `get_signal_automation_config` — full automation config for a signal
- `analyze_signal_with_cfo` — overlay CFO Line on a signal's asset
- `toggle_auto_invest` — enable/disable auto-buy (DB-only, no exchange side-effect)
- `toggle_auto_stop` — enable/disable stop-loss automation
- `toggle_auto_sell` — enable/disable take-profit automation
- `update_signal_target` — update target, stop-loss, or entry prices

## Examples

| File | What It Demonstrates |
|------|---------------------|
| [list-active-signals.md](list-active-signals.md) | List all positions with P&L and automation state |
| [analyze-signal-with-cfo.md](analyze-signal-with-cfo.md) | CFO regime analysis on a signal's asset |
| [toggle-automation.md](toggle-automation.md) | Enable/disable auto-buy for a specific signal |
| [update-signal-targets.md](update-signal-targets.md) | Update target and stop-loss prices |

## DB-Only Note

`toggle_auto_invest`, `toggle_auto_stop`, `toggle_auto_sell`, and `update_signal_target` are
database-only operations. They update your Anny settings but do not place, modify, or cancel
any exchange orders. Use `cancel_pending_order` or `place_take_profit` for exchange-side actions.
