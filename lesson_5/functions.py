# Визначення функції:
# Визначення функції означає створення нового "блоку" коду, який можна використовувати в програмі. Функція
# може приймати аргументи (вхідні дані) і виконувати конкретну дію або обчислення, після чого може повертати
# результат (якщо необхідно). Відомий також як "підпрограма" або “процедура”.
from dns.rdtypes.util import priority_processing_order


def add_integers(a, b):
    result = a + b
    return result

# Виклик функції:
# Виклик функції - це запуск функції в коді програми. При виклику функції ви передаєте їй аргументи (якщо вони
# потрібні), і функція виконує свій код. Результати роботи функції можуть бути використані в інших частинах
# програми.

sum_int = add_integers(5, 10)
print(sum_int)





def say_hello(username, age):
    print(f'Hello {username}')
    print(f'your age is {age}')

say_hello('Kate', 20)

def print_numbers(start, stop):
    for num in range(start, stop): #range може приймати один аргумент і видавати від нуля но вказаного числа
        # не включаючи його, або може приймати діапазон і віддавати від першого аргументу до останнього,
        # не включаючи його
        print(f"current number is {num}")

print_numbers(1, 11)

# current number is 1
# current number is 2
# current number is 3
# current number is 4
# current number is 5
# current number is 6
# current number is 7
# current number is 8
# current number is 9
# current number is 10

# Параметри функцій : позиційні, іменовані
# Позиційні параметри:
# • Параметри передаються функції в тому порядку, в якому вони визначені у визначенні функції.
# • Значення, яке ви передаєте, відповідає позиції параметра у визначенні функції.
sum_int = add_integers(10, 20)
print(sum_int)
# Іменовані параметри:
# • Параметри передаються функції з вказанням їхніх імен.
# • Ви можете передати параметри у будь-якому порядку, вказавши ім'я параметра і значення, яке ви хочете
# передати.
sum_int = add_integers(a=20, b=30)
print(sum_int)

user_data = {"Kate": 20, 'Dima': 25, "Tom": 11}
list_of_ranges = [(1, 3), (13, 16), (27, 30)]

for name, age in user_data.items():
    say_hello(name, age)
    # Hello Kate
    # your age is 20
    # Hello Dima
    # your age is 25
    # Hello Tom
    # your age is 11

for start_pos, stop_pos in list_of_ranges:
    print_numbers(start_pos, stop_pos)
    # current number is 1
    # current number is 2
    # current number is 13
    # current number is 14
    # current number is 15
    # current number is 27
    # current number is 28
    # current number is 29

def check_connection (username, count_tries, priority):
    print('----------------------------')
    if priority >= 10:
        finish = 5
        for attemt in range(1, count_tries + 1):
            if attemt == finish:
                print('connected')
                break
            print(f'Attemp -  {attemt} to connect {username}')
    elif priority >= 5 and priority < 10:
        finish = 3
        for attemt in range(1, 6):
            if attemt == finish:
                print('connected')
                break
            print(f'Attemp -  {attemt} to connect {username}')
    else:
        print('low priority')

check_connection(count_tries=10, username='Kate', priority=100)