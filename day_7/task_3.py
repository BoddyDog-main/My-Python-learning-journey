"""
Дано:
returns = [0.05, -0.02, 0.03, -0.01, 0.07]
Создай список positive_returns, в котором:
положительные значения остаются как есть;
отрицательные заменяются на 0.
Ожидается:
[0.05, 0, 0.03, 0, 0.07]
"""

returns = [0.05, -0.02, 0.03, -0.01, 0.07]
positive_returns = [value if value > 0 else 0 for value in returns]
print(positive_returns)