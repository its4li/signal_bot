import os
os.environ.setdefault("TELEGRAM_API_ID", "34978337")
os.environ.setdefault("TELEGRAM_SESSION_PATH", "/Users/ali/tg_session.session")

from config import get_config


def test_config_loads():
    cfg = get_config()
    assert "rules" in cfg
    assert "hummingbot_url" in cfg
    assert "target_pairs" in cfg
