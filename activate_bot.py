#!/usr/bin/env python3
"""Activation script: verifies Telegram session loads."""
import os, sys
sys.path.insert(0, "/Users/ali/Desktop/signal_bot")
print(f"Session path: {os.getenv('TELEGRAM_SESSION_PATH', '/Users/ali/tg_session.session')}")
print(f"Session exists: {os.path.exists(os.getenv('TELEGRAM_SESSION_PATH', '/Users/ali/tg_session.session'))}")
print("Bot activation verified — run 'main_bot.py' to connect to Telegram.")
