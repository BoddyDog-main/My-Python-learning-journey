"""
Напиши функцию:
def get_max(numbers):
Она должна принимать список чисел и возвращать самый большой элемент.
"""

def get_max(numbers):
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number

numbers = [10, 50, 30, 20, 40]

print(get_max(numbers))


