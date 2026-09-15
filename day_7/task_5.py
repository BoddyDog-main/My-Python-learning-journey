"""
Дано:

prices = {
    "AAPL": 250,
    "NVDA": 175,
    "MSFT": 500,
    "TSLA": 220
}

Создай:

discounted

с помощью dict comprehension, где каждая цена уменьшена на 10%.
"""

prices = {
    "AAPL": 250,
    "NVDA": 175,
    "MSFT": 500,
    "TSLA": 220
}

discounted = {
    ticker : price * 0.9
    for ticker, price in prices.items()
}

for key, value in discounted.items():
    print(key, value)