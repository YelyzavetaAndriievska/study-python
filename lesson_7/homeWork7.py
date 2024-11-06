# **Завдання 1: Наслідування**
#
# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`,
# `Motorcycle`, `Bicycle`, тощо. Кожен підклас повинен мати додаткові атрибути та методи,
# які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут
# `fuel_type` та метод `start_engine()`.
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

# **Завдання 2: Поліморфізм**
#
# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний
# засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
#
# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної
# інформації про цей вид транспорту.
#
# Створіть список об'єктів з різних видів транспорту, викличте метод
# `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати
# правильну версію методу для кожного об'єкта.
#

class Vehicle:
    """class for Vehicles"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'{self.model} model - created by {self.make} in {self.year} year')

class Car(Vehicle):
    """car"""

    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self) -> None:
        print('lets ride this car')

    def display_info(self):
        print(f'{self.model} model - created by {self.make} in {self.year} year, it runs on {self.fuel_type}')

class Motorcycle(Vehicle):
    """Motorcycle"""

    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def get_color(self) -> None:
        print(f'your motorcycle is {self.color}')

    def display_info(self):
        print(f'{self.model} model - created by {self.make} in {self.year} year, goes in {self.color} color')

class Bicycle(Vehicle):
    """Bicycle"""

    def __init__(self, make, model, year, prev_owner):
        super().__init__(make, model, year)
        self.prev_owner = prev_owner

    def get_owner(self) -> None:
        print(f'previous owner is {self.prev_owner}')

    def display_info(self):
        print(f'{self.model} model - created by {self.make} in {self.year} year, previously owned by {self.prev_owner}')


car = Car('bmw', 'x76', 1997, 'gas')
motorcycle = Motorcycle('kihu', 'gia3', 2011, 'red')
bicycle = Bicycle('hikerrr', '20x', 2022, 'Jake')

car.display_info() # x76 model - created by bmw in 1997 year, it runs on gas
car.start_engine() # lets ride this car

motorcycle.display_info() # gia3 model - created by kihu in 2011 year, goes in red color
motorcycle.get_color() # your motorcycle is red

bicycle.display_info() # 20x model - created by hikerrr in 2022 year, previously owned by Jake
bicycle.get_owner() # previous owner is Jake
