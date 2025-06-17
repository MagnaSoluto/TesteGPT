"""Funções para execução de ordens."""

from binance.client import Client
from binance.exceptions import BinanceAPIException
from loguru import logger


def execute_order(client: Client, symbol: str, side: str, quantity: float):
    """Executa ordem de mercado.

    Parameters
    ----------
    client : Client
        Instância do cliente da Binance.
    symbol : str
        Par de trading.
    side : str
        'BUY' ou 'SELL'.
    quantity : float
        Quantidade a negociar.
    """

    if side not in {"BUY", "SELL"}:
        raise ValueError("side deve ser 'BUY' ou 'SELL'")

    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type=Client.ORDER_TYPE_MARKET,
            quantity=quantity,
        )
        logger.info(f"Ordem executada: {order}")
        return order
    except BinanceAPIException as exc:
        logger.error(f"Erro ao executar ordem: {exc}")
        raise
