"""
Теперь сделаем небольшую задачу, которая максимально похожа на реальную обработку данных.

У нас есть portfolio.csv:

ticker,price,shares
AAPL,250,10
NVDA,175,5
MSFT,500,3
TSLA,220,8

Напиши программу, которая:

читает portfolio.csv через csv.DictReader;
рассчитывает value = price × shares для каждой позиции;
создаёт portfolio.json;
записывает туда данные примерно такого вида:
{
    "AAPL": {
        "price": 250,
        "shares": 10,
        "value": 2500
    },
    "NVDA": {
        "price": 175,
        "shares": 5,
        "value": 875
    }
}
в конце программа должна вывести:
Total portfolio value: 6635

После создания portfolio.json снова открой его через json.load() и выведи только акции, стоимость позиции которых больше 1500:

AAPL: 2500
TSLA: 1760
AMD: 1680

Здесь я специально не говорю, использовать ли for, if, dict comprehension или что-то ещё. Выбери сам.
"""

import json
import csv

total = 0
portfolio = {}

with open("portfolio.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ticker = row["ticker"]
        price = int(row["price"])
        shares = int(row["shares"])
        value = price * shares

        total += value

        portfolio[ticker] = {
            "price": price,
            "shares": shares,
            "value": value
        }

with open("portfolio.json", "w") as file:
    json.dump(portfolio, file, indent=4)

with open("portfolio.json", "r") as file:
    stock = json.load(file)

    for ticker, data in stock.items():
        if data["value"] > 1500:
            print(f"{ticker}: {data['value']}")

print(f"Total portfolio value: {total}")