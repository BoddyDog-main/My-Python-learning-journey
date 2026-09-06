""""
Напиши функцию:
def get_positive_numbers(numbers):
Она должна принять список чисел и вернуть новый список, содержащий только положительные числа.
"""
numbers = [-5, 10, -2, 8, 0, 3]

def get_positive_numbers(numbers):
    positive_numbers = []

    for i in numbers:
        if i > 0:
            positive_numbers.append(i)

    return positive_numbers

print(get_positive_numbers(numbers))