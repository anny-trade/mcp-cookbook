"""
Run CFO Line backtests across multiple assets and output a Sharpe-ranked table.
This reproduces the multi-asset sweep from the 2026-04-26 overnight research session.

Usage:
    python backtest/cfo_line_multi_asset.py
    python backtest/cfo_line_multi_asset.py --assets BTC ETH DOT XRP DOGE
    python backtest/cfo_line_multi_asset.py --interval 1d --period 1y --mode long
    python backtest/cfo_line_multi_asset.py --csv results.csv
"""

import sys
import json
import argparse
import csv as csv_module
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from auth.pat_client import AnnyMCPClient

DEFAULT_ASSETS = ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "AVAX", "LINK", "DOT"]
VALIDATED_ASSETS = ["DOT", "XRP", "DOGE", "BTC", "AVAX", "ETH"]  # from research


def run_backtest(client: AnnyMCPClient, asset: str, interval: str, period: str, mode: str) -> dict:
    result = client.call("backtest_custom_strategy", {
        "asset": asset,
        "interval": interval,
        "period": period,
        "mode": mode,
    })
    content = result.get("content", [{}])[0].get("text", "{}")
    return json.loads(content) if isinstance(content, str) else content


def format_row(asset: str, data: dict) -> dict:
    perf = data.get("performance", {})
    oos = data.get("oos", {})
    return {
        "asset": asset,
        "total_return": perf.get("totalReturn", 0),
        "delta_bh": perf.get("delta", 0),
        "win_rate": perf.get("winRate", 0),
        "sharpe": perf.get("sharpeRatio", 0),
        "max_dd": perf.get("maxDrawdown", 0),
        "trades": perf.get("tradeCount", 0),
        "oos_return": oos.get("return", None),
        "oos_validated": oos.get("validated", False),
    }


def print_table(rows: list[dict], interval: str, period: str, mode: str):
    print(f"\nCFO Line Backtest — {interval}/{period} — {mode} mode")
    print(f"Ranked by Sharpe ratio\n")
    header = (f"{'ASSET':<6} {'RETURN':>8} {'DELTA':>7} {'WIN%':>6} "
              f"{'SHARPE':>7} {'DD':>6} {'TRADES':>6} {'OOS':>8} {'VALID':>5}")
    print(header)
    print("-" * len(header))
    for r in rows:
        oos_str = f"{r['oos_return']:+.2f}%" if r['oos_return'] is not None else "N/A"
        valid_str = "YES" if r['oos_validated'] else "NO"
        print(
            f"{r['asset']:<6} {r['total_return']:>+7.2f}% {r['delta_bh']:>+6.2f}% "
            f"{r['win_rate']:>5.1f}% {r['sharpe']:>7.2f} {r['max_dd']:>5.1f}% "
            f"{r['trades']:>6} {oos_str:>8} {valid_str:>5}"
        )
    validated = [r for r in rows if r["oos_validated"]]
    print(f"\nValidated (OOS > 0): {len(validated)}/{len(rows)} assets")


def write_csv(rows: list[dict], path: str):
    with open(path, "w", newline="") as f:
        writer = csv_module.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV written to {path}")


def main():
    parser = argparse.ArgumentParser(description="CFO Line multi-asset backtest")
    parser.add_argument("--assets", nargs="+", default=DEFAULT_ASSETS)
    parser.add_argument("--interval", default="1d",
                        choices=["1h", "4h", "1d", "1w"])
    parser.add_argument("--period", default="1y",
                        choices=["3m", "6m", "9m", "1y"])
    parser.add_argument("--mode", default="long",
                        choices=["long", "long_short", "short"])
    parser.add_argument("--validated-only", action="store_true",
                        help="Only test the research-validated assets")
    parser.add_argument("--csv", help="Write results to CSV file")
    args = parser.parse_args()

    assets = VALIDATED_ASSETS if args.validated_only else args.assets
    client = AnnyMCPClient()
    rows = []

    print(f"Running CFO Line backtest on {len(assets)} assets...")
    print(f"Each backtest costs 100 credits. Total: {len(assets) * 100} credits\n")

    for asset in assets:
        print(f"  {asset}...", end=" ", flush=True)
        try:
            data = run_backtest(client, asset, args.interval, args.period, args.mode)
            row = format_row(asset, data)
            rows.append(row)
            oos = f"OOS={row['oos_return']:+.2f}%" if row['oos_return'] is not None else ""
            print(f"Sharpe={row['sharpe']:.2f} Return={row['total_return']:+.2f}% {oos}")
        except Exception as e:
            print(f"ERROR: {e}")

    if not rows:
        print("No results.")
        return

    # Sort by Sharpe descending
    rows.sort(key=lambda r: r["sharpe"], reverse=True)
    print_table(rows, args.interval, args.period, args.mode)

    if args.csv:
        write_csv(rows, args.csv)


if __name__ == "__main__":
    main()
