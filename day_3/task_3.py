"""
У тебя уже есть:
def add(a, b):
    return a + b
Создай функцию:

def multiply(a, b):
которая возвращает произведение.
А затем получи результат:
multiply(add(2, 3), 4)
"""

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(multiply(add(2, 3), 4)) # обращаемся к другой функции

