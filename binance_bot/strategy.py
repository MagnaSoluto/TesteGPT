"""Implementação da estratégia RSI Candle."""

import pandas as pd
from ta.momentum import RSIIndicator


def add_rsi(df: pd.DataFrame, window: int) -> pd.DataFrame:
    """Adiciona a coluna de RSI ao DataFrame."""

    rsi = RSIIndicator(close=df["close"], window=window).rsi()
    df = df.copy()
    df["rsi"] = rsi
    return df


def check_signal(df: pd.DataFrame, prev_rsi: float, prev_close: float, oversold: int, overbought: int):
    """Verifica sinal de compra ou venda baseado no RSI e candle atual.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo pelo menos as colunas 'close' e 'rsi'. Deve estar ordenado do mais antigo para o mais recente.
    prev_rsi : float
        RSI do candle anterior.
    prev_close : float
        Fechamento do candle anterior.
    oversold : int
        Nível de sobrevenda.
    overbought : int
        Nível de sobrecompra.

    Retorna
    -------
    str | None
        "BUY" se houver sinal de compra, "SELL" se houver sinal de venda ou None caso contrário.
    """

    current = df.iloc[-1]

    if prev_rsi < oversold and current["rsi"] > oversold and current["close"] > prev_close:
        return "BUY"
    if prev_rsi > overbought and current["rsi"] < overbought and current["close"] < prev_close:
        return "SELL"
    return None
