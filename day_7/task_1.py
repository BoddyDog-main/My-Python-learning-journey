"""
словари глубже + list/dict comprehension

dict
expensive = {
    ticker: price
    for ticker, price in prices.items()
    if price > 200
}
# создай словарь из ticker: price для каждого элемента prices, если price > 200

squares = [number ** 2 for number in numbers]
"""

"""
Есть:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Создай новый список squares, содержащий квадраты только чётных чисел.

Ожидается:

[4, 16, 36, 64, 100]

Сделай это именно через list comprehension, без обычного for.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers if number % 2 == 0]
print(squares)
