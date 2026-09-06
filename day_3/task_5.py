"""
Напиши функцию:
def calculate_price(price, quantity, discount=0):
Она должна возвращать итоговую стоимость:
price × quantity − discount
Проверь:
print(calculate_price(100, 5))
print(calculate_price(100, 5, 50))
"""

def calculate_price(price, quantity, discount=0):
    return price * quantity - discount

print(calculate_price(100, 5))
print(calculate_price(100, 5, 50))