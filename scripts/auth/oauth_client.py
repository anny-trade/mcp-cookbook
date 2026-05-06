"""
OAuth 2.1 + PKCE client for headless / server environments.
For most use cases, prefer pat_client.py — it's simpler.
Use this when you need to mint fresh OAuth tokens programmatically.

Usage:
    python auth/oauth_client.py --callback-port 8080
"""

import os
import sys
import json
import base64
import hashlib
import secrets
import argparse
import threading
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests
from dotenv import load_dotenv

load_dotenv()

AUTH_SERVER = os.environ.get("ANNY_AUTH_URL", "https://mcp.anny.trade")
CLIENT_ID = os.environ.get("ANNY_CLIENT_ID", "")  # optional — auto-registered if blank
SCOPES = "read:portfolio read:analysis ask:anny"


def _pkce_pair() -> tuple[str, str]:
    """Generate a PKCE code_verifier and code_challenge (S256)."""
    verifier = secrets.token_urlsafe(64)
    digest = hashlib.sha256(verifier.encode()).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
    return verifier, challenge


def _register_client(redirect_uri: str) -> str:
    """Dynamic client registration (RFC 7591). Returns client_id."""
    resp = requests.post(
        f"{AUTH_SERVER}/register",
        json={
            "client_name": "anny-mcp-cookbook",
            "redirect_uris": [redirect_uri],
            "grant_types": ["authorization_code"],
            "response_types": ["code"],
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()["client_id"]


class _CallbackHandler(BaseHTTPRequestHandler):
    """Minimal HTTP handler that captures the OAuth callback code."""

    code = None
    error = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = dict(urllib.parse.parse_qsl(parsed.query))
        _CallbackHandler.code = params.get("code")
        _CallbackHandler.error = params.get("error")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorization complete. Return to your terminal.")

    def log_message(self, *args):
        pass  # suppress access logs


def run_pkce_flow(port: int = 8080) -> dict:
    """
    Full PKCE authorization code flow.
    Opens the browser, starts a local callback server, exchanges code for tokens.
    Returns {"access_token": ..., "refresh_token": ...}
    """
    redirect_uri = f"http://localhost:{port}/callback"
    verifier, challenge = _pkce_pair()

    client_id = CLIENT_ID or _register_client(redirect_uri)
    print(f"Client ID: {client_id}")

    auth_url = (
        f"{AUTH_SERVER}/authorize"
        f"?response_type=code"
        f"&client_id={urllib.parse.quote(client_id)}"
        f"&redirect_uri={urllib.parse.quote(redirect_uri)}"
        f"&scope={urllib.parse.quote(SCOPES)}"
        f"&code_challenge={challenge}"
        f"&code_challenge_method=S256"
    )

    print(f"\nOpen this URL in your browser:\n{auth_url}\n")

    # Start callback server in background
    server = HTTPServer(("localhost", port), _CallbackHandler)
    thread = threading.Thread(target=server.handle_request)
    thread.start()
    thread.join(timeout=120)

    if _CallbackHandler.error:
        raise RuntimeError(f"OAuth error: {_CallbackHandler.error}")
    if not _CallbackHandler.code:
        raise RuntimeError("No authorization code received (timeout?)")

    # Exchange code for tokens
    resp = requests.post(
        f"{AUTH_SERVER}/token",
        json={
            "grant_type": "authorization_code",
            "code": _CallbackHandler.code,
            "code_verifier": verifier,
            "client_id": client_id,
            "redirect_uri": redirect_uri,
        },
        timeout=15,
    )
    resp.raise_for_status()
    tokens = resp.json()
    print("Tokens received successfully.")
    return tokens


def main():
    parser = argparse.ArgumentParser(description="Anny OAuth PKCE flow")
    parser.add_argument("--callback-port", type=int, default=8080,
                        help="Local port for OAuth callback (default: 8080)")
    args = parser.parse_args()

    tokens = run_pkce_flow(port=args.callback_port)
    print("\nAccess token (expires in 1 hour):")
    print(tokens.get("access_token", ""))
    print("\nRefresh token (expires in 30 days):")
    print(tokens.get("refresh_token", ""))


if __name__ == "__main__":
    main()
