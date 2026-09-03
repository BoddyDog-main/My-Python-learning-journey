"""
У тебя есть несколько позиций:
positions = [
    ("AAPL", 200, 4),
    ("NVDA", 150, 6),
    ("MSFT", 400, 3)
]
Твоя задача:
Написать for, который распаковывает каждый кортеж в:
ticker
price
shares
Для каждой позиции вывести:
Ticker: AAPL
Position value: 800
и так для всех трёх.
"""

positions = [
    ("AAPL", 200, 4),
    ("NVDA", 150, 6),
    ("MSFT", 400, 3)
]

for ticker, price, shares in positions:
    print(f'Ticker: {ticker}\n'
          f'Position value: {price * shares}\n')