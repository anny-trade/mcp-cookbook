"""
Check exchange balances across all connected exchanges.

Usage:
    python portfolio/balance_checker.py
    python portfolio/balance_checker.py --asset USDT
    python portfolio/balance_checker.py --exchange BINANCE
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from auth.pat_client import AnnyMCPClient


def get_balances(client: AnnyMCPClient, asset: str = None, exchange: str = None) -> dict:
    params = {}
    if asset:
        params["asset"] = asset
    if exchange:
        params["exchangeCode"] = exchange
    result = client.call("get_exchange_balance", params)
    content = result.get("content", [{}])[0].get("text", "{}")
    return json.loads(content) if isinstance(content, str) else content


def print_balances(data: dict):
    balances = data.get("balances", [])
    if not balances:
        print("No balances found.")
        return

    header = f"{'EXCHANGE':<12} {'ASSET':<8} {'FREE':>12} {'LOCKED':>12} {'TOTAL':>12}"
    print("\n" + header)
    print("-" * len(header))

    total_usdt = 0
    for b in sorted(balances, key=lambda x: x.get("total", 0), reverse=True):
        free = b.get("free", 0)
        locked = b.get("locked", 0)
        total = b.get("total", 0)
        print(
            f"{b.get('exchange', ''):<12} {b.get('asset', ''):<8} "
            f"{free:>12.4f} {locked:>12.4f} {total:>12.4f}"
        )

    total_free_usdt = data.get("totalFreeUsdt", 0)
    if total_free_usdt:
        print(f"\nTotal free USDT equivalent: ${total_free_usdt:,.2f}")


def main():
    parser = argparse.ArgumentParser(description="Exchange balance checker")
    parser.add_argument("--asset", help="Filter to a specific asset (e.g., USDT, BTC)")
    parser.add_argument("--exchange", help="Filter to a specific exchange (e.g., BINANCE)")
    args = parser.parse_args()

    client = AnnyMCPClient()
    print("Fetching exchange balances...")
    data = get_balances(client, args.asset, args.exchange)
    print_balances(data)


if __name__ == "__main__":
    main()
