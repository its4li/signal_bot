#!/usr/bin/env python3
"""Vercel serverless endpoint for Telegram webhook + signal analysis."""
import sys, os, json
sys.path.insert(0, "/Users/ali/Desktop/signal_bot")

def handler(event, context):
    path = event.get("path", "/")
    method = event.get("httpMethod", "GET")
    if method == "POST" and "/webhook" in path:
        return {"statusCode": 200, "body": '{"ok":true}', "headers": {"Content-Type":"application/json"}}
    try:
        from analysis.signal_fetcher import fetch_ohlcv
        from analysis.signal_analyzer import analyze_signal
        df = fetch_ohlcv("BTC/USDT")
        result = analyze_signal(df, pair="BTC/USDT")
        return {"statusCode": 200, "body": json.dumps({"signal": result, "status":"ok"}), "headers":{"Content-Type":"application/json"}}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)}), "headers":{"Content-Type":"application/json"}}
