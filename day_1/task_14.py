"""
Словари - изменяемый тип данных
stock["price"]              # получить
stock["company"] = "Apple"  # добавить
stock["price"] = 240        # изменить
del stock["shares"]         # удалить
student.keys()    # ключи
student.values()  # значения
student.items()   # ключ + значение
student.get()     # безопасно получить значение
"""
"""
Самостоятельно создай:

student = {
    "name": "Alex",
    "age": 25,
    "language": "Python"
}

И сделай последовательно:

Выведи имя.
Выведи возраст.
Измени возраст на 26.
Добавь ключ "city" со значением "Stockholm".
Удали ключ "language".
Выведи итоговый словарь.
"""

student = {
    "name": "Alex",
    "age": 25,
    "language": "Python"
}
print(f"имя: {student["name"]}\n"
      f"возраст: {student["age"]}\n")
student["age"] = 26
student["city"] = "Stockholm"
del student["language"]
print(student)

print(student.items())