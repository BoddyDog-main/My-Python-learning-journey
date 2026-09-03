"""
portfolio = {
    "AAPL": 230,
    "NVDA": 175,
    "MSFT": 510
}

Сделай следующее:

Добавь новую акцию:
TSLA → 350
Измени цену AAPL с 230 на 250.
Удали NVDA.
Используя for + items(), выведи итоговый портфель в формате:
AAPL → 250
MSFT → 510
"""

portfolio = {
    "AAPL": 230,
    "NVDA": 175,
    "MSFT": 510
}

portfolio['TSLA'] = 350
portfolio['AAPL'] = 250
del portfolio['NVDA']
for key, value in portfolio.items():
    print(f'{key} -> {value}')
