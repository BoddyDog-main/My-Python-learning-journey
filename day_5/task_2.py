"""
Ошибки
try - попробуй выполнить часть кода
except - в противном случае выведи ошибку
else выполняется только если ошибки не произошло.

"""

"""
Давай применим это к нашему prices.txt.
Представь, что файл содержит:
100
105
hello
110
115
Напиши программу, которая читает файл и для каждой строки пытается сделать:
price = int(line.strip())
Если строка не является числом — программа должна не завершаться с ошибкой, а вывести:
Invalid price: hello
и продолжить обработку следующих строк.
"""

with open("prices.txt", "r") as file:
    valid = 0
    invalid = 0
    for line in file:
        try:
            price = int(line.strip())
        except ValueError:
            invalid += 1
            print(f'Invalid prices: {line.strip()}')
        else:
            valid += 1
            print(f"Valid price: {price}")
    print(f"\nValid prices: {valid}\n"
          f"Invalid prices: {invalid}\n")

