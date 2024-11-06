# Принцип наслідування та ого застосування.
# Він дозволяє створювати нові класи на основі існуючих (батьківських) класів, спадкуючи їхні атрибути
# та методи. Це спрощує кодування та сприяє перевикористанню коду. Розглянемо цей принцип на прикладах.
# Приклад 1: Батьківський та підкласи
# Припустимо, у нас є клас Vehicle, який представляє транспортний засіб. У цьому класі є атрибути та методи, які властиві всім
# транспортним засобам:

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print('start engine')

# Тепер ми можемо створити підкласи, наприклад, Car та Motorcycle, які успадковують властивості і методи батьківського класу Vehicle:

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year) # super викликає батьківський ініт
        self.num_doors = num_doors

    def drive(self):
        print('driving the car')

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def ride(self):
        print('riding the motorcycle')

# За допомогою успадкування ми не повторюємо код для властивостей make, model та year, а знову
# використовуємо їх у підкласах. Кожен підклас також може мати свої власні атрибути та методи
# (наприклад, num_doors у Car).



#-------------------------------------------------------------------------------------------------------



# Приклад 2: Поліморфізм через успадкування
# Поліморфізм - це здатність об'єктів різних класів виконувати однакові методи.
# Успадковані методи можуть бути перевизначені у підкласах

class Shape:
    def area(self):
        pass # нічого не робить, для наглядності що цей метод треба переписати при наслідуванні

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

circle = Circle(5)
square = Square(4)

# методи area виконуються у підклассах, бо вони там перевизначені, метод area у батьківському класі при цьому не викликається
print(circle.area()) # 78.5
print(square.area()) # 16

# Обидва класи Circle та Square успадковують клас Shape та перевизначають метод area(). Це дозволяє викликати метод
# area() для об'єктів обох класів, і вони повертають правильні значення площі, незважаючи на різний спосіб обчислення
# площі круга і квадрата






# -------------------------------------------------------------------------------------------------------------------

# практика


class A:
    """Class A"""
    name_a = 'Class A is a parent class'
    is_main_class = True

class B(A):
    """Class B"""
    name_b = 'Class B is a child class'
    is_main_class = False

class C(B):
    """Class C"""
    pass

test_ex = C()
print(test_ex.name_a)
# Class A is a parent class - шукає name_a у класі C, далі в B, далі в A, за порядком наслідування,
# так само з викликом функцій класів, викликає де найближче знаходить


# ------------------------------------------------------------------------------------------------------------------
# наслідування з методом супер

class Transport:
    """it`s a basic class for transport"""

    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color

    def move(self):
        print('here we go')

class BMW(Transport):
    """Class BMW"""

    def __init__(self, type, color, cost=0) -> None:
        super().__init__(type, color)
        self.cost = cost

    def run(self):
        super().move() # так можна викликати батьківський метод
        print('run')

class Bike(Transport):
    """Class Bike"""

    def __init__(self, type, color, wheels_num) -> None:
        super().__init__(type, color)
        self.wheels_num = wheels_num

    def start(self):
        print('start')

    def move(self):
        print(f"{self.type} is moving")


bmw_1 = BMW('car', 'red', 10000)
bmw_1.run()

bike_1 = Bike('bike', 'blue', 2)
bike_1.move()



# ------------------------------------------------------------------------------------------------------------------
# Поліморфізм:
# загальний інтерфейс для різних класів
# Поліморфізм - це один із ключових принципів ООП,
# який дозволяє об'єднати різні класи в єдиний інтерфейс або використовувати об'єкти різних
# класів через спільний інтерфейс. В інших словах, поліморфізм дозволяє використовувати об'єкти
# різних класів так, ніби вони є об'єктами одного і того ж базового класу.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# функція яка використовує поліморфізм
def animal_sound(animal):
    return animal.speak()

cat = Cat()
dog = Dog()

print(animal_sound(cat)) # Meow
print(animal_sound(dog)) # Woof


# Основні ідеї поліморфізму включають:
# • Інтерфейси та абстрактні класи: Ви можете створити спільний
# інтерфейс або абстрактний клас, які містять специфікації методів, які повинні
# бути реалізовані в підкласах. Різні класи можуть реалізовувати ці методи по різному.

# • Перевизначення методів: Підкласи можуть перевизначати (override)
# методи, успадковані від базового класу, для зміни їх поведінки. При цьому,
# хоча інтерфейс методу залишається тим самим, різні підкласи можуть мати
# свої власні реалізації.

# • Використання базового класу: Код може оперувати об'єктами базового
# класу, не знаючи конкретних деталей підкласу. Це дозволяє створювати
# загальні функції та методи, які можна використовувати для обробки об'єктів
# різних класів.





# --------------------------------------------------------------------------------------------------------------
# практика

class Count:
    """Counting something"""

    def __init__(self, count_obj, type_obj, max_elements) -> None:
        self.count_obj = count_obj
        self.type_obj = type_obj
        self.max_elements = max_elements

    def counter(self):
        print(f"type of object {self.type_obj}")
        if isinstance(self.count_obj, (list, dict, str, tuple)): # перевірка чи тип данних один з перечислених
            count = len(self.count_obj)
            if count > self.max_elements:
                print('numbers in your object are too big')
            else:
                print(f'count of elements: {count}')
        else:
            print('not countable object')

    def get_attrs(self):
        print('attrs -', self.__dict__)

    def set_attr(self, attr, value):
       if hasattr(self, attr):
           setattr(self, attr, value)
       else:
           print('check your attrs')

class ListElements(Count):
    """class for list elements"""

    def __init__(self, count_obj, type_obj, max_elements) -> None:
        super().__init__(count_obj, type_obj, max_elements)
        pass

    def counter(self):
        super().counter()
        print('operation ended')

list_ex = ListElements([1, 2, 3, 4], list, 10)
list_ex.counter()
list_ex.set_attr('count_obj', [1, 2, 3, 4, 5, 6])
list_ex.get_attrs()




# ----------------------------------------------------------------------------------------------------------------
# варіант коли є єдиний інтерфейс у базовому класі

class BaseInterface:
    """Class for base interface"""

    def __init__(self) -> None: # -> None це анотація типів. треба використовувати таку форму коли функція нічого не повертає
        pass

    def get_attrs(self) -> None:
        pass

    def print_model(self) -> None:
        pass

    def calculate_price(self) -> None:
        pass

    def call_support(self) -> None:
        pass

class SiteInterface(BaseInterface):
    """class for site interface"""

    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self) -> None:
        print(f'model of site: {self.model}')

    def calculate_price(self) -> None:
        print(f'site price is: {self.price * 2} $')

    def call_support(self) -> None:
        print(f'support number is: {self.number}')


class AppInterface(BaseInterface):
    """class for app interface"""

    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self) -> None:
        print(f'model of app: {self.model}')

    def calculate_price(self) -> None:
        print(f'app price is: {self.price * 2} $')

    def call_support(self) -> None:
        print(f'support number is: {self.number}')

site_user = SiteInterface(12345, 'landing', 500)
app_user = AppInterface(54754, 'android', 2100)

for user in (site_user, app_user):
    user.print_model()
    user.calculate_price()
    user.call_support()
    print('-----------------')
