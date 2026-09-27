from bot_handlers.signal_handler import build_signal_message, get_confirm_buttons


def test_build_signal_message_contains_pair():
    msg = build_signal_message("BTC/USDT")
    assert "BTC/USDT" in msg
    assert "BUY" in msg or "SELL" in msg or "HOLD" in msg


def test_get_confirm_buttons_has_trade_button():
    buttons = get_confirm_buttons()
    assert "inline_keyboard" in buttons
    # Find confirm trade button
    texts = []
    for row in buttons.get("inline_keyboard", []):
        for btn in row:
            texts.append(btn.get("text", ""))
    assert any("Confirm" in t for t in texts)
