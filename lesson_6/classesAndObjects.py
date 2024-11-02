# Основні поняття ООП:
from tkinter.font import names


# класи, об'єкти, атрибути, методи

# 1. Класи (Classes):
#  - Класи є шаблонами або формами, за допомогою яких визначаються об'єкти.
#  - Вони описують структуру та поведінку об'єктів, які належать до цього класу.
#  - Класи містять атрибути (змінні) та методи (функції), які можна використовувати для створення та взаємодії з обʼєктами.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

# 2. Об'єкти (Objects):
#  - Об'єкти - це конкретні екземпляри класів, створені на основі класу.
#  - Вони мають власні атрибути та можуть викликати методи, визначені у відповідному класі.
#  - Об'єкти реалізують концепцію інкапсуляції, яка дозволяє зберігати дані та функції, які їх опрацьовують, разом у одному
# обʼєкти.

person1 = Person('Alice', 30)
person2 = Person('Bob', 25)

# 3. Атрибути (Attributes):
#  - Атрибути - це змінні, які визначені у класі та призначені для зберігання даних, пов'язаних з об'єктами класу.
#  - Вони визначають стан об'єкта та представляють його характеристики.
#  - Атрибути можуть бути публічними, приватними або захищеними, залежно від їх видимості.

print(person1.name) # Alica
print(person2.age) # 25

# 4. Методи (Methods):
#  - Методи - це функції, які визначені у класі та призначені для виконання операцій над об'єктами цього класу.
#  - Вони реалізують поведінку об'єктів класу та використовують атрибути для виконання різних операцій.
#  - Методи можуть бути публічними (доступними ззовні), приватними (доступними лише в межах класу) або
# захищеними (доступними для підкласів)

print(person1.greet()) # Hello, my name is Alice and I am 30 years old



#--------------------------------------------------------------------------------------------------------------------

# Практика

class Human:
    """ Class for creation persons""" # дот нотейшн, док стрінга (у трьох кавичках), опис для чого клас
    name = 'Tom'
    age = 18
    high = 180

print(Human.name, Human.age)
Human.age = 40
print(Human.age)

print(Human.__dict__) # показує все що лежить у класі
# {'__module__': '__main__', 'name': 'Tom', 'age': 40, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}

human1 = Human() #створюємо екземпляр класу
print(human1) # <__main__.Human object at 0x1014b2df0> - ссилається на об'єкт класу хьюмен і показує яку займає пам'ять
print(human1.name, human1.age, human1.high)

human2 = Human()
human2.is_animal = False # присвоюється екземпляру класу, у Human цього атрибуту немає
print(human2.__dict__) # {'is_animal': False}

# вбудовані функції для роботи з класами
print(getattr(person1, 'name')) # Alice
print(getattr(person1, "where_is" , False)) # False - якщо не впевнені чи є такий атрибум третім параметром можна задати значення

human1.age = 51
human1.color = 'orange'
print(human1.__dict__) #{'age': 51, 'color': 'orange'}

setattr(human1, 'high', 100) # поміняли значення з 180 на 100
print(human1.high)

print(hasattr(human1, 'name')) # - True , метод щоб перевірити чи є у класі чи об'єкті класу якийсь атрибут
print(hasattr(human1, 'some_attr')) # False
print('--------------')
# видалення атрибутів
del Human.high
print(hasattr(Human, 'high')) # False
delattr(Human, 'age')
print(hasattr(Human, 'age')) # False
print(Human.__dict__) # залишився тільки name

# getattr() - якщо треба прочитати атрибут, що в ньому
# setattr() - змінити атрибут
# hasattr() - переконатись що атрибут є
# delattr() - перед видаленням треба переконатись що він є, неіснуючий дасть помилку

print(Human.__doc__) # показує анотацію до класу - '__doc__': ' Class for creation persons'

#--------------------------------------------------------------------------------------------------------------------

# Ініціалізація об'єктів через конструктор
# Ініціалізація об'єктів через конструктор - це процес надання початкових значень атрибутам об'єкта під час
# його створення. У багатьох об'єктно-орієнтованих мовах програмування, таких як Python, це зазвичай
# реалізовано за допомогою спеціального методу, відомого як конструктор класу.
# У Python цей метод має ім'я __init__

