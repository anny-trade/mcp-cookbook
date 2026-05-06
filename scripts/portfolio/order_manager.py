"""
List and cancel open orders. Requires explicit --confirm flag for cancellations.

Usage:
    python portfolio/order_manager.py                        # list all open orders
    python portfolio/order_manager.py --symbol BTC/USDT     # filter by symbol
    python portfolio/order_manager.py --cancel ORDER_ID --symbol BTC/USDT --confirm
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from auth.pat_client import AnnyMCPClient


def get_open_orders(client: AnnyMCPClient, symbol: str = None, exchange: str = None) -> dict:
    params = {}
    if symbol:
        params["symbol"] = symbol
    if exchange:
        params["exchangeCode"] = exchange
    result = client.call("get_open_orders", params)
    content = result.get("content", [{}])[0].get("text", "{}")
    return json.loads(content) if isinstance(content, str) else content


def cancel_order(client: AnnyMCPClient, order_id: str, symbol: str, exchange: str = None) -> dict:
    params = {"orderId": order_id, "symbol": symbol}
    if exchange:
        params["exchangeCode"] = exchange
    result = client.call("cancel_order", params)
    content = result.get("content", [{}])[0].get("text", "{}")
    return json.loads(content) if isinstance(content, str) else content


def print_orders(data: dict):
    orders = data.get("orders", [])
    total = data.get("total", len(orders))

    if not orders:
        print("No open orders.")
        return

    print(f"\nOpen orders ({total}):\n")
    header = f"{'ORDER_ID':<20} {'EXCHANGE':<10} {'SYMBOL':<12} {'SIDE':<6} {'TYPE':<18} {'QTY':>10} {'PRICE':>12}"
    print(header)
    print("-" * len(header))

    for o in orders:
        print(
            f"{o.get('orderId', ''):<20} "
            f"{o.get('exchange', ''):<10} "
            f"{o.get('symbol', ''):<12} "
            f"{o.get('side', ''):<6} "
            f"{o.get('type', ''):<18} "
            f"{o.get('qty', 0):>10.4f} "
            f"{o.get('price', 0):>12.4f}"
        )


def main():
    parser = argparse.ArgumentParser(description="Open order manager")
    parser.add_argument("--symbol", help="Filter by trading pair (e.g., BTC/USDT)")
    parser.add_argument("--exchange", help="Filter by exchange (e.g., BINANCE)")
    parser.add_argument("--cancel", metavar="ORDER_ID",
                        help="Order ID to cancel (requires --confirm)")
    parser.add_argument("--confirm", action="store_true",
                        help="Required to actually execute a cancellation")
    args = parser.parse_args()

    client = AnnyMCPClient()

    if args.cancel:
        if not args.confirm:
            print("ERROR: --confirm flag required to cancel an order.")
            print(f"       Run again with --cancel {args.cancel} --confirm to proceed.")
            sys.exit(1)
        if not args.symbol:
            print("ERROR: --symbol required for cancellation (e.g., --symbol BTC/USDT)")
            sys.exit(1)

        print(f"Cancelling order {args.cancel} for {args.symbol}...")
        result = cancel_order(client, args.cancel, args.symbol, args.exchange)
        if result.get("cancelled"):
            print(f"OK: Order {result.get('orderId')} cancelled at {result.get('cancelledAt')}")
        else:
            print(f"Failed: {result}")
        return

    # Default: list open orders
    print("Fetching open orders...")
    data = get_open_orders(client, args.symbol, args.exchange)
    print_orders(data)

    orders = data.get("orders", [])
    if orders:
        print(f"\nTo cancel an order:")
        first = orders[0]
        print(f"  python portfolio/order_manager.py "
              f"--cancel {first.get('orderId')} "
              f"--symbol {first.get('symbol')} "
              f"--confirm")


if __name__ == "__main__":
    main()
