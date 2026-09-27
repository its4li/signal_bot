import sys, os
sys.path.insert(0, "/Users/ali/Desktop/signal_bot")
from routines.auto_signal import main


def test_auto_signal_runs():
    result = main()
    assert isinstance(result, dict)
    assert "action" in result
    assert result["pair"] in ["BTC/USDT", "ETH/USDT"]
