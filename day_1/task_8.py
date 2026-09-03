"""
У нас есть:
stocks = [
    ("AAPL", 230),
    ("NVDA", 175),
    ("MSFT", 510)
]
Каждый элемент списка — это tuple.
Твоя задача — вывести:
Ticker: AAPL, Price: 230
Ticker: NVDA, Price: 175
Ticker: MSFT, Price: 510
Условие
Используй:
for
распаковку tuple
f-string
Не используй индексы ([0], [1]).
"""

stocks = [
    ("AAPL", 230),
    ("NVDA", 175),
    ("MSFT", 510)
]

for ticker, price in stocks:
    print(f'Ticker: {ticker}, Price: {price}')
    
for stock in stocks:
    ticker, price = stock
    print(f'Ticker: {ticker}, Price: {price}')

