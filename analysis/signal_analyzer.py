import pandas as pd
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
import json
import os


def load_rules(config_path: str = None) -> dict:
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "rules_config.json")
    with open(config_path, "r") as f:
        return json.load(f)


def analyze_signal(df: pd.DataFrame, pair: str = "BTC/USDT", config_path: str = None) -> dict:
    close = df["close"]
    rules = load_rules(config_path) if config_path else load_rules()

    # Indicators
    macd = MACD(close=close)
    rsi = RSIIndicator(close=close)
    bb = BollingerBands(close=close, window=20, window_dev=2)

    macd_diff = macd.macd_diff().iloc[-1] if not macd.macd_diff().empty else 0.0
    rsi_val = rsi.rsi().iloc[-1] if not rsi.rsi().empty else 50.0

    thresholds = rules.get("rules", {})
    macd_thresh = thresholds.get("macd_diff_threshold", 0)
    rsi_buy = thresholds.get("rsi_buy_above", 50)
    rsi_sell = thresholds.get("rsi_sell_below", 30)

    action = "HOLD"
    if macd_diff > macd_thresh and rsi_val > rsi_buy:
        action = "BUY"
    elif rsi_val < rsi_sell:
        action = "SELL"

    return {
        "pair": pair,
        "action": action,
        "confidence": 0.7 if action != "HOLD" else 0.3,
        "indicators": {
            "macd_diff": float(macd_diff),
            "rsi": float(rsi_val),
        },
        "message": f"{pair}: {action} (MACD={macd_diff:.2f}, RSI={rsi_val:.1f})",
    }
