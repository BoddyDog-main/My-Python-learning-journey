"""
Есть список сотрудников:
employees = [
    ("Alex", 25, "Python"),
    ("John", 30, "Java"),
    ("Sarah", 22, "Python"),
    ("Mike", 28, "C++")
]
Твоя задача — написать цикл, который для каждого сотрудника выводит:
Name: Alex
Age: 25
Language: Python
И так для каждого.
"""
employees = [
    ("Alex", 25, "Python"),
    ("John", 30, "Java"),
    ("Sarah", 22, "Python"),
    ("Mike", 28, "C++")
]

for name, age, language in employees:
    print(f'Name: {name}\nAge: {age}\nLanguage: {language}\n')