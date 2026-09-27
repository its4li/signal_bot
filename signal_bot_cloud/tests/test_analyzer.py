import pandas as pd
from analysis.signal_analyzer import analyze_signal


def test_analyze_signal_returns_dict():
    df = pd.DataFrame({
        "open": [100] * 20,
        "high": [102] * 20,
        "low": [98] * 20,
        "close": list(range(100, 120))
    })
    result = analyze_signal(df, pair="BTC/USDT")
    assert isinstance(result, dict), f"Expected dict, got {type(result)}"
    assert "action" in result
    assert result["action"] in ["BUY", "SELL", "HOLD"]
    assert "indicators" in result
    assert "macd_diff" in result["indicators"]
    assert "rsi" in result["indicators"]


def test_analyze_signal_hold_for_flat():
    df = pd.DataFrame({
        "open": [100] * 20,
        "high": [100] * 20,
        "low": [100] * 20,
        "close": [100] * 20,
        "volume": [500] * 20
    })
    result = analyze_signal(df, pair="ETH/USDT")
    assert result["pair"] == "ETH/USDT"
    assert result["action"] in ["BUY", "SELL", "HOLD"]
