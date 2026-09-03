"""
Допустим, у нас есть два списка:
monday = ["Alex", "John", "Mike", "Sarah"]
tuesday = ["John", "Mike", "David", "Emma"]
Нужно определить:
1. Кто заходил и в понедельник, и во вторник?
2. Кто заходил хотя бы один раз за эти два дня?
3. Кто заходил только в понедельник, но не во вторник?
"""

monday = ["Alex", "John", "Mike", "Sarah"]
tuesday = ["John", "Mike", "David", "Emma"]

set_monday = set(monday)
set_tuesday = set(tuesday)

print(set_monday & set_tuesday) #пересечение множеств
print(set_monday | set_tuesday) #объединение множеств
print(set_monday - set_tuesday) #разность множеств !важен порядок!
# есть еще операнда ^ - симметричная разность, т.е. элементы, которые есть только в одном из множеств, но не в обоих.
