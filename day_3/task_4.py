"""
def power(number, exponent=2):
Она должна возвращать number, возведённое в степень exponent.
Проверь её двумя способами:
print(power(5))
print(power(5, 3))
"""

def power(number, exponent=2):
    return number ** exponent

print(power(5))
print(power(5, 3))