"""
Работа с файлами
file = open("prices.txt", "r")
"prices.txt" — имя файла;
"r" — режим read, то есть чтение.
content = file.read()
print(content)
file.close()
Почему нужно закрывать файл?
Потому что open() создаёт соединение Python с файлом.
Когда закончили работу, это соединение нужно закрыть.
with open("prices.txt", "r") as file:
    content = file.read()
    print(content)
"r" → read     → чтение
"w" → write    → запись
"a" → append   → добавление в конец
"x" → create   → создание нового файла
Если файл содержит несколько строк, можно использовать:
file.readlines()
"""

"""
Создай в папке day_5 файл:
prices.txt
и положи туда:
100
105
98
110
115
Затем напиши Python-код, который:
Открывает prices.txt для чтения.
Читает все строки.
Выводит их на экран.
Использует именно конструкцию with open(...).
"""

"""with open("prices.txt", "r") as file:
    content = file.read()
    print(content)
    #file.close()  # с конструкцией with не надо использовать close, так как,
    # когда Python выходит из блока with, файл автоматически закрывается.
"""


"""
Используй тот же prices.txt, но теперь:
with open("prices.txt", "r") as file:
получи данные через readlines() и выведи каждую строку отдельно с помощью for.
удали \n в конце каждой строки 
преобразуй в int
выведи сумму всех чисел
создать файл "result.txt"
вывести в него сумму
записать в него с новой строки "Status: completed"
вывести файл в режиме чтения
"""
with open("prices.txt", "r") as file:
    summary = 0
    content = file.readlines()
    for line in content:
        price = int(line.strip())
        summary += price

with open("result.txt", "w") as file:
    file.write(f'Total: {summary}\n')
with open("result.txt", "a") as file:
    file.write(f'Status: completed\n')


with open("result.txt", "r") as file:
    print(file.read())