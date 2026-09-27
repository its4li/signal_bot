import pandas as pd
import numpy as np


def fetch_ohlcv(pair: str = "BTC/USDT") -> pd.DataFrame:
    """Fetch OHLCV data. Mock implementation for prototype; integrate TradingView-API or Python fetch in production."""
    np.random.seed(42)
    n = 50
    close = 65000 + np.cumsum(np.random.randn(n) * 200)
    df = pd.DataFrame({
        "open": close * 0.998,
        "high": close * 1.002,
        "low": close * 0.996,
        "close": close,
        "volume": np.random.randint(100, 1000, n),
    })
    df.index = pd.date_range(start="2026-01-01", periods=n, freq="D")
    return df
