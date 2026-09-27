from bot_handlers.trade_handler import execute_order, build_trade_response


def test_execute_order_returns_dict():
    result = execute_order("BTC/USDT", "BUY")
    assert isinstance(result, dict)
    assert "status" in result


def test_build_trade_response_format():
    assert "Trade executed" in build_trade_response({"status": "success", "message": "filled"}, "BTC/USDT")
    assert "Trade failed" in build_trade_response({"status": "failed", "detail": "timeout"}, "ETH/USDT")
