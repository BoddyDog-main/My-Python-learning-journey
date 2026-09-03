"""
Теперь хочу проверить, действительно ли ты понял, почему tuple может быть полезен.
Представь:
stock = ("AAPL", 230, 5)
где:
"AAPL" — тикер
230 — цена
5 — количество акций
Попробуй написать программу, которая:
распаковывает tuple;
вычисляет общую стоимость позиции;
выводит результат.
Ожидаемый результат:
Ticker: AAPL
Position value: 1150
Формула простая:
price × shares
"""

stock = ("AAPL", 230, 5)

ticker, price, shares = stock

print(f'Ticker: {ticker}\n'
      f'Position value: {price * shares}')
