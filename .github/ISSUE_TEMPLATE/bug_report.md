---
name: Bug report
about: Report a broken tool, unexpected response shape, or litmus test failure
title: "[BUG] "
labels: bug
assignees: ''
---

## Litmus Check Failed

Which litmus check: [ ] guest_tools_check [ ] auth_tools_check [ ] specific tool: ___________

## Tool Name

<!-- Exact tool name from tools.md -->

## Prompt Used

```
(paste exact prompt here)
```

## Expected Behavior

<!-- Describe what you expected (refer to expected_responses/ JSON schemas) -->

## Actual Response

```json
(paste the actual response or error here)
```

## Auth Method

[ ] Guest (no auth)
[ ] Personal Access Token (PAT)
[ ] OAuth

## Client

[ ] Claude Desktop
[ ] Claude Code
[ ] Cursor
[ ] Custom client
[ ] Python script

## Environment

- Date/time of issue:
- MCP URL used:
