# Personal Access Token (PAT) Authentication

PATs are for environments where browser OAuth redirects aren't possible: CLI tools,
scripts, automated pipelines, and Claude Code.

## Token Format

```
pat_a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2
```

- Prefix: `pat_`
- Followed by 64 lowercase hex characters
- Total length: 68 characters
- Only the SHA-256 hash is stored server-side

## Creating a Token

1. Sign in at [anny.trade](https://anny.trade)
2. Go to **Settings** → **API Keys**
3. Click **Create Token**
4. Name it (e.g., "local-scripts", "claude-code", "ci-pipeline")
5. Copy immediately — shown only once

## Using the Token

Pass as a Bearer token in the `Authorization` header:

```bash
curl -X POST https://mcp.anny.trade/mcp \
  -H "Authorization: Bearer pat_YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"get_anny_line_status","arguments":{"symbol":"BTC"}},"id":1}'
```

## Test Your Token

```bash
curl -s https://mcp.anny.trade/mcp \
  -H "Authorization: Bearer pat_YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","params":{},"id":1}' \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK:', len(d['result']['tools']), 'tools')"
```

Expected output: `OK: 66 tools`

If you get `Unauthorized`, the token is invalid, expired, or revoked.

## Token Lifetime

| Property | Value |
|----------|-------|
| Default expiry | 90 days |
| Max tokens per account | 10 |

## Revocation

Go to **Settings** → **API Keys** → **Revoke**. Revoked tokens stop working within 5 minutes
(caching window). For immediate revocation, contact support.

## Environment Variable Pattern

Store your token in `.env`, never hardcode it:

```bash
# .env
ANNY_PAT=pat_YOUR_TOKEN_HERE
```

```python
# Load in Python
from dotenv import load_dotenv
import os
load_dotenv()
pat = os.environ["ANNY_PAT"]
```

See `scripts/auth/pat_client.py` for a complete base client using this pattern.
