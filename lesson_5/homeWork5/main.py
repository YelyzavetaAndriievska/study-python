# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і
# використовує його функції для виконання обчислень. Попросіть користувача
# ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.

import calculator
import utilities

def calculation(n1, n2, type):
    if type == 'add':
        return calculator.add(n1, n2)
    if type == 'subtract':
        return calculator.subtract(n1, n2)
    if type == 'multiply':
        return calculator.multiply(n1, n2)
    if type == 'divide':
        return calculator.divide(n1, n2)

result = calculation(20, 5, 'divide')
print(result) # 4.0

numbers = [4, 6, 3, 8, 5]

utilities.calculate_average(numbers) # 5.2
utilities.find_max(numbers) # 8