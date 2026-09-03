"""
Создай:
stock = ("AAPL", 230, 5)
Это:
тикер
цена
количество акций
Распакуй tuple в три переменные:
ticker
price
shares
и выведи:
Ticker: AAPL
Price: 230
Shares: 5
Не используй stock[0], stock[1], stock[2].
"""

stock = ("AAPL", 230, 5)
ticker, price, shares = stock #распаковка кортежа !работает по принципу! одна переменная ← один элемент
print(f'Ticker: {ticker}\n'
      f'Price: {price}\n'
      f'Shares: {shares}')