# **Завдання 1: Створення класу і об'єктів**
# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)
#
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.
# Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.
# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

sounds = {'cow': 'moo', 'dog': 'woof'}

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        for key, value in sounds.items():
            if key == self.species:
                print(f'{self.species} makes sound {value}')


cow = Animal('Amy', 'cow', '3')
dog = Animal('Mike', 'dog', '5')

cow.make_sound() #cow makes sound moo
dog.make_sound() #dog makes sound woof


# **Завдання 2: Робота з об'єктами**
# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle`
# повинен мати наступні атрибути:
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)
#
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.
# Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
#
# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи
# `calculate_area()`, виведіть площу прямокутників на екран.
#

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(self.width * self.height)

rect1 = Rectangle(10, 10)
rect2 = Rectangle(15, 15)

rect1.calculate_area() # 100
rect2.calculate_area() # 225