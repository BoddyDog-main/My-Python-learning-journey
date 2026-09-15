"""
Есть:
prices = [100, 200, 150, 300, 250]
Создай список:
doubled_prices, в котором каждая цена умножена на 2.
Ожидается:
[200, 400, 300, 600, 500]
"""

prices = [100, 200, 150, 300, 250]
doubled_prices = [number * 2 for number in prices]
print(doubled_prices)