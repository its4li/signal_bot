import requests
import os


def execute_order(pair: str, action: str = "BUY") -> dict:
    url = os.getenv("HUMMINGBOT_API_URL", "http://localhost:8000") + "/trade"
    payload = {"pair": pair, "action": action}
    try:
        resp = requests.post(url, json=payload, timeout=5)
        return resp.json() if resp.status_code == 200 else {"status": "failed", "detail": f"HTTP {resp.status_code}"}
    except Exception as e:
        return {"status": "failed", "detail": str(e)}


def build_trade_response(result: dict, pair: str) -> str:
    status = result.get("status", "unknown")
    if status == "success" or ("success" in str(result.get("message", "")).lower()):
        return f"✅ Trade executed: {pair} {result.get('action', 'BUY')} — {result.get('message', 'filled')}"
    else:
        return f"❌ Trade failed: {pair} — {result.get('detail', 'Unknown error')}"
