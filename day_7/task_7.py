"""
Есть:
numbers = [1, 2, 2, 3, 4, 4, 5, 6]
Создай even_squares через set comprehension, чтобы получить уникальные квадраты только чётных чисел.
"""

numbers = [1, 2, 2, 3, 4, 4, 5, 6]
even_squares = {number ** 2 for number in numbers if number % 2 == 0}
print(even_squares)