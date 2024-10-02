# Вбудовані функції для роботи з типами даних

# Функції для чисел:
# • int(x): Перетворює значення `x` у ціле число (без плаваючої точки).
# • float(x): Перетворює значення `x` у дійсне число (з плаваючою точкою).
num_1 = '1'
print(type(num_1))  #<class 'str'>

num1 = int(num_1)
print(type(num1))  #<class 'int'> 1

num1 = float(num_1)
print(type(num1))  #<class 'float'> 1.0


# Функції для рядків:
# • len(s): Повертає довжину рядка `s`. вертає кількість усіх символів з пробілами у рядку.
# • str(x): Перетворює значення `x` у рядок.

string = 'hello world!'
print(len(string))
string = string.upper()
print(string) #HELLO WORLD!
string = string.lower()
print(string) #hello world!
string = string.capitalize()
print(string) #Hello world!
string = string.replace('!','.')
print(string) #Hello world.
string2 = string.split() #за замовчуванням розбиває по пробілам, можна нічого не передавати
print(string2) #['Hello', 'world.']
string = string.count('o')
print(string) #у на 2 букви 0 в строці
string2 = ' '.join(string2)
print(string2) #роз'єднує список назад в строку переданим пробілом. Hello world.
string = 1
string = str(string) #перетворює значення на строку
print(type(string)) #<class 'str'>


# Функції для списків та кортежів:
# • len(lst): Повертає кількість елементів у списку чи кортежі `lst`.
# • lst.append(x): Додає елемент `x` в кінець списку `lst`.

base_list = [1, 2, 3]
print(len(base_list)) #3
base_list.append(4) #додає елемент у кінець списку
print(base_list) #[1, 2, 3, 4]

base_list.extend([5, 6, 7]) #додає більше одного елементу у кінець списку
print(base_list) # [1, 2, 3, 4, 5, 6, 7]

print(base_list.index(4)) # 3 - 4 на 3 місці бо початок з 0


# Функції для роботи зі словниками:
# • dct.keys(): Повертає список ключів у словнику `dct`.
# • dct.values(): Повертає список значень у словнику `dct`.
# • dct.items(): Повертає список кортежів (ключ, значення) у словнику `dct`.

base_dict = {'name': 'Tom', 'age': 40, 'high': 180}
print(base_dict.keys()) #dict_keys(['name', 'age', 'high'])
print(base_dict.values()) #dict_values(['Tom', 40, 180])
print(base_dict.items()) #dict_items([('name', 'Tom'), ('age', 40), ('high', 180)]) - список з кортежів
print(base_dict['name']) #Tom
print(base_dict.get('name')) #Tom
print(base_dict.get('is_animal', 'No')) #No. Таким чином можна задати значення ключу
# якщо його нема - дефолтне значення для неіснуючого ключа (не додається у оригінальний словник)


