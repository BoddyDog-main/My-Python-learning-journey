"""
Давай следующее задание:
portfolio = {
    "AAPL": 230,
    "NVDA": 175,
    "MSFT": 510
}
Нужно вывести:
AAPL → 230
NVDA → 175
MSFT → 510
Но есть условие: используй
for key, value in ...
и items().
"""

portfolio = {
    "AAPL": 230,
    "NVDA": 175,
    "MSFT": 510
}

for key, value in portfolio.items():
    print(f'{key} -> {value}')

