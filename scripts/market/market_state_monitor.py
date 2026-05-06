"""
Poll the market state and alert when Fear & Greed crosses a threshold.
Useful for setting up a cron job or keeping a terminal window open.

Usage:
    python market/market_state_monitor.py
    python market/market_state_monitor.py --alert-below 25
    python market/market_state_monitor.py --alert-above 75 --interval 300
"""

import sys
import json
import time
import argparse
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from auth.pat_client import AnnyMCPClient


def get_market_state(client: AnnyMCPClient) -> dict:
    result = client.call("get_market_state")
    content = result.get("content", [{}])[0].get("text", "{}")
    return json.loads(content) if isinstance(content, str) else content


def format_state(data: dict) -> str:
    fg = data.get("fearGreed", {})
    btc = data.get("btc", {})
    deriv = data.get("derivatives", {})
    etf = data.get("etfFlows", {})
    ts = datetime.now().strftime("%H:%M:%S")

    fg_val = fg.get("value", 0)
    fg_class = fg.get("classification", "")
    btc_price = btc.get("price", 0)
    btc_rsi = btc.get("rsi14", 0)
    funding = deriv.get("btcFundingRate8h", 0)
    etf_daily = etf.get("daily", 0)

    return (
        f"[{ts}] F&G={fg_val} ({fg_class}) | "
        f"BTC=${btc_price:,.0f} RSI={btc_rsi:.1f} | "
        f"Funding={funding:.4f}% | "
        f"ETF={'+' if etf_daily >= 0 else ''}{etf_daily:.0f}M"
    )


def main():
    parser = argparse.ArgumentParser(description="Market state monitor")
    parser.add_argument("--alert-below", type=int, default=0,
                        help="Alert when Fear & Greed drops below this value")
    parser.add_argument("--alert-above", type=int, default=100,
                        help="Alert when Fear & Greed rises above this value")
    parser.add_argument("--interval", type=int, default=60,
                        help="Poll interval in seconds (default: 60)")
    parser.add_argument("--once", action="store_true",
                        help="Run once and exit (no polling)")
    args = parser.parse_args()

    client = AnnyMCPClient()

    print(f"Market state monitor | alert < {args.alert_below} or > {args.alert_above} | "
          f"polling every {args.interval}s")
    print("Press Ctrl+C to stop\n")

    while True:
        try:
            data = get_market_state(client)
            line = format_state(data)
            print(line)

            fg_val = data.get("fearGreed", {}).get("value", 50)
            if fg_val < args.alert_below:
                print(f"  *** ALERT: Fear & Greed {fg_val} is below threshold {args.alert_below} ***")
            if fg_val > args.alert_above:
                print(f"  *** ALERT: Fear & Greed {fg_val} is above threshold {args.alert_above} ***")

            if args.once:
                break

            time.sleep(args.interval)

        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print(f"  ERROR: {e}")
            time.sleep(args.interval)


if __name__ == "__main__":
    main()
