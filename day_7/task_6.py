"""
Создай функцию:
def calculate_return(initial_price, final_price):
Она должна возвращать доходность:
(final_price - initial_price) / initial_price
Есть данные:
prices = {
    "AAPL": (200, 250),
    "NVDA": (150, 180),
    "MSFT": (400, 420),
    "TSLA": (250, 225)
}
Создай словарь returns через dict comprehension, вызывая calculate_return() для каждой акции.
Ожидается примерно:
{
    "AAPL": 0.25,
    "NVDA": 0.20,
    "MSFT": 0.05,
    "TSLA": -0.10
}

Создай positive_returns, содержащий только акции, у которых доходность больше 10%.
"""


prices = {
    "AAPL": (200, 250),
    "NVDA": (150, 180),
    "MSFT": (400, 420),
    "TSLA": (250, 225)
}

def calculate_return(initial_price, final_price):
    return (final_price - initial_price) / initial_price

"""
positive_returns = {}

for ticker, (initial_price, final_price) in prices.items():
    return_rate = calculate_return(initial_price, final_price)

    if return_rate > 0.1:
        positive_returns[ticker] = return_rate
        print(ticker, return_rate)
код без comprehension 
"""

returns = {
    ticker : calculate_return(initial_price, final_price)
    for ticker, (initial_price, final_price) in prices.items()
}

positive_returns = {
    ticker : calculate_return(initial_price, final_price)
    for ticker, (initial_price, final_price) in prices.items()
    if calculate_return(initial_price, final_price) > 0.1
}


for key, value in positive_returns.items():
    print(key, value)

