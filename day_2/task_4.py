"""
Дано:
text = "Python is my favorite programming language"
Определи с помощью подходящих инструментов:
Есть ли в строке "Python"?
На каком индексе начинается "favorite"?
Сколько раз встречается буква "a"?
Начинается ли строка с "Python"?
Заканчивается ли строка на "language"?
"""

text = "Python is my favorite programming language"

print(f'Есть ли в строке "Python": {"Python" in text}\n'
      f'На каком индексе начинается "favorite": {text.find("favorite")}\n'
      f'Сколько раз встречается буква "a": {text.count("a")}\n'
      f'Начинается ли строка с "Python": {text.startswith("Python")}\n'
      f'Заканчивается ли строка на "language": {text.endswith("language")}')