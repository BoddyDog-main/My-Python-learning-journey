"""
Создай в main.py список:
returns = [0.05, -0.02, 0.03, 0.01, -0.01]
Используй модуль statistics и выведи:
среднее значение через mean();
медиану через median().
Для этого можешь использовать:
from statistics import mean, median
"""
from statistics import mean, median, pstdev
returns = [0.05, -0.02, 0.03, 0.01, -0.01]

print(f'{mean(returns)}\n'
      f'{median(returns)}\n'
      f'{pstdev(returns)}\n')