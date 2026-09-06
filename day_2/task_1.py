"""
Строки - неизменяемый тип данных
word[0]        # символ по индексу
word[-1]       # последний символ
word[1:4]      # срез
len(word)      # количество символов
text.upper()       # HELLO PYTHON WORLD, не изменяет исходную строку
text.lower()       # hello python world, не изменяет исходную строку
text.capitalize()  # Hello python world
text.title()       # Hello Python World
strip()  #  убрать пробелы с двух сторон
text.lstrip()  # убрать пробелы слева
text.rstrip()  # убрать пробелы справа
replace()  #  заменить часть строки, не изменяет исходную строку
split()  #  разбить строку, преобразует строку в list
find()  #  найти позицию, если ничего не найдено, find() возвращает -1.
count()  #  сколько раз встречается
startswith()  #  начинается ли строка с чего-то, результат — это логическое значение True или False.
Оператор in  #  это не метод, а отдельный оператор, возвращаешь логическое True или False
"""

"""
Есть:
text = "Quant Engineer"
Сделай:
Выведи первый символ.
Выведи последний символ.
Выведи количество символов.
Выведи слово "Quant".
Выведи слово "Engineer".
Выведи строку в обратном порядке.
"""

text = "Quant Engineer"
print(text[0])
print(text[-1])
print(len(text))
print(text[0:5])
print(text[6:14])
print(text[::-1])