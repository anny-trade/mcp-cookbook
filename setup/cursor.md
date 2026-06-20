# Cursor Setup

Connect Anny MCP to Cursor in under 2 minutes.

## Method 1: URL (Recommended)

1. Open Cursor
2. Go to **Settings** → **Features** → **MCP**
3. Click **Add new MCP server**
4. Set **Type** to `URL`
5. Paste: `https://mcp.anny.trade/mcp`
6. Click **Save**

On first use with an authenticated prompt, a browser window opens for OAuth login.

## Method 2: PAT (for Claude Code-style header auth)

If Cursor supports custom headers in your version:

```json
{
  "mcpServers": {
    "anny": {
      "type": "http",
      "url": "https://mcp.anny.trade/mcp",
      "headers": {
        "Authorization": "Bearer pat_YOUR_TOKEN_HERE"
      }
    }
  }
}
```

Get a PAT: [anny.trade](https://anny.trade) → Settings → API Keys → Create token.
PAT format and lifetime: [setup/pat-authentication.md](pat-authentication.md)

## Verify the Connection

Once Cursor shows the MCP server as connected, paste this into a new chat:

```
What's the CFO Line reading for BTC right now?
```

Expected: structured response with Accumulate / Wait / Distribute state.
Troubleshooting: [setup/verify-connection.md](verify-connection.md)

## Guest Tools (No Login Required)

45 read-only tools work without OAuth or PAT — useful for testing the connection. A few of them:

- `get_technical_analysis` — RSI, MACD, ADX for any symbol
- `get_anny_line_status` — CFO Line state + flips
- `get_flip_intelligence` — flip confidence scoring
- `compare_assets` — side-by-side TA comparison
- `get_institutional_intelligence` — ETF flows, whale activity
- `get_trading_idea_analysis` — strategy education

## See Also

- [claude-desktop.md](claude-desktop.md) — Claude Desktop setup
- [claude-code.md](claude-code.md) — Claude Code (`settings.json`) setup
- [verify-connection.md](verify-connection.md) — 3 test prompts with expected shapes
