"""
Задание 1 — индексы и срезы
text = "Quant Engineer"
Выведи:
Q
r
Quant
Engineer
reenignE tnauQ
"""

text = "Quant Engineer"
print(f'Задание 1\n'
      f'{text[0]}\n'
      f'{text[-1]}\n'
      f'{text[0:5]}\n'
      f'{text[6::]}\n'
      f'{text[::-1]}\n')

"""
Задание 2 — методы строк
text = "   python is very powerful   "
Нужно получить:
PYTHON IS VERY USEFUL
То есть программа должна:
Убрать пробелы по краям.
Заменить powerful на useful.
Перевести весь текст в верхний регистр.
"""

text_2 = "   python is very powerful   "
text_2 = text_2.replace("powerful", "useful")
print(f'Задание 2\n'
      f'{text_2.strip().upper()}\n')

"""
Задание 3 — split()
Есть:
text = "AAPL NVDA MSFT TSLA"
Преврати строку в список и выведи:
['AAPL', 'NVDA', 'MSFT', 'TSLA']
Затем отдельно выведи:
AAPL
TSLA
"""

text_3 = "AAPL NVDA MSFT TSLA"
print(f'Задание 3\n'
      f'{text_3.split()}\n'
      f'{text_3.split()[0]}\n'
      f'{text_3.split()[-1]}\n')

"""
Задание 4 — поиск
Есть:
text = "Python is my favorite programming language"
Определи:
Есть ли "programming" в строке.
На каком индексе начинается "language".
Сколько раз встречается буква "o".
Начинается ли строка с "Java".
Заканчивается ли строка на "language".
"""

text_4 = "Python is my favorite programming language"
print(f'Задание 4\n'
      f'Есть ли "programming" в строке: {"programming" in text_4}\n'
      f'На каком индексе начинается "language": {text_4.find("language")}\n'
      f'Сколько раз встречается буква "o": {text_4.count("o")}\n'
      f'Начинается ли строка с "Java": {text_4.startswith("Java")}\n'
      f'Заканчивается ли строка на "language": {text_4.endswith("language")}\n')

"""
Задание 5 — f-string
Есть:
ticker = "aapl"
price = 245.6789
shares = 4
Выведи:
Ticker: AAPL
Price: 245.68
Position value: 982.72
"""

ticker = "aapl"
price = 245.6789
shares = 4

print(f'Задание 5\n'
      f'Ticker: {ticker.upper()}\n'
      f'Price: {price:.2f}\n'
      f'Position value: {price*shares:.2f}\n')

"""
Задание 6 — маленький микс 
Есть:
data = "   AAPL,245.50,4   "
Нужно получить:
Ticker: AAPL
Price: 245.50
Shares: 4
Position value: 982.00
"""

data = "   AAPL,245.50,4   "
data = data.strip().split(',')
print('Задание 6\n'
      f'Ticker: {data[0]}\n'
      f'Price: {data[1]}\n'
      f'Shares: {data[2]}\n'
      f'Position value: {float(data[1])*float(data[2]):.2f}\n')