#!/usr/bin/env python3
"""Telegram Bot using Bot Token (for mobile access + Mini App)."""
import os, sys
sys.path.insert(0, "/Users/ali/Desktop/signal_bot")

from telethon import TelegramClient, events
from telethon.tl.types import ReplyInlineMarkup, KeyboardButtonCallback

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
if not BOT_TOKEN or BOT_TOKEN.startswith("YOUR"):
    print("Error: TELEGRAM_BOT_TOKEN not set. Get it from @BotFather.")
    sys.exit(1)

# Bot API uses bot token directly (Telethon bot mode or python-telegram-bot)
# For simplicity with user's Telethon setup, we use TelegramClient with bot parameters

client = TelegramClient('piggy_bot_session', '', '')  # Bot mode placeholder

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("🐷 Piggy Bank Bot is active! Use /signal for analysis.")

@client.on(events.NewMessage(pattern='/signal'))
async def signal(event):
    from bot_handlers.signal_handler import build_signal_message, get_confirm_buttons
    msg = build_signal_message("BTC/USDT")
    await event.respond(msg)

@client.on(events.NewMessage(pattern='/portfolio'))
async def portfolio(event):
    await event.respond("📊 Portfolio dashboard — coming with Mini App.")

if __name__ == "__main__":
    print("Bot ready. Set TELEGRAM_BOT_TOKEN to run.")
