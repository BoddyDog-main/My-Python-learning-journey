"""
А теперь попробуй самостоятельно вывести стоимость позиции AAPL.
Дано:
portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    }
}

Нужно получить:
AAPL position value: 1150
"""

portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    }
}

print(f'AAPL position value: {portfolio["AAPL"]["price"]*portfolio["AAPL"]["shares"]}\n'
      f'MSFT position value: {portfolio["MSFT"]["price"]*portfolio["MSFT"]["shares"]}')