# Binance RSI Candle Bot

Este projeto implementa um robô de trading automático utilizando a API da Binance e a estratégia **RSI Candle**. Ele executa ordens de compra e venda quando o RSI cruza os níveis de sobrevenda ou sobrecompra e o candle de confirmação fecha em direção ao sinal.

## Requisitos

- Python 3.8+
- Conta na Binance com API habilitada

## Instalação

1. Clone o repositório e crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

1. Copie o arquivo `.env.example` para `.env` e preencha as variáveis:
   ```bash
   cp .env.example .env
   ```
   Edite o arquivo `.env` preenchendo suas chaves de API da Binance e os parâmetros desejados (símbolo, intervalo, quantidade etc.).

2. Execute o bot:
   ```bash
   python main.py
   ```

Os logs serão gravados no console e no arquivo `bot.log`.

## Testes

Execute os testes unitários com:
```bash
pytest
```

Certifique-se de que todas as dependências estejam instaladas e que o arquivo `.env` esteja configurado antes de rodar o bot.
