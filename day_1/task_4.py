"""
Есть два списка:
python_students = ["Alex", "John", "Mike", "Sarah", "David"]
sql_students = ["John", "Mike", "Emma", "David", "Chris"]
Нужно вывести:
Студентов, которые изучают и Python, и SQL.
Всех студентов, которые изучают хотя бы один из двух языков.
Студентов, которые изучают только Python.
Студентов, которые изучают только SQL."""

python_students = ["Alex", "John", "Mike", "Sarah", "David"]
sql_students = ["John", "Mike", "Emma", "David", "Chris"]

python_set = set(python_students)
sql_set = set(sql_students)

common = python_set & sql_set
one_of = python_set | sql_set
python_only = python_set - sql_set
sql_only = sql_set - python_set

print(f'Студенты, которые изучают и Python, и SQL: {common}\n'
      f'Студенты, которые изучают хотя бы один из двух языков: {one_of}\n'
      f'Студенты, которые изучают только Python: {python_only}\n'
      f'Студенты, которые изучают только SQL: {sql_only}\n')

