"""
Есть словарь:

stock = {
    "ticker": "AAPL",
    "price": 230,
    "shares": 5,
    "sector": "Technology"
}

Сделай:

Выведи все ключи.
Выведи все значения.
Выведи все пары ключ → значение через items().
Получи цену через get().
Попробуй получить ключ "currency" через get() так, чтобы вместо None выводилось "USD"
"""

stock = {
    "ticker": "AAPL",
    "price": 230,
    "shares": 5,
    "sector": "Technology"
}

print(stock.keys())
print(stock.values())
print(stock.items())
print(stock.get("price"))
print(stock.get("currency", 'USD'))
