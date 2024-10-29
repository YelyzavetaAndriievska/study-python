# Словники

# Створення словника:
# Словник в Python - це колекція пар ключ-значення, де ключі унікальні та незмінні,
# а значення можуть бути будь-якого типу даних. Словники створюються за допомогою
# фігурних дужок {} або dict(), а пари ключ-значення розділяються двокрапкою.

test_dict = {
    'user': 'Oleg',
    'age': 21,
    'country': 'Poland'
}

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'} # Створення словника
# empty_dict = {} # Порожній словник

# Доступ до значень за ключем:
# Ви можете отримати доступ до значень в словнику, вказавши ключ у квадратних дужках або
# за допомогою методу .get().
# name = my_dct['name'] # Отримання значення за ключем 'name'
# age = my_dict.get('age') # Отримання значення за ключем 'age' за допомогою методу .get()

print(test_dict['user'], test_dict['age'], test_dict.get('country'))
print(test_dict.get('animal', 'key not found')) #key not found якщо ключа не існує можна задати дефолтне значення

# Зміна значень за ключем:
# Значення в словнику можна змінювати, вказавши нове значення за існуючим ключем:
# my_dict['age'] = 31 # Зміна значення 'age' на 31

test_dict['age'] = 30

# Додавання нових пар ключ-значення:
# Для додавання нової пари ключ-значення просто вказуйте новий ключ та відповідне значення:
# my_dict['country'] = 'USA' # Додавання нового ключа 'country' зі значенням ‘USA'

test_dict['animal'] = 'cat'

# Видалення пар ключ-значення:
# Ви можете видалити пару ключ-значення за ключем за допомогою оператора del або методу .pop():
# del my_dict['city'] # Видалення ключа 'city' із словника
# country = my_dict.pop('country') # Видалення та отримання значення за ключем 'country'

animal = test_dict.pop('animal')
print(animal)

# Методи словника

# clear(): Видаляє всі пари ключ-значення з словника і робить його порожнім.
my_dict = {'name': 'John', 'age': 30}
my_dict.clear() # Зараз my_dict порожній словник - {}

# copy(): Створює копію словника.
# original_dict = {'name': 'John', 'age': 30}
# new_dict = original_dict.copy() # Створить копію original_dict, яка буде присвоєна змінній new_dict

copy_test = test_dict.copy() #{'user': 'Oleg', 'age': 30, 'country': 'Poland'}

# get(key, default=None): Повертає значення, якщо ключ існує в словнику, інакше повертає значення за замовчуванням (default, за замовчуванням None).
age = copy_test.get('age') # Повертає 30
country = my_dict.get('country', 'USA') # Повертає 'USA', оскільки ключ 'country' відсутній

# items(): Повертає усі пари ключ-значення словника у вигляді кортежів.
for key, value in test_dict.items():
    print(f" Key: {key}, Value: {value}")

    # Key: user, Value: Oleg
    # Key: age, Value: 30
    # Key: country, Value: Poland

# my_dict = {'name': 'John', 'age': 30}
# items = my_dict.items() # Повертає [('name', 'John'), ('age', 30)]

# keys(): Повертає список усіх ключів у словнику.
for item in test_dict:
    print(item) # user age country - по дефолту працює з keys(), видає тільки ключі

# my_dict = {'name': 'John', 'age': 30}
# keys = my_dict.keys() # Повертає ['name', ‘age']

# values(): Повертає список усіх значень у словнику.
# my_dict = {'name': 'John', 'age': 30}
# values = my_dict.values() # Повертає ['John', 30]

for item in test_dict.values():
    print(item) #Oleg 30 Poland

# pop(key, default=None): Видаляє і повертає значення, що відповідає ключу. Якщо ключ не існує і вказано значення за замовчуванням, то повертає значення за замовчуванням.
# age = my_dict.pop('age') # Видаляє ключ 'age' і повертає 30
# country = my_dict.pop('country', 'USA') # Не видаляє ключ 'country' і повертає ‘USA'

wrong_key = copy_test.pop('currency', 'key not found') # не знайшло currency і повернуло дефолтне значення
print(wrong_key) #key not found

# update(iterable): Оновлює словник, додаючи пари ключ-значення із іншого
# ітерабельного об'єкту (зазвичай, іншого словника).
# my_dict = {'name': 'John', 'age': 30}
# my_dict.update({'city': 'New York', 'country': 'USA'}) # Оновлює словник з новими парами

dict_update = {
    'new_role': 'admin',
    'salary': 10000
}

print(copy_test) # {'user': 'Oleg', 'age': 30, 'country': 'Poland'}
copy_test.update(dict_update)
print(copy_test) # {'user': 'Oleg', 'age': 30, 'country': 'Poland', 'new_role': 'admin', 'salary': 10000}