class PersonInit:
    def __init__(self, name, age):
        self.name = name
        self.age = age

personInit1 = PersonInit('Mark', 23)
personInit2 = PersonInit('Jake', 34)

print(""
      "---------------------"
      "")
# У цьому прикладі конструктор __init__ класу Person приймає два аргументи: name і age. Після створення
# об'єкта класу Person, конструктор встановлює значення цих атрибутів за допомогою переданих аргументів.
# При створенні об'єктів person1 і person2 ми передаємо їхні імена і вік у конструктор, і ці значення зберігаються
# в атрибутах name і age відповідно.
# Конструктори дозволяють задати початковий стан об'єктів та ініціалізувати їх атрибути, щоб об'єкти були
# готові до використання при їхньому створенні.

#--------------------------------------------------------------------------------------------------------------------

# практика

class Character:
    """ Class to describe book characters """

    def __init__(self, name, role, appearance, goals, obstacles):
        self.name = name
        self.role = role
        self.appearance = appearance
        self.goals = goals
        self.obstacles = obstacles

    def print_attrs(self):
        print(self.name, self.role, self.appearance, self.goals, self.obstacles)

character1 = Character(
    'Kate',
    'main',
    'redhead, sea blue-green eyes, freckles, 23 yo',
    'save Ann`s library',
    'ghosted by past, hated or despised by family and everyone else, but need to come back'
)

character1.print_attrs()


class Point:
    """Class for creating and setting coords"""

    def __init__(self, x ,y, z):
        self.x = x
        self.y = y
        self.z = z
        self.get_attrs() # щоб не викликати ці функції вручну за межами класу для кожного екземпляру, автоматично запустить ці функції
        self.check_coords()

    def check_coords(self): # перевірити щоб координати були > 0
        for attr in self.__dict__:
            if getattr(self, attr, False) < 0 and not isinstance(self.__dict__[attr], str): # дістати атрибут, якщо немає призначити йому False, перевірити чи атрибут не менше 0 і чи не є строкою
                setattr(self, attr, 0)
                print('Coord can`t be less than 0')
            elif getattr(self, attr, False) > 100 and not isinstance(self.__dict__[attr], str):
                setattr(self, attr, 100)
                print('Coord can`t be greater than 100')
        print('out of condition ', self.__dict__)

    def get_attrs(self):
        print('get attrs ------- ', self.__dict__)

    def set_attrs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.check_coords() # автоматично перевірити знову після зміни атрибутів
        print('set attrs ------- ', self.__dict__)

point1 = Point(-1,101,50)
point1.get_attrs() # {'x': -1, 'y': 101, 'z': 50}
point1.check_coords()
# Coord can`t be less than 0 - for -1
# Coord can`t be greater than 100 - for 101
# >=0 and <=100  {'x': 0, 'y': 100, 'z': 50} - for 50

point1.set_attrs(1000, 1000, -5) # {'x': 1000, 'y': 1000, 'z': -5}
point1.get_attrs() # get attrs -------  {'x': 1000, 'y': 1000, 'z': -5}
point1.check_coords()
# Coord can`t be greater than 100
# Coord can`t be greater than 100
# Coord can`t be less than 0

print('--------------------------------------')
# після додавання функцій get_attrs, check_coords в ініціалізацію

point2 = Point(-7,340,20)
point2.set_attrs(2000, 23, 21)
# автоматично з ініціалізації get_attrs() -        get attrs -------  {'x': -7, 'y': 340, 'z': 20}
# автоматично з ініціалізації check_coords() -     Coord can`t be less than 0,Coord can`t be greater than 100, out of condition  {'x': 0, 'y': 100, 'z': 20}
# автоматично з set_attrs викликає check_coords() -     Coord can`t be greater than 100, out of condition  {'x': 100, 'y': 23, 'z': 21}, set attrs -------  {'x': 100, 'y': 23, 'z': 21}
