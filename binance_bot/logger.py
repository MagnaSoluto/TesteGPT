"""Configuração de logging para o bot."""

from loguru import logger

logger.add("bot.log", rotation="10 MB", enqueue=True)
