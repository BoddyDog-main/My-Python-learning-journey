"""
numbers = [10, 20, 20, 30, 20, 40, 50]
Твоя задача:
Узнать, сколько раз встречается 20.
Узнать индекс первого 30.
Удалить один 20.
Добавить 60 в конец.
Развернуть список.
Вывести итоговый список.
"""
numbers = [10, 20, 20, 30, 20, 40, 50]
print(numbers.count(20))
print(numbers.index(30))
numbers.remove(20)
numbers.append(60)
numbers.reverse()
print(numbers)

