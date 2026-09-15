"""
Задание 1
Дан список:
prices = [100, 250, 80, 300, 150, 420]
Создай high_prices, содержащий только цены от 200 и выше, через list comprehension.
"""

prices = [100, 250, 80, 300, 150, 420]
high_prices = [price for price in prices if price >= 200]
print(f'Задание 1:\n{high_prices}')

"""
Задание 2
Дан:
prices = [100, 250, 80, 300, 150, 420]
Создай discounted, где каждая цена уменьшена на 15%.
"""

prices_2 = [100, 250, 80, 300, 150, 420]
discounted = [price*0.85 for price in prices_2]
print(f'\nЗадание 2:\n{discounted}')

"""
Задание 3
Есть:
prices = {
    "AAPL": 250,
    "NVDA": 175,
    "MSFT": 500,
    "TSLA": 220,
    "AMD": 140
}
Создай high_prices через dict comprehension, оставив акции с ценой не меньше 200.
"""

prices_3 = {
    "AAPL": 250,
    "NVDA": 175,
    "MSFT": 500,
    "TSLA": 220,
    "AMD": 140
}

high_prices = {
    ticker : price
    for ticker, price in prices_3.items()
    if price >= 200
}
print('\nЗадание 3:')
for key, value in high_prices.items():
    print(f'{key}: {value}')

"""
Задание 4
Есть:
returns = {
    "AAPL": 0.12,
    "NVDA": -0.03,
    "MSFT": 0.08,
    "TSLA": -0.10,
    "AMD": 0.15
}
Создай positive_returns, где останутся только доходности больше 0.
"""

returns = {
    "AAPL": 0.12,
    "NVDA": -0.03,
    "MSFT": 0.08,
    "TSLA": -0.10,
    "AMD": 0.15
}

positive_returns = {
    ticker : price
    for ticker, price in returns.items()
    if price > 0
}

print("\nЗадание 4:")
for key, value in positive_returns.items():
    print(f'{key}: {value}')

"""
Задание 5
Есть:
prices = {
    "AAPL": (200, 250),
    "NVDA": (150, 180),
    "MSFT": (400, 420),
    "TSLA": (250, 225),
    "AMD": (100, 130)
}
Напиши функцию:
def calculate_return(initial_price, final_price):
и создай через dict comprehension словарь доходностей.
"""

prices_4 = {
    "AAPL": (200, 250),
    "NVDA": (150, 180),
    "MSFT": (400, 420),
    "TSLA": (250, 225),
    "AMD": (100, 130)
}

def calculate_return(initial_price, final_price):
    return (final_price - initial_price)/initial_price

returns_dict = {
    ticker: calculate_return(initial_price, final_price)
    for ticker, (initial_price, final_price) in prices_4.items()

}

print("\nЗадание 5:")
for key, value in returns_dict.items():
    print(f'{key} -> {value}')


"""
Используй:
prices = {
    "AAPL": (200, 250),
    "NVDA": (150, 180),
    "MSFT": (400, 420),
    "TSLA": (250, 225),
    "AMD": (100, 130)
}
Нужно получить словарь только тех акций, доходность которых выше 10%.

"""

prices_6 = {
    "AAPL": (200, 250),
    "NVDA": (150, 180),
    "MSFT": (400, 420),
    "TSLA": (250, 225),
    "AMD": (100, 130)
}

final_mix = {
    ticker : calculate_return(initial_price, final_price)
    for ticker, (initial_price, final_price) in prices_6.items()
    if calculate_return(initial_price, final_price) > 0.1
}

print('\nЗадание 6:')
for key, value in final_mix.items():
    print(f'"{key}": {value}')

"""
Вариант через for
final_mix = {}

for ticker, (initial_price, final_price) in prices_6.items():
    return_rate = calculate_return(initial_price, final_price)

    if return_rate > 0.1:
        final_mix[ticker] = return_rate
"""