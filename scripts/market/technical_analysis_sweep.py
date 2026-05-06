"""
Sweep multiple assets for technical analysis and output a ranked table.
Ranks by RSI value (oversold first), then summarizes EMA position and MACD signal.

Usage:
    python market/technical_analysis_sweep.py
    python market/technical_analysis_sweep.py --assets BTC ETH SOL DOGE XRP
    python market/technical_analysis_sweep.py --timeframe 4h --csv output.csv
"""

import sys
import json
import argparse
import csv as csv_module
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from auth.pat_client import AnnyMCPClient

DEFAULT_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "AVAX", "LINK", "DOT"]
DEFAULT_TIMEFRAME = "1d"


def get_ta(client: AnnyMCPClient, asset: str, timeframe: str) -> dict:
    symbol = f"{asset}USDT"
    result = client.call("get_technical_analysis", {"symbol": symbol, "timeframe": timeframe})
    content = result.get("content", [{}])[0].get("text", "{}")
    return json.loads(content) if isinstance(content, str) else content


def format_row(asset: str, data: dict) -> dict:
    momentum = data.get("momentum", {})
    trend = data.get("trend", {})
    rsi = momentum.get("rsi", {})
    macd = momentum.get("macd", {})
    adx = momentum.get("adx", {})
    price = data.get("price", 0)
    ema200 = trend.get("ema200", 0)

    rsi_val = rsi.get("value", 0)
    above_ema200 = price > ema200 if price and ema200 else None
    macd_trend = macd.get("trend", "")
    adx_val = adx.get("value", 0)

    return {
        "asset": asset,
        "rsi": round(rsi_val, 1),
        "rsi_signal": rsi.get("signal", ""),
        "macd_trend": macd_trend,
        "adx": round(adx_val, 1),
        "above_ema200": "YES" if above_ema200 else "NO" if above_ema200 is not None else "?",
        "ema200": round(ema200, 2) if ema200 else 0,
    }


def print_table(rows: list[dict]):
    header = f"{'ASSET':<6} {'RSI':>5} {'SIGNAL':<12} {'MACD':>12} {'ADX':>5} {'EMA200':>8}"
    print("\n" + header)
    print("-" * len(header))
    for r in rows:
        ema_flag = f"[{'ABOVE' if r['above_ema200'] == 'YES' else 'BELOW'}]"
        print(
            f"{r['asset']:<6} {r['rsi']:>5.1f} {r['rsi_signal']:<12} "
            f"{r['macd_trend']:>12} {r['adx']:>5.1f} {ema_flag:>8}"
        )


def write_csv(rows: list[dict], path: str):
    with open(path, "w", newline="") as f:
        writer = csv_module.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nCSV written to {path}")


def main():
    parser = argparse.ArgumentParser(description="Technical analysis sweep")
    parser.add_argument("--assets", nargs="+", default=DEFAULT_ASSETS)
    parser.add_argument("--timeframe", default=DEFAULT_TIMEFRAME,
                        choices=["5m", "15m", "30m", "1h", "4h", "1d", "1w"])
    parser.add_argument("--csv", help="Write results to CSV file")
    args = parser.parse_args()

    client = AnnyMCPClient()
    rows = []

    print(f"Sweeping {len(args.assets)} assets on {args.timeframe}...")
    for asset in args.assets:
        print(f"  {asset}...", end=" ", flush=True)
        try:
            data = get_ta(client, asset, args.timeframe)
            row = format_row(asset, data)
            rows.append(row)
            print(f"RSI={row['rsi']:.1f}")
        except Exception as e:
            print(f"ERROR: {e}")

    # Sort by RSI ascending (oversold first)
    rows.sort(key=lambda r: r["rsi"])
    print_table(rows)

    if args.csv:
        write_csv(rows, args.csv)


if __name__ == "__main__":
    main()
