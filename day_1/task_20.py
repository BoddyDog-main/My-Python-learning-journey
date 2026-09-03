"""
итоговая практика

Задание 1 — немного на всё
Есть:
prices = [100, 150, 100, 200, 250, 150, 300]
Нужно:
Узнать, сколько уникальных цен в списке.
Отсортировать цены по возрастанию.
Вывести первые три цены.

Задание 2 — set
Есть два списка:
monday = ["Alex", "John", "Mike", "Sarah"]
tuesday = ["John", "Mike", "David", "Emma"]
Нужно вывести:
Кто был и в понедельник, и во вторник
Кто был только в понедельник
Кто был только во вторник

Задание 3 — tuple
Есть:
stock = ("AAPL", 230, 5)
Распакуй его в:
ticker
price
shares
и выведи:
Ticker: AAPL
Price: 230
Shares: 5

Задание 4 — dict
Есть:
student = {
    "name": "Alex",
    "age": 25,
    "language": "Python"
}
Нужно:
Изменить возраст на 26.
Добавить "city": "Stockholm".
Удалить "language".
Через items() вывести оставшиеся пары.

Задание 5 — вложенная структура
Есть:
portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    },
    "NVDA": {
        "price": 175,
        "shares": 10
    }
}
Используя for и items(), выведи для каждой акции:
AAPL → 1150
MSFT → 1020
NVDA → 1750
"""


# Задание 1
"""
Задание 1 — немного на всё
Есть:
prices = [100, 150, 100, 200, 250, 150, 300]
Нужно:
Узнать, сколько уникальных цен в списке.
Отсортировать цены по возрастанию.
Вывести первые три цены.
"""

prices = [100, 150, 100, 200, 250, 150, 300]
print("Задание 1")
print(len(set(prices)))
prices.sort()
print(prices[:3])

#Задание 2
"""
Задание 2 — set
Есть два списка:
monday = ["Alex", "John", "Mike", "Sarah"]
tuesday = ["John", "Mike", "David", "Emma"]
Нужно вывести:
Кто был и в понедельник, и во вторник
Кто был только в понедельник
Кто был только во вторник
"""
monday = ["Alex", "John", "Mike", "Sarah"]
tuesday = ["John", "Mike", "David", "Emma"]

set_monday = set(monday)
set_tuesday = set(tuesday)

print("\nЗадание 2")
print(set_monday&set_tuesday)
print(set_monday-set_tuesday)
print(set_tuesday-set_monday)

#Задание 3
"""
Задание 3 — tuple
Есть:
stock = ("AAPL", 230, 5)
Распакуй его в:
ticker
price
shares
и выведи:
Ticker: AAPL
Price: 230
Shares: 5
"""

stock = ("AAPL", 230, 5)
ticker, price, shares = stock
print('\nЗадание 3')
print(f'Ticker: {ticker}\nPrice: {price}\nShares: {shares}')

#Задание 4
"""
Задание 4 — dict
Есть:
student = {
    "name": "Alex",
    "age": 25,
    "language": "Python"
}
Нужно:
Изменить возраст на 26.
Добавить "city": "Stockholm".
Удалить "language".
Через items() вывести оставшиеся пары.
"""

student = {
    "name": "Alex",
    "age": 25,
    "language": "Python"
}
student["age"] = 26
student["city"] = "Stockholm"
del student["language"]
print('\nЗадание 4')
for key, value in student.items():
    print(f'{key}: {value}')

#Задание 5
"""
Задание 5 — вложенная структура
Есть:
portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    },
    "NVDA": {
        "price": 175,
        "shares": 10
    }
}
Используя for и items(), выведи для каждой акции:
AAPL → 1150
MSFT → 1020
NVDA → 1750
"""

portfolio = {
    "AAPL": {
        "price": 230,
        "shares": 5
    },
    "MSFT": {
        "price": 510,
        "shares": 2
    },
    "NVDA": {
        "price": 175,
        "shares": 10
    }
}
print("\nЗадание 5")
for key, value in portfolio.items():
    print(f'{key} -> {value["price"]*value["shares"]}')