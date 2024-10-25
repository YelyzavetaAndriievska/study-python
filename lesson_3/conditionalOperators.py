string = 'Hello world!'

if 'Hello' in string:
    print("Hello in string")
elif "world" in string:
    print("world in string")
else:
    print("Word not in string")


a = 10
b = 20

if a >= 10 and b == 20:
    print(a + b)
else:
    print('Wrong condition')


test_list = ['hello', 'test', 1, 2, 3]

if "hello" in test_list and 1 in test_list:
    print('hello 1')
elif 'test' in test_list and 4 not in test_list:
    print('test not 4')
else:
    print('your condition go wrong')

c = 'chat is active'
d = 'count of users'

if len(c) >= b:
    print(c)
elif len(d) <= a:
    print(d)
else:
    print('wrong condition')


user_1 = {
    'name': 'Tom',
    'age': 21,
    'balance': 20000,
    'currency': 'USD',
    'status': True
}

user_2 = {
    'name': 'John',
    'age': 17,
    'balance': 5000,
    'currency': 'EUR',
    'status': False
}

user_3 = {
    'name': 'Karine',
    'age': 30,
    'balance': 100000,
    'currency': 'UAH',
    'status': True
}

list_of_currencies = ['USD', 'GBR', 'UAH', 'EUR']

if user_2['name'] and user_2['age'] >= 18 and user_2['status']:
    if user_2['balance'] >= 10000 and user_2['currency'] in list_of_currencies:
        print(f"Hello! You can create your account, welcome {user_2['name']}")
    elif user_2['balance'] >= 1000 and user_2['currency'] in list_of_currencies:
         print('You need more money')
    else:
        print('not enough money')
elif not user_2['name']:
    print('please add your name to your account info')
elif user_2['age'] < 18:
    print('for registry you have to be 10 yo')
else:
    print('Something went wrong')