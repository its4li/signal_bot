#!/usr/bin/env python3
"""Auto-routine: fetches signal every interval (e.g., hourly via cron or loop)."""
import sys, os
sys.path.insert(0, "/Users/ali/Desktop/signal_bot")
from analysis.signal_fetcher import fetch_ohlcv
from analysis.signal_analyzer import analyze_signal
from config import get_config

def main():
    cfg = get_config()
    pair = cfg.get("target_pairs", ["BTC/USDT"])[0]
    df = fetch_ohlcv(pair)
    result = analyze_signal(df, pair=pair)
    print(f"[AUTO-SIGNAL] {pair} -> Action: {result['action']} (MACD={result['indicators']['macd_diff']:.2f}, RSI={result['indicators']['rsi']:.1f})")
    return result

if __name__ == "__main__":
    main()
