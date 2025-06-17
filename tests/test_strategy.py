import pandas as pd
from binance_bot.strategy import add_rsi, check_signal


def test_add_rsi():
    data = {
        "close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    }
    df = pd.DataFrame(data)
    result = add_rsi(df, window=14)
    assert "rsi" in result.columns
    assert len(result) == len(df)


def test_check_signal_buy_sell():
    df = pd.DataFrame({"close": [1, 2], "rsi": [25, 35]})
    signal = check_signal(df, prev_rsi=25, prev_close=1, oversold=30, overbought=70)
    assert signal == "BUY"

    df = pd.DataFrame({"close": [2, 1], "rsi": [75, 65]})
    signal = check_signal(df, prev_rsi=75, prev_close=2, oversold=30, overbought=70)
    assert signal == "SELL"

    df = pd.DataFrame({"close": [2, 2], "rsi": [50, 55]})
    signal = check_signal(df, prev_rsi=50, prev_close=2, oversold=30, overbought=70)
    assert signal is None
