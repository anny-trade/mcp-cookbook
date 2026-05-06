"""
Run a custom strategy backtest from a JSON strategy file, then scan live conditions.

The strategy JSON file format matches the backtest_custom_strategy tool parameters.
See examples/ for sample JSON files.

Usage:
    python backtest/custom_strategy_runner.py --strategy ema_cross.json
    python backtest/custom_strategy_runner.py --strategy ema_cross.json --scan-only
    python backtest/custom_strategy_runner.py --strategy ema_cross.json --asset ETH
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from auth.pat_client import AnnyMCPClient

# Example strategy bundled with the script
EXAMPLE_STRATEGY = {
    "name": "EMA 9/21 Crossover",
    "asset": "BTC",
    "interval": "1d",
    "direction": "long",
    "lookback_period": "1y",
    "trigger": {
        "indicator": "EMA",
        "params": {"period": 9},
        "field": "value",
        "operator": "crosses_above",
        "compare_to": {
            "indicator": "EMA",
            "params": {"period": 21},
            "field": "value"
        }
    },
    "confirmations": [],
    "stop_loss": {"type": "percent", "value": 3},
    "take_profit": {"type": "percent", "value": 6}
}


def load_strategy(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def print_backtest_results(data: dict):
    perf = data.get("performance", {})
    oos = data.get("oos", {})
    name = data.get("name", "Strategy")
    asset = data.get("asset", "")
    signal = data.get("signalStatus", "unknown")

    print(f"\n{'='*50}")
    print(f"{name} — {asset}")
    print(f"{'='*50}")
    print(f"Total return:    {perf.get('totalReturn', 0):+.2f}%")
    print(f"vs Buy & Hold:   {perf.get('delta', 0):+.2f}%")
    print(f"Win rate:        {perf.get('winRate', 0):.1f}%")
    print(f"Sharpe ratio:    {perf.get('sharpeRatio', 0):.2f}")
    print(f"Max drawdown:    {perf.get('maxDrawdown', 0):.1f}%")
    print(f"Trade count:     {perf.get('tradeCount', 0)}")
    print(f"Avg hold (days): {perf.get('avgHoldDays', 0):.1f}")
    print(f"\nOOS return:      {oos.get('return', 0):+.2f}%")
    print(f"OOS validated:   {'YES' if oos.get('validated') else 'NO'}")
    print(f"\nSignal now:      {signal}")

    warnings = data.get("warnings", [])
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  ! {w}")


def print_scan_results(data: dict):
    status = data.get("overallStatus", "unknown")
    conditions = data.get("conditions", [])

    print(f"\nLive scan: {status}")
    for c in conditions:
        indicator = c.get("indicator", "")
        current = c.get("currentValue", 0)
        cond_status = c.get("status", "")
        print(f"  {indicator}: {current} — {cond_status}")


def main():
    parser = argparse.ArgumentParser(description="Custom strategy runner")
    parser.add_argument("--strategy", help="Path to strategy JSON file")
    parser.add_argument("--asset", help="Override the asset in the strategy file")
    parser.add_argument("--scan-only", action="store_true",
                        help="Only run live scan, skip backtest")
    parser.add_argument("--backtest-only", action="store_true",
                        help="Only run backtest, skip live scan")
    parser.add_argument("--example", action="store_true",
                        help="Run the bundled EMA 9/21 example strategy")
    args = parser.parse_args()

    if args.example:
        strategy = EXAMPLE_STRATEGY.copy()
    elif args.strategy:
        strategy = load_strategy(args.strategy)
    else:
        parser.error("Provide --strategy <file.json> or --example")

    if args.asset:
        strategy["asset"] = args.asset

    client = AnnyMCPClient()

    if not args.scan_only:
        print(f"Running backtest for {strategy.get('name', 'strategy')} on {strategy['asset']}...")
        result = client.call("backtest_custom_strategy", strategy)
        content = result.get("content", [{}])[0].get("text", "{}")
        data = json.loads(content) if isinstance(content, str) else content
        print_backtest_results(data)

    if not args.backtest_only:
        print(f"\nScanning live conditions for {strategy['asset']}...")
        scan_params = {
            "asset": strategy["asset"] + "USDT",
            "interval": strategy.get("interval", "1d"),
            "trigger": strategy["trigger"],
            "confirmations": strategy.get("confirmations", []),
        }
        result = client.call("scan_custom_signals", scan_params)
        content = result.get("content", [{}])[0].get("text", "{}")
        scan_data = json.loads(content) if isinstance(content, str) else content
        print_scan_results(scan_data)


if __name__ == "__main__":
    main()
