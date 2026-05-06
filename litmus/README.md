# Litmus Tests

Structural conformance checks for the Anny MCP server. These verify that expected fields
are present in responses — not that values are specific numbers (market values change daily).

## Philosophy

**Structural conformance, not value conformance.**

The check is "does `fearGreed.value` exist?" not "is Fear & Greed 42?". Market data changes
every minute. Field presence is the server contract.

Expected JSON files use `0.0` and `"..."` as placeholders. Any non-null value satisfies the check.

## Running the Checks

Paste the litmus prompts into your MCP-connected AI client. For each check, verify that
the fields listed in the expected response shape are present in the actual response.

For automated checking, use the Python scripts in `scripts/auth/pat_client.py` as a base
and call each tool with the parameters listed here.

## Files

| File | Checks | Auth Required |
|------|--------|---------------|
| [guest_tools_check.md](guest_tools_check.md) | 5 checks, no auth | No |
| [auth_tools_check.md](auth_tools_check.md) | 4 checks | Yes |
| `expected_responses/` | JSON schemas for 4 key tools | — |
