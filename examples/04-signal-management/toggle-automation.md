# How do I enable or disable auto-invest on a trading signal?

Enable or disable auto-buy for a signal. DB-only — no exchange side-effect.

## Prompt

```
Enable auto-invest for signal #12345.
```

## Tools Used

- `toggle_auto_invest` — signal_id: `12345`, enabled: `true`

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

Confirmation of the new automation state. `toggle_auto_invest` is a database-only operation —
it updates the flag that controls whether the bot will automatically enter this signal on the
next trigger. No order is placed immediately, and toggling it never cancels or modifies anything
that is already on the exchange. The change takes effect from the next trigger evaluation, so an
entry that's already mid-flight is unaffected. The companion toggles behave the same way:
`toggle_auto_stop` controls automated stop-loss exits and `toggle_auto_sell` controls automated
take-profit exits, each flipping a setting rather than touching live orders. For exchange-side
actions, use `cancel_pending_order` or `place_take_profit` instead.

## Expected Response Shape

```json
{
  "signalId": "...",
  "autoInvest": true,
  "updated": true
}
```

## Other Automation Toggles

| Action | Tool | Effect |
|--------|------|--------|
| Enable auto-buy | `toggle_auto_invest` | Bot auto-enters the signal |
| Enable auto-stop | `toggle_auto_stop` | Bot auto-places stop-loss |
| Enable auto-sell | `toggle_auto_sell` | Bot auto-takes profit at targets |
| Enable trailing stop | `toggle_auto_trailing` | Bot uses trailing stop instead of fixed SL |

All four are DB-only — they configure what the bot does on the next trigger cycle.

## Variations

```
Disable auto-sell for signal #12345.
```

```
Turn on auto-stop for all my BTC signals.
```

## See Also

- [update-signal-targets.md](update-signal-targets.md) — change the prices automation acts on
- [list-active-signals.md](list-active-signals.md) — see current automation state
