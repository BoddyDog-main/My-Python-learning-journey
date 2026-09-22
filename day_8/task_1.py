"""
CSV — это по сути таблица, где значения разделены запятыми.

Создай portfolio.csv с четырьмя акциями из примера и напиши программу, которая:

импортирует csv;
открывает файл через with open();
использует csv.reader;
выводит каждую строку отдельно.

Пока не преобразовывай строки в int и не считай стоимость портфеля.

Переделай свой код на csv.DictReader и для каждой акции выведи:

AAPL: price=250, shares=10
NVDA: price=175, shares=5
MSFT: price=500, shares=3
TSLA: price=220, shares=8


Измени код так, чтобы для каждой акции выводилось:

AAPL: value=2500
NVDA: value=875
MSFT: value=1500
TSLA: value=1760

где:

value = price × shares

Переделай программу так, чтобы она:

выводила стоимость каждой позиции;
в конце выводила:

Total portfolio value: 6635


Переделай свою текущую программу так, чтобы она одновременно:

читала portfolio.csv;
считала value каждой позиции;
печатала позиции на экран;
создавала portfolio_report.csv;
записывала туда заголовок:
"""

import csv
total = 0
with open("portfolio.csv", "r") as file:
    reader = csv.DictReader(file)
    with open("portfolio_report.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["ticker", "price", "shares", "value"])

        for row in reader:
            price = int(row["price"])
            shares = int(row["shares"])
            value = price * shares
            total += value

            print(f"{row['ticker']}: value={value}")

            writer.writerow([row["ticker"], price, shares, value])

print(f"Total portfolio value: {total}")