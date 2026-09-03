"""
Вложенные структуры
"""
"""Есть:

portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    },
    "NVDA": {
        "price": 175,
        "shares": 10
    }
}

Без for пока.

Сделай так, чтобы программа вывела:

AAPL price: 230
AAPL shares: 5
NVDA price: 175"""


portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    },
    "NVDA": {
        "price": 175,
        "shares": 10
    }
}

print(f'AAPL pice: {portfolio["AAPL"]["price"]}\n'
      f'AAPL shares: {portfolio["AAPL"]["shares"]}\n'
      f'MSFT pice: {portfolio["MSFT"]["price"]}\n'
      f'MSFT shares: {portfolio["MSFT"]["shares"]}\n'
      f'NVDA pice: {portfolio["NVDA"]["price"]}\n'
      f'NVDA shares: {portfolio["NVDA"]["shares"]}')