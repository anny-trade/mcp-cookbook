# Litmus Test

The litmus suite checks structural conformance of MCP responses — not market values.

## What "Healthy" Looks Like

A healthy Anny MCP server:
- Returns valid JSON for all tool calls
- Includes all documented fields in responses (field presence contract)
- Completes guest tool calls in < 3 seconds
- Completes analysis calls in < 10 seconds
- Returns HTTP 200 for valid requests, 429 with `retryAfterMs` for rate limits, 401 for bad tokens

## How to Verify

**Quickest check (30 seconds):**

```
What's the CFO Line reading for BTC? Then give me the market analysis. Then show RSI for ETHUSDT on 1d.
Report all three results and flag any that were missing expected fields.
```

Expected: Three successful tool calls, each returning the fields in the schemas at `litmus/expected_responses/`.

**Full guest check:**
See [litmus/guest_tools_check.md](../litmus/guest_tools_check.md) — 5 checks, no auth.

**Auth tools check:**
See [litmus/auth_tools_check.md](../litmus/auth_tools_check.md) — 4 checks, requires PAT or OAuth.

## Failure Modes

| Symptom | Likely Cause |
|---------|-------------|
| HTTP 401 on all calls | PAT expired or revoked — create a new one |
| HTTP 401 on auth tools only | Guest token used for authenticated tools |
| HTTP 429 immediately | Rate limit exceeded — wait 60s and retry |
| Missing fields in response | Server version mismatch — check docs.anny.trade for updates |
| Tool not found error | Tool name mismatch — verify against tools.md |
| Empty response | Network error or server outage — retry once |

## Reporting Issues

If a litmus check fails and retrying doesn't help, open an issue with:
1. Which check failed
2. The exact prompt used
3. The response received (or error message)
4. Your auth method (OAuth / PAT / guest)

Issue template: [../.github/ISSUE_TEMPLATE/bug_report.md](../.github/ISSUE_TEMPLATE/bug_report.md)
