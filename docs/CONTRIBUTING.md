# Contributing

## What Makes a Good Example

Each example `.md` file must lead with the natural-language question — not the tool name.
AI search engines index the question; the tool is secondary.

## Required Sections

Every example file must include these sections in order:

```markdown
## Prompt
(exact copy-pasteable query)

## Tools Used
(bulleted list of tool names and key parameters)

## Auth Required
(Yes / No — with tier note if PRO required)

## Credit Cost
(exact number, or "0", or "Included in message cost")

## What Anny Returns
(prose description of the response — not JSON, human-readable)

## Expected Response Shape
(JSON skeleton with 0.0 and "..." placeholders)

## Variations
(2–3 alternative phrasings of the same prompt)

## See Also
(cross-links to related examples)
```

## Tool Name Accuracy

All tool names must exactly match those in `anny-docs/docs/mcp/tools.md`. Never invent or
abbreviate tool names. If you're unsure, use the guest check in `litmus/guest_tools_check.md`
to verify the tool exists.

## Credit Costs

Credit costs must match `docs/CREDIT_COSTS.md`. Do not guess. If a tool cost is listed as
"Included in message cost", use that exact phrase.

## Prompt-First Principle

The `## Prompt` section must be a natural-language question a human would actually ask.
Not: "Call get_market_state with no parameters"
Yes: "What's the current Fear & Greed reading and how long has it been at this level?"

## Complexity Graduation

Folder numbers signal complexity. Contributions to `01-guest-no-auth/` must require no auth
and no credits. Contributions to `09-multi-turn-workflows/` should genuinely require multiple
sequential tool calls where each output feeds the next.

## Submitting

Open an issue using the [example request template](../.github/ISSUE_TEMPLATE/example_request.md)
before submitting a PR. This prevents duplicate work.
