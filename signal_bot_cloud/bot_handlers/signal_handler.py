from analysis.signal_fetcher import fetch_ohlcv
from analysis.signal_analyzer import analyze_signal


def build_signal_message(pair: str = "BTC/USDT") -> str:
    df = fetch_ohlcv(pair)
    result = analyze_signal(df, pair=pair)
    indicators = result.get("indicators", {})
    macd = indicators.get("macd_diff", 0)
    rsi = indicators.get("rsi", 50)
    action_icon = "🟢" if result["action"] == "BUY" else ("🔴" if result["action"] == "SELL" else "⚪")
    return (
        f"📊 <b>Signal — {result['pair']}</b>\n"
        f"{action_icon} <b>Action: {result['action']}</b>\n"
        f"Indicators: MACD={macd:.2f}, RSI={rsi:.1f}\n"
        f"Confidence: {result['confidence']}\n"
        f"{result['message']}"
    )


def get_confirm_buttons():
    # Inline buttons for Telegram confirmation
    # Using a simple dict representation for prototype; Telethon buttons can be mapped from this
    return {
        "inline_keyboard": [
            [{"text": "✅ Confirm Trade", "callback_data": "trade_BUY"}],
            [{"text": "❌ Ignore", "callback_data": "ignore"}],
        ]
    }
