# Claude Desktop Setup

Connect Anny to Claude Desktop using OAuth — no token management required.

## Steps

1. Open Claude Desktop
2. Go to **Settings** → **Integrations** (or **MCP** tab depending on version)
3. Click **Add Integration** or **+ Add MCP Server**
4. Enter:
   - **Name:** Anny
   - **URL:** `https://mcp.anny.trade/mcp`
5. Click **Save**
6. Claude will open a browser window for OAuth login
7. Sign in with your Anny account (Google, Apple, or email)
8. Return to Claude Desktop — the integration is now active

## Verify It Works

Type this in a new conversation:

```
What's the CFO Line reading for BTC?
```

Anny should respond with the current Accumulate / Wait / Distribute state and recent flip history.

For a full health check, see [verify-connection.md](verify-connection.md).

## Token Lifecycle

OAuth tokens issued via Claude Desktop:

| Token | Lifetime |
|-------|----------|
| Access token | 1 hour (auto-refreshed) |
| Refresh token | 30 days |

Claude Desktop handles token refresh automatically. If you see an auth error after 30 days,
re-authorize by removing and re-adding the integration.

## Scopes Requested

```
read:portfolio    — Access your portfolio positions and P&L
read:analysis     — Access indicator readings and scenario analysis
ask:anny          — Chat with Anny AI assistant
```

## Troubleshooting

**"Connection refused" or "Server not found"** — Check your network. The endpoint is
`https://mcp.anny.trade/mcp` (HTTPS, port 443).

**"Unauthorized"** — Re-authorize: remove the integration and add it again.

**Tools not appearing** — Restart Claude Desktop after adding the integration.
