"""
Напиши функцию:
def check_age(age):
Она должна:
вернуть "Adult", если age >= 18
вернуть "Minor", если age < 18
"""

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(15))