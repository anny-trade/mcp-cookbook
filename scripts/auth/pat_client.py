"""
Base MCP HTTP client using Personal Access Token (PAT) authentication.
All other scripts inherit from or instantiate this client.

Usage:
    python auth/pat_client.py --test
"""

import os
import sys
import json
import time
import argparse
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

MCP_URL = os.environ.get("ANNY_MCP_URL", "https://mcp.anny.trade/mcp")
PAT = os.environ.get("ANNY_PAT", "")

MAX_RETRIES = 3
BACKOFF_BASE = 2.0  # seconds


class AnnyMCPClient:
    """Minimal MCP HTTP client with retry + exponential backoff."""

    def __init__(self, pat: str = PAT, url: str = MCP_URL):
        if not pat:
            raise ValueError("ANNY_PAT not set. Add it to your .env file.")
        self.pat = pat
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {pat}",
            "Content-Type": "application/json",
        })
        self._req_id = 0

    def _next_id(self) -> int:
        self._req_id += 1
        return self._req_id

    def call(self, tool: str, arguments: dict[str, Any] = None) -> dict:
        """
        Call an MCP tool and return the result dict.
        Raises RuntimeError on non-retryable errors.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {"name": tool, "arguments": arguments or {}},
            "id": self._next_id(),
        }

        last_error = None
        for attempt in range(MAX_RETRIES):
            try:
                resp = self.session.post(self.url, json=payload, timeout=60)

                if resp.status_code == 429:
                    retry_after = resp.json().get("retryAfterMs", 60000) / 1000
                    print(f"  Rate limited — waiting {retry_after:.0f}s", file=sys.stderr)
                    time.sleep(retry_after)
                    continue

                resp.raise_for_status()
                data = resp.json()

                if "error" in data:
                    raise RuntimeError(f"MCP error: {data['error']}")

                return data.get("result", data)

            except requests.exceptions.RequestException as e:
                last_error = e
                wait = BACKOFF_BASE ** attempt
                print(f"  Request failed (attempt {attempt+1}/{MAX_RETRIES}): {e} — retrying in {wait:.0f}s",
                      file=sys.stderr)
                time.sleep(wait)

        raise RuntimeError(f"Failed after {MAX_RETRIES} attempts: {last_error}")

    def list_tools(self) -> list[str]:
        """Return a list of available tool names."""
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/list",
            "params": {},
            "id": self._next_id(),
        }
        resp = self.session.post(self.url, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        tools = data.get("result", {}).get("tools", [])
        return [t["name"] for t in tools]


def main():
    parser = argparse.ArgumentParser(description="Anny MCP PAT client")
    parser.add_argument("--test", action="store_true", help="Run connection test")
    parser.add_argument("--list-tools", action="store_true", help="List all available tools")
    args = parser.parse_args()

    client = AnnyMCPClient()

    if args.list_tools:
        tools = client.list_tools()
        print(f"Available tools ({len(tools)}):")
        for t in sorted(tools):
            print(f"  {t}")
        return

    if args.test:
        print("Testing connection to Anny MCP...")
        tools = client.list_tools()
        print(f"OK: {len(tools)} tools available")

        print("\nTesting get_anny_line_status(BTC)...")
        result = client.call("get_anny_line_status", {"symbol": "BTC"})
        content = result.get("content", [{}])[0].get("text", "{}")
        data = json.loads(content) if isinstance(content, str) else content
        state = data.get("state", "unknown")
        print(f"OK: BTC CFO Line state = {state}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
