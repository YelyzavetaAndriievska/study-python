# Цикли: while і for. Ітерування по послідовностям.
# 1. Цикл `while`:
# • - Цикл `while` виконує блок коду, поки виконується певна умова.
# • - Умова обчислюється перед кожним повторенням циклу.
# • - Якщо умова спочатку є `False`, то цикл може навіть не виконатися жодного разу.
# • - Цикл `while` корисний, коли кількість повторень залежить від умови.
# 2. Цикл `for`:
# • - Цикл `for` використовується для ітерування по послідовностям, таким як списки, кортежі, рядки тощо.
# • - Він автоматично перебирає кожен елемент послідовності та виконує блок коду для кожного елемента.
# • - Цикл `for` корисний, коли ви точно знаєте кількість елементів у послідовності або коли потрібно виконати певну дію для
# кожного елемента послідовності.
# 3. Ітерування по послідовностям:
# • - Ітерування означає проходження по послідовності один за одним елементом.
# • - У Python ітерування зазвичай використовується для обробки кожного елемента послідовності окремо.
# • - Це може бути важливим для виконання операцій, таких як обробка даних у списку, рядку або іншій структурі даних.


test_list = [1, 2, 3, 4, 5, 6]

for num in test_list:
    print(num)

a = 0
while a < 10:
    a += 1
    print(a)

while len(test_list) < 10:
    test_list.append(3)
    print(test_list)

test_list = ['test', 'python', 'code']
for s in test_list:
    print(s, '------<')
    if s == 'test':
        print(s)
    elif s == 'python':
        print(s)
    else:
        print(s)


a = 0
add_list = []

while len(add_list) < 10:
    print(add_list)
    add_list.append(a)
    a += 1
    if len(add_list) == 5:
        print('middle of count')


user_1 = {
    'user_name': 'tester',
    'role': 'admin',
    'account_connection': True
}

user_2 = {
    'user_name': 'junior',
    'role': 'user',
    'account_connection': False
}

user_3 = {
    'user_name': 'middle',
    'role': 'pro_user',
    'account_connection': True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    if not user['account_connection']:
        count_of_tries = 10
        while count_of_tries != 0:
            # if count_of_tries == 5:
            #     user['account_connection'] = True
            #     break # виходить з циклу, йде на наступну ітерацію по списку юзерів
            print("try to connect to user account ")
            count_of_tries -= 1
            if count_of_tries == 5:
                print('middle of count')
                continue # пропускає поточну ітерацію, не виконує наступну строку і йде одразу на наступну ітерацію
            print('tries left - ', count_of_tries)
    if user['role'] == 'admin':
        print(f"hello in system {user['user_name']}")
    else:
        print('wellcome')