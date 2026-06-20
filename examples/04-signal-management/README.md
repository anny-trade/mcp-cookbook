# How do I manage my crypto signals and automation in Anny?

A signal in Anny is a tracked trade idea — an asset, a direction, and entry, target, and
stop-loss prices. These tools let you list active signals and positions (`list_active_signals`),
inspect one in detail (`get_signal`), overlay the CFO Anny Line to check regime alignment
(`analyze_signal_with_cfo`), and control automation: `toggle_auto_invest`, `toggle_auto_stop`,
and `toggle_auto_sell` flip the flags that decide whether Anny enters, stops out, or takes
profit for you. `update_signal_target` edits the prices. The toggles and target updates are
database-only — they change settings, not live exchange orders.

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

## See Also

- [../03-portfolio-management/README.md](../03-portfolio-management/) — exchange-side balance checks and order placement
- [../05-cfo-line-backtest/README.md](../05-cfo-line-backtest/) — backtest the CFO Line behind `analyze_signal_with_cfo`
- [../09-multi-turn-workflows/README.md](../09-multi-turn-workflows/) — fold signals into a portfolio-review workflow

## DB-Only Note

`toggle_auto_invest`, `toggle_auto_stop`, `toggle_auto_sell`, and `update_signal_target` are
database-only operations. They update your Anny settings but do not place, modify, or cancel
any exchange orders. Use `cancel_pending_order` or `place_take_profit` for exchange-side actions.
