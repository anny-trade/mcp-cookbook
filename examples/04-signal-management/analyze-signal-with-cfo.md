# Analyze Signal with CFO Line

Overlay the CFO Anny Line on a signal's asset, using the signal's native timeframe.

## Prompt

```
Analyze signal #12345 with the CFO Line. Is the regime aligned with the signal direction?
```

## Tools Used

- `analyze_signal_with_cfo` — signal_id: `12345`

## Auth Required

Yes

## Credit Cost

0

## What Anny Returns

The signal details combined with the CFO Line reading for the signal's asset, using the
signal's configured timeframe. Returns whether the CFO regime (Accumulate / Wait / Distribute)
is aligned with the signal direction (long vs short), recent flips, and a summary assessment.

A long signal with the CFO Line in Accumulate state is regime-aligned — the indicator and
the signal agree. A long signal in Distribute state is a divergence — higher risk.

## Expected Response Shape

```json
{
  "signal": {
    "id": "...",
    "asset": "...",
    "direction": "...",
    "entryPrice": 0.0,
    "pnlPct": 0.0
  },
  "cfoLine": {
    "state": "...",
    "stateSince": "...",
    "aligned": true,
    "assessment": "..."
  }
}
```

## Variations

```
Is the CFO Line aligned with my BTC signal?
```

```
Check regime alignment for all my active signals.
```

## See Also

- [list-active-signals.md](list-active-signals.md) — get signal IDs first
- [examples/05-cfo-line-backtest/README.md](../05-cfo-line-backtest/README.md) — understand what CFO states mean
