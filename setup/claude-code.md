# Claude Code Setup

Claude Code is a CLI tool that can't do browser OAuth redirects. Use a Personal Access Token (PAT)
instead.

## Step 1: Create a PAT

1. Go to [anny.trade](https://anny.trade) → **Settings** → **API Keys**
2. Click **Create Token**
3. Give it a name (e.g., "Claude Code")
4. Copy the token immediately — it's shown only once
5. Token format: `pat_` followed by 64 hex characters (68 chars total)

## Step 2: Add to Claude Code settings

Edit `~/.claude/settings.json`:

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

Replace `pat_YOUR_TOKEN_HERE` with your actual token.

## Step 3: Verify

Start a new Claude Code session and run:

```
What's the CFO Line reading for BTC?
```

## Using Project-Scoped Settings

For a per-project token (useful if you have multiple Anny accounts), add to
`.claude/settings.local.json` in the project directory instead of the global settings file.
This file should be in `.gitignore` — never commit PATs.

## Full Health Check

```
Call get_anny_line_status for BTC, then get_market_analysis, then
get_technical_analysis for BTCUSDT on the 1d timeframe.
Tell me which tools responded and summarize the key fields returned.
```

Expected: all three calls succeed, response includes state/band values, BTC regime,
and RSI/EMA/MACD indicators respectively.

## Token Security

- PATs are hashed server-side with SHA-256 — the plaintext is never stored
- Revoke at Settings → API Keys if compromised
- Max 10 active PATs per account
- Default expiry: 90 days
