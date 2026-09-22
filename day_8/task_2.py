"""
Создай файл stock.json:

{
    "ticker": "AAPL",
    "price": 250,
    "shares": 10
}

И напиши Python-код, который:

открывает stock.json;
использует json.load();
сохраняет результат в переменную stock;
выводит:
AAPL
250
10
"""

import json

with open("stock.json", "r") as file:
    stock = json.load(file)
    print(stock["ticker"])
    print(stock["price"])
    print(stock["shares"])

"""
Создай словарь:
portfolio = {
    "AAPL": {
        "price": 250,
        "shares": 10
    },
    "NVDA": {
        "price": 175,
        "shares": 5
    }
}

И сохрани его в:

portfolio.json

через json.dump() с:

indent=4
"""

portfolio = {
    "AAPL": {
        "price": 250,
        "shares": 10
    },
    "NVDA": {
        "price": 175,
        "shares": 5
    }
}

with open("stock_result.json", "w") as file:
    json.dump(portfolio, file, indent=4)


"""
У тебя есть portfolio:

{
    "AAPL": {
        "price": 250,
        "shares": 10
    },
    "NVDA": {
        "price": 175,
        "shares": 5
    }
}

Напиши программу, которая:

открывает stock_result.json;
читает его через json.load();
проходит по всем акциям;
считает стоимость каждой позиции:
price × shares
выводит:
AAPL: 2500
NVDA: 875
в конце выводит:
Total: 3375"""

total = 0
with open("stock_result.json", "r") as file:
    stock = json.load(file)
    for key, value in stock.items():
        price = value["price"]
        shares = value["shares"]
        common = price * shares
        print(f"{key}: {common}")
        total += common
print(f'\nTotal: {total}')