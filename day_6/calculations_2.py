"""
calculations.py
Создай три функции:
calculate_total(numbers)
calculate_average(numbers)
calculate_sqrt(number)
Первая должна возвращать сумму списка.
Вторая — среднее значение списка.
Третья — квадратный корень числа через math.sqrt().
"""

from math import sqrt

numbers = [10, 20, 30, 40, 50]


def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def calculate_average(numbers):
    average = calculate_total(numbers)/len(numbers)
    return average

def calculate_sqrt(number):
    return sqrt(number)

if __name__ == "__main__":
    print(calculate_total(numbers))
    print(calculate_average(numbers))
    print(calculate_sqrt(25))