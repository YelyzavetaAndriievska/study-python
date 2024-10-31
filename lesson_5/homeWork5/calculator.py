# **Завдання 1: Робота з функціями**
#
# Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:
#
# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
def add(a, b):
    return a + b
add_result = add(2, 3)
# print(add_result)

# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
def subtract(a, b):
    return a - b
subtract_result = subtract(5, 3)
# print(subtract_result)

# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
def multiply(a, b):
    return a * b
multiply_result = multiply(5, 3)
# print(multiply_result)

# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.
def divide(a, b):
    if b > 0:
      return  a / b
    else:
        print('error')
divide_result = divide(18, 3)
# print(divide_result)
