"""
Напиши программу, которая:
value = input("Введите число: ")
пытается преобразовать его в int.
Если пользователь ввёл число:
Valid number: 25
Если ввёл что-то вроде hello:
Invalid number
И в любом случае в конце должна появиться:
Processing finished
"""

value = input("Введите число: ")

try:
    value = int(value)
    print(f'Valid number: {value}')
except ValueError:
    print("Invalid number")
finally:
    print("Processing finished")