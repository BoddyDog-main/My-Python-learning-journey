"""
Задание 1

Создай prices.txt:

100
250
hello
80
300
abc
150

Напиши программу, которая читает файл и выводит только корректные цены.
"""

with open('prices.txt', 'r') as file:
    for line in file:
        try:
            price = int(line.strip())
            print(price)
        except ValueError:
            continue


"""
Теперь на основе этого же prices.txt сделай счётчики:
Valid prices: 5
Invalid prices: 2
То есть корректные значения увеличивают valid, а строки,
которые не удалось преобразовать в int, увеличивают invalid.
"""

with open('prices.txt', 'r') as file:
    valid = 0
    invalid = 0
    for line in file:
        try:
            price = int(line.strip())
        except ValueError:
            invalid += 1
        else:
            valid += 1
            print(price)
    print(f'\nValid prices: {valid}\n'
          f'Invalid prices: {invalid}\n')


"""
Задание 3 — считаем сумму
Теперь добавим всего одну новую вещь.
Нужно получить:
Total: 880
Причём считать нужно только корректные цены.
У тебя уже есть:
valid = 0
invalid = 0
Добавь третий накопитель и используй его внутри успешной ветки.
sum() не использовать.
Теперь результат нужно сохранить в result.txt.
"""

with open('prices.txt', 'r') as file:
    valid = 0
    invalid = 0
    summary = 0
    for line in file:
        try:
            price = int(line.strip())
        except ValueError:
            invalid += 1
        else:
            valid += 1
            print(price)
            summary += price
    print(f'\nValid prices: {valid}\n'
          f'Invalid prices: {invalid}\n'
          f'Total: {summary}\n')

with open('result.txt', 'w') as file:
    file.write(f'Valid prices: {valid}\n'
               f'Invalid prices: {invalid}\n'
               f'Total: {summary}\n')


"""
Теперь вынесем самую важную часть в функцию.
Напиши:
def calculate_total(filename):
Функция должна:
Открыть переданный filename.
Пройти по всем строкам.
Преобразовать корректные строки в int.
Некорректные строки пропустить.
Вернуть сумму корректных цен через return.
"""

def calculate_total(filename):
    with open(filename, 'r') as file:
        total = 0
        for line in file:
            try:
                price = int(line.strip())
            except ValueError:
                continue
            else:
                total += price
        return total

print(calculate_total('prices.txt'))