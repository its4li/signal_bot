from bot_handlers.signal_handler import build_signal_message
from bot_handlers.trade_handler import execute_order, build_trade_response


def test_end_to_end_signal_format():
    msg = build_signal_message("BTC/USDT")
    assert "📊" in msg
    assert "BTC/USDT" in msg


def test_end_to_end_trade_response():
    result = execute_order("BTC/USDT", "BUY")
    response = build_trade_response(result, "BTC/USDT")
    assert isinstance(response, str)
    assert len(response) > 0
