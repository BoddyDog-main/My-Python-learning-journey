"""
И у нас есть список:
users = ["Alex", "John", "Alex", "Mike", "John", "Sarah", "Mike"]
Представь, что это список пользователей, которые заходили на сайт.
Твоя задача:
1. Вывести количество всех посещений.
2. Получить set уникальных пользователей.
3. Вывести количество уникальных пользователей.
4. Вывести сам set.
"""

users = ["Alex", "John", "Alex", "Mike", "John", "Sarah", "Mike"]
set_users = set(users)

print(len(users))
print(len(set_users))
print(set_users)