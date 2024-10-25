# ### Умовні конструкції:

# 1. **Перевірка паролю:**
#  Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє,
#  чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123",
#  виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть
#  повідомлення "Неправильний пароль".

user_1 = {
    'password' : 'test'
}

user_2 = {
    'password' : 'password123'
}

users_list = [user_1, user_2]
default_password = 'password123'

for user in users_list:
    if user['password'] == default_password:
        print('Ви увійшли в систему', user['password'])
    else:
        print('Неправильний пароль', user['password'])

# 2. **Визначення днів тижня:**
# Завдання: Створіть програму, яка встановлює номер дня тижня і виводить
# назву відповідного дня тижня. Якщо номер дня недійсний (менше 1 або більше 7),
# виведіть повідомлення про помилку.

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day_number = 0

for day in week:
    day_number += 1
    print(day, ' number = ', day_number)
    if day_number < 1 or day_number > 7:
        print('Error')



# ### Цикли:

# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання
# без використання `input`. Використовуйте умовні конструкції і цикли для розв'язання
# кожного завдання.

# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.

test_num = 5
counter = 0

while counter < 10:
    counter += 1
    print(test_num, "*", counter, "=", test_num * counter)

#
# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.

list_of_numbers = [1, 2, 3]
count = 0

for num in list_of_numbers:
    count += num
    print(count)


# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.

test_num = 4
factorial = 1

while test_num > 1:
    factorial = factorial * test_num
    test_num = test_num - 1

print(factorial)



# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.
list_of_numbers = []
counter = 0

while len(list_of_numbers) < 50:
    counter += 1
    list_of_numbers.append(counter)

for num in list_of_numbers:
   if num % 2 == 0:
       print('even - ', num)

#
# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
#    (Просте число - число яке нарівно ділиться тільки на 1 і на себе)

lower_n = 1
upper_n = 20

for number in range(lower_n, upper_n + 1):
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                break
        else:
            print(number)
