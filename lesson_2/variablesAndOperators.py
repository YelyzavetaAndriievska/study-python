# variables

# var can starts with _ or any english letter, number
# can't be reserved word : False, def, if, raise, None, del, import, return, True, elif, in,
# try, and, else, is, while, as, except, lambda, with, assert, finally, nonlocal, yield, break
# for, not, class, form, or, continue, global, pass, async, await

# You can wrap strings in "" or ''. Naming - you can use underscore or camelCase,
# for ex. user_name or userName

# reuse variables
name = "Tom"
# print(name)

name = "Sarah"
# print(name)

# оператори:
#  + додавання, * множення, / ділення,  - віднімання
#  == рівно, != не рівно, < менше, > більше
#  and - і, повертає true, якщо обидва вирази true
#  or - або, повертає true, якщо хоча б один з виразів є true
#  not - не, інвертує значення, змінюючи true на false і навпаки


# арифметичні оператори

# num_1 = 100
# num_2 = 10
# num_3 = num_1 + num_2
# print(num_3)

# num_1 = 100
# num_2 = 10
# num_3 = num_1 - num_2
# print(num_3)

# num_1 = 100
# num_2 = 10
# num_3 = num_1 * num_2
# print(num_3)

# num_1 = 100
# num_2 = 10
# num_3 = num_1 / num_2
# print(num_3)

num_1 = 7
num_2 = 2
# ділить порівну 7/2 = 3,5
num_3 = num_1 / num_2
# ділить цілими числами, показує скільки 2 влазить в 7 = 3
num_4 = num_1 // num_2
#print(num_3, num_4)

num_1 = 5
num_2 = 2
# 5 у 2й ступені = 25
num_3 = num_1 ** num_2
#print(num_3)

num_1 = 7
num_2 = 2
# залишок від ділення = 1. 2ка помістилась у 7 тричі, це 6. 7-6=1
num_3 = num_1 % num_2
#print(num_3)


# логічні оператори

# num = 10
# name = "Tom"
# result = num > 5 and name == "Tom"
# print(result)
#
# num = 10
# name = "Tom"
# result = num < 5 or name == "Tom"
# print(result)
#
# num = 10
# name = "Tom"
# message = "Tom got some money"
# print(name in message)
#
# name = "John"
# message = "You won!"
# print(name not in message)

age = 50
name = "Ira"
animal = "cat"
print(age == 50 and "I" in name and animal != "dog")