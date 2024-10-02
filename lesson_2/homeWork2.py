#1 Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
hw_str = 'home work'
print(type(hw_str))

hw_num = 5
print(type(hw_num))

hw_float = 2,5
print(type(hw_float))

hw_bool = True
print(type(hw_bool))

hw_lst = [1, 2, 3]
print(type(hw_lst))

hw_dct = {'fruit' : 'banana', 'animal': 'cat'}
print(type(hw_dct))

hw_tpl = (1, 2, 3)
print(type(hw_tpl))

hw_none = None
print(type(hw_none))

#2 Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки,
# словники і кортежі

num1 = 1
num2 = 8
num3 = num1 + num2 #9
num4 = num2 - num1 #7
num5 = num3 / 3 #3.0
num6= num3 // 3 #3
num7 = num5 * num3 #27.0
num8 = num2 ** num6 #512
num9 = 12 % 5 #2

more = num4 > num6
less = num1 < num8

is_equal = num4 == 7 and num8 == 512
is_equal = num4 == 3 or num8 == 512

lst_and_dct = 'fruit' in hw_dct and hw_lst[1] !=5
hw_bool = more and less

# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
numToStr = str(num_str)

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
# усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
message = message.replace('y', '0')
message = message.replace('i', '1')

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
split_test = split_test.split()
string_join = ' '.join(split_test)

#  4. Визначити довжину рядку string_join за допомогою функції len()
string_join_len = len(string_join)

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4,
#  а потім 5
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)

#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9]
#  за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])

#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
list_extend_indx = list_extend.index(6)

#  4. Визначити довжину списку list_append за допомогою функції len()
list_append_len = len(list_append)
print(list_append_len)

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
#  та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print(dict_test.values())
print(dict_test.keys())

#  3. За допомогою функції items() вивести на екран пари ключ - значення
dict_test_items = dict_test.items()
