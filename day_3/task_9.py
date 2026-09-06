"""
Напиши функцию:
def square(number):
Она должна возвращать квадрат числа.
Проверка:
print(square(7))
Ожидается:
49
"""

def square(number, degree):
    return number ** degree

print(f'Задание 1\n'
      f'{square(int(input("Введите число: ")), 
                int(input("Введите степень, в которую возвести число: ")))}\n')

"""
Задание 2 — несколько параметров
Напиши:
def calculate_sum(a, b, c):
Функция должна вернуть сумму трёх чисел.
Проверка:
print(calculate_sum(10, 20, 30))
→ 60
"""

def calculate_sum(a, b, c):
    return a + b + c

print(f'Задание 2\n'
      f'{calculate_sum(int(input("Введите первое число: ")),
                       int(input("Введите второе число: ")), 
                       int(input("Введите третье число: ")))}\n')


"""
Задание 3 — значение по умолчанию
Напиши:
def greet(name="George"):
Функция должна возвращать:
Hello, George!
если имя не передано, и соответствующее приветствие для другого имени.
Проверь:
print(greet())
print(greet("Alex"))
"""

def greet(name="George"):
    return (f"Задание 3 \n"
            f"Hello, {name}!")
print(greet())
#print(greet("Alex"))

"""
Задание 4 — if + return
Напиши функцию:
def check_number(number):
Она должна возвращать:
"positive"  → если число > 0
"negative"  → если число < 0
"zero"      → если число == 0
Проверь все три случая."""

def check_number(number):
    if number > 0:
        return ("Задание 4\n"
                "positive")
    elif number < 0:
        return ("Задание 4\n"
                "negative")
    else:
        return ("Задание 4\n"
                "zero")

print(check_number(int(input("Введите число: "))))

"""
Задание 5 — функция со списком
Дан список:
numbers = [10, 5, 20, 3, 15]
Напиши функцию:
def get_even_numbers(numbers):
Она должна вернуть новый список, содержащий только чётные числа.
Ожидается:
[10, 20]
Исходный список менять нельзя.
"""

numbers = input("Введите числа через пробел: ")
numbers = list(map(int, numbers.split()))

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

print(f'Задание 5: \n{get_even_numbers(numbers)}\n')

"""
Задание 6 — финальный микс 
Дан список цен:
prices = [100, 250, 80, 300, 150]
Напиши функцию:
def get_expensive_prices(prices, min_price=150):
Она должна вернуть новый список всех цен, которые не меньше min_price.
Проверь:
print(get_expensive_prices(prices))
print(get_expensive_prices(prices, 200))
Должно получиться:
[250, 300, 150]
[250, 300]
"""

prices = input("Введите цены через пробел: ")
prices = list(map(int, prices.split()))
min_price = int(input("Введите минимальную цену: "))

def get_expensive_prices(prices, min_price):
    expensive_prices = []
    for price in prices:
        if price >= min_price:
            expensive_prices.append(price)
    return expensive_prices

print(get_expensive_prices(prices))

