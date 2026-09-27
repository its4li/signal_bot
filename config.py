import os
import json
from dotenv import load_dotenv

load_dotenv()


def get_config() -> dict:
    rules_path = os.path.join(os.path.dirname(__file__), "analysis", "rules_config.json")
    with open(rules_path, "r") as f:
        rules = json.load(f)
    rules["hummingbot_url"] = os.getenv("HUMMINGBOT_API_URL", "http://localhost:8000")
    rules["telegram_session"] = os.getenv("TELEGRAM_SESSION_PATH", "")
    rules["telegram_api_id"] = os.getenv("TELEGRAM_API_ID", "")
    rules["target_pairs"] = [p.strip() for p in os.getenv("TARGET_PAIRS", "BTC/USDT,ETH/USDT").split(",")]
    return rules
