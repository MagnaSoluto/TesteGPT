"""Carrega e valida configurações do arquivo .env."""

from dataclasses import dataclass
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

@dataclass
class Settings:
    """Configurações para o bot."""

    api_key: str
    api_secret: str
    symbol: str
    interval: str
    quantity: float
    rsi_window: int
    rsi_oversold: int
    rsi_overbought: int


def get_settings() -> Settings:
    """Lê variáveis de ambiente e retorna um objeto Settings validado."""

    try:
        api_key = os.environ["BINANCE_API_KEY"]
        api_secret = os.environ["BINANCE_API_SECRET"]
        symbol = os.environ.get("SYMBOL", "").upper()
        interval = os.environ.get("INTERVAL", "1m")
        quantity = float(os.environ.get("QUANTITY", 0))
        rsi_window = int(os.environ.get("RSI_WINDOW", 14))
        rsi_oversold = int(os.environ.get("RSI_OVERSOLD", 30))
        rsi_overbought = int(os.environ.get("RSI_OVERBOUGHT", 70))
    except Exception as exc:
        logger.error(f"Erro ao ler variáveis de ambiente: {exc}")
        raise

    if not api_key or not api_secret:
        raise ValueError("API KEY e SECRET devem ser preenchidos")
    if not symbol:
        raise ValueError("O símbolo deve ser informado")
    if quantity <= 0:
        raise ValueError("QUANTITY deve ser maior que zero")
    if rsi_window <= 0:
        raise ValueError("RSI_WINDOW deve ser maior que zero")

    return Settings(
        api_key=api_key,
        api_secret=api_secret,
        symbol=symbol,
        interval=interval,
        quantity=quantity,
        rsi_window=rsi_window,
        rsi_oversold=rsi_oversold,
        rsi_overbought=rsi_overbought,
    )
