"""Cliente Binance e utilidades de dados."""

from typing import Any
from binance.client import Client
import pandas as pd
from loguru import logger


def init_client(api_key: str, api_secret: str) -> Client:
    """Inicializa e retorna a instância do Client da Binance."""
    return Client(api_key, api_secret)


def get_ohlcv(client: Client, symbol: str, interval: str, limit: int = 500) -> pd.DataFrame:
    """Retorna dados OHLCV como DataFrame.

    Parameters
    ----------
    client : Client
        Instância do cliente da Binance.
    symbol : str
        Par de trading.
    interval : str
        Intervalo de tempo (ex: '1m').
    limit : int
        Quantidade de candles a retornar.
    """
    try:
        klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    except Exception as exc:
        logger.error(f"Erro ao obter candles: {exc}")
        raise

    df = pd.DataFrame(klines, columns=[
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
        "taker_buy_base",
        "taker_buy_quote",
        "ignore",
    ])
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
    return df
