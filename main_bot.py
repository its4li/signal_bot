#!/usr/bin/env python3
"""Telegram bot entry point using user's Telethon session."""
import os
import sys

# Ensure project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from telethon import TelegramClient, events
from telethon.tl.types import ReplyInlineMarkup, KeyboardButtonCallback
from bot_handlers.signal_handler import build_signal_message, get_confirm_buttons
from bot_handlers.trade_handler import execute_order, build_trade_response
from analysis.signal_fetcher import fetch_ohlcv
from analysis.signal_analyzer import analyze_signal

client = TelegramClient(
    'tg_session',
    int(os.getenv('TELEGRAM_API_ID', 34978337)),
    os.getenv('TELEGRAM_API_HASH', 'your_api_hash'),
)


@client.on(events.NewMessage(pattern='/signal'))
async def handle_signal(event):
    pair = "BTC/USDT"
    msg = build_signal_message(pair)
    await event.respond(msg, buttons=ReplyInlineMarkup([
        [KeyboardButtonCallback("✅ Confirm Trade", b"trade_BUY")],
        [KeyboardButtonCallback("❌ Ignore", b"ignore")],
    ]))


@client.on(events.CallbackQuery(data=lambda d: d.startswith(b"trade_")))
async def handle_trade_callback(event):
    action = event.data.decode('utf-8').replace("trade_", "")
    result = execute_order("BTC/USDT", action)
    await event.respond(build_trade_response(result, "BTC/USDT"))


@client.on(events.NewMessage(pattern='/portfolio'))
async def handle_portfolio(event):
    # Placeholder — integrates with Condor portfolio mechanism
    await event.respond(
        "📊 Portfolio: Net Worth — see `/signal` for active signals. "
        "Integration with Condor /portfolio coming next."
    )


if __name__ == "__main__":
    print("Bot started. Send /signal in Telegram chat.")
    client.start()
    client.run_until_disconnected()
