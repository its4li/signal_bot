import pandas as pd
from analysis.signal_fetcher import fetch_ohlcv


def test_fetch_ohlcv_returns_dataframe():
    df = fetch_ohlcv("BTC/USDT")
    assert isinstance(df, pd.DataFrame), f"Expected DataFrame, got {type(df)}"
    assert "close" in df.columns, "Missing 'close' column"
    assert len(df) > 0, "DataFrame is empty"


def test_fetch_ohlcv_columns():
    df = fetch_ohlcv()
    required = {"open", "high", "low", "close", "volume"}
    assert required.issubset(set(df.columns)), f"Missing columns: {required - set(df.columns)}"
