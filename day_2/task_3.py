"""
Дано:

text = "   Python is very powerful   "

Сделай последовательно:

Убери пробелы по краям.
Замени "powerful" на "useful".
Разбей получившуюся строку на список слов.
Выведи получившийся список.
Выведи первый элемент списка.
"""

text = "   Python is very powerful   "

text = text.strip()
text = text.replace("powerful", "useful")
text = text.split()
print(text)
print(text[0])