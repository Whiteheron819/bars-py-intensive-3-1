"""
Что будет выведено после выполнения кода? Почему?
"""
x = 42


def some_func():
    global x
    x = x + 1
    print(x)


some_func()
print(x)

"""
После выполнения кода будет выведено 43, а потом 43.
В данном случае мы делаем x глобальной, в теле функции прибавляем 1 к x, и выводим её значение.
В первом случае мы обращаемся к функции, прибавляем 1, и выводим получившийся результат.
Во втором мы просто выводим x, но его значение уже изменено.
Если бы мы поменяли местами вывод x и обращение к функции - то было бы 42, 43
"""