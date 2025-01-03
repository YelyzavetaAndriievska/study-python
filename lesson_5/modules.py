# Робота з модулями:
# імпорт, створення власних модулів
# Імпорт модулів:
# • У багатьох мовах програмування є можливість імпортувати вбудовані або сторонні
# модулі для використання їх функцій та класів.
# • Для імпорту модулів зазвичай використовують ключові слова, такі як import або require, наприклад

import math # імпортуємо вбудований модуль

result = math.sqrt(25)
print(result) # 5.0

# Створення власних модулів:
# Ви можете створювати власні модулі, щоб організовувати код у ваших програмах та використовувати його в
# різних місцях.
# Для створення власного модуля зазвичай виносьте функції, класи або змінні до окремого файлу з розширенням,
# яке вказує на мову програмування (наприклад, .py для Python або .js для JavaScript).
# Після створення модуля ви можете імпортувати його у свої програми для використання.
# Створимо файл my_module.py з наступним вмістом:

import module.my_module
module.my_module.hello('kate')

# Це лише початок роботи з модулями. У мові програмування існують різні можливості та концепції, пов'язані з
# модулями, такі як простори імен (namespace), пакети (packages), імпорт з аліасами (alias), і багато інших.
# Навчання цих концепцій розширить ваші можливості в програмуванні.


# практика
import turtle #малює та виводить на екран різні лінії

# turtle.speed(1)  #швидкість малювання
# turtle.left(90)
# turtle.forward(150)  #малює вперед
# turtle.left(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(150)

def drawSquare(size, color):
    turtle.speed(1)
    turtle.color(color) #колір яким малює лінії
    turtle.begin_fill() #заливка кольором
    def move(len):
        turtle.forward(len)
        turtle.left(90)
    for _ in range(4): # _ так треба називати змінну якщо ми її не використовуватимемо і вона потрібна лише для ітерації
        move(size)

    turtle.end_fill() #заливка кольором

drawSquare(100, "red") # відкриває окреме вікно і малює квадрат
turtle.goto(200, 200)
drawSquare(200, 'blue')