# Setup

Choose the method that matches your environment.

## Decision Tree

```
Are you using Claude Desktop or Cursor?
  YES → claude-desktop.md or add the URL in your client's MCP panel
  NO

Are you using Claude Code (CLI)?
  YES → claude-code.md (PAT in Authorization header)
  NO

Are you building a custom client?
  YES → pat-authentication.md for PAT flow, oauth_client.py for full PKCE
```

## Connection URL

```
https://mcp.anny.trade/mcp
```

This is the primary endpoint. It supports both OAuth tokens and Personal Access Tokens.

## After Connecting

Run the verification prompts in [verify-connection.md](verify-connection.md) to confirm
the tools are responding correctly.

## Rate Limits

| Tier | Per Minute | Per Day |
|------|-----------|---------|
| Guest (no auth) | 5 | 50 |
| FREE | 10 | 200 |
| PRO | 30 | 1,000 |
| PRO+ | 60 | 5,000 |

Authenticated users get 2x the guest limit even on the FREE tier.
