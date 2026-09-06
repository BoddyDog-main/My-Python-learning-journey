"""
Дано:
ticker = "nvda"
price = 175.5678
shares = 10
С помощью одного print и f-string выведи:
Ticker: NVDA
Price: 175.57
Position value: 1755.68
"""

ticker = "nvda"
price = 175.5678
shares = 10

print(f'Ticker: {ticker.upper()}\n'
      f'Price: {price:.2f}\n'
      f'Position value: {price*shares:.2f}\n')