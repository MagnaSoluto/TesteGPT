"""Ponto de entrada do bot."""

import time
import schedule
from loguru import logger

from config import get_settings
from binance_bot.client import init_client, get_ohlcv
from binance_bot.logger import logger as log_conf
from binance_bot.strategy import add_rsi, check_signal
from binance_bot.trader import execute_order


def job(settings, client):
    """Executa ciclo de checagem de sinal e envio de ordens."""

    df = get_ohlcv(client, settings.symbol, settings.interval, limit=settings.rsi_window + 2)
    df = add_rsi(df, settings.rsi_window)
    prev = df.iloc[-2]
    signal = check_signal(df, prev_rsi=prev["rsi"], prev_close=prev["close"], oversold=settings.rsi_oversold, overbought=settings.rsi_overbought)
    if signal:
        execute_order(client, settings.symbol, signal, settings.quantity)
    else:
        logger.info("Nenhum sinal encontrado")


def main():
    """Carrega configurações, inicializa cliente e inicia o loop principal."""

    settings = get_settings()
    client = init_client(settings.api_key, settings.api_secret)

    schedule.every(1).minutes.do(job, settings=settings, client=client)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Bot finalizado pelo usuário")
            break
        except Exception as exc:
            logger.exception(f"Erro inesperado: {exc}")
            time.sleep(5)


if __name__ == "__main__":
    main()
