"""
Есть:
prices = {
    "AAPL": 250,
    "NVDA": 175,
    "MSFT": 500,
    "TSLA": 220,
    "AMD": 140
}
Создай словарь:
expensive
с помощью dict comprehension, в котором останутся только акции с ценой не меньше 200.
"""

prices = {
    "AAPL": 250,
    "NVDA": 175,
    "MSFT": 500,
    "TSLA": 220,
    "AMD": 140
}

expensive = {
    ticker: price
    for ticker, price in prices.items()
    if price >= 200
}

print(expensive)