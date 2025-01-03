# **Завдання 2: Створення та імпорт власних модулів**
#
# Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі створіть наступні функції:
#
# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.
#
# Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`),
# який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.
#
# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities`
# для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.

# numbers = [4, 6, 3, 8, 5]

def calculate_average(num):
    average = sum(num) / len(num)
    print(average)

# calculate_average(numbers)

def find_max(num):
    num.sort()
    print(num[-1])

# find_max(numbers)