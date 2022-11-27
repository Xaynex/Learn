# Задача 1. Функции
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
#
# def func_1(x):
#     return x + 10
#
# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции.
# Пример основного кода:
# print(func_2(func_1, 9))
#
# Результат: 361.
# from typing import Callable
#
#
# def func_1(num: int) -> int:
#     return num + 10
#
#
# def func_2(func: Callable, num):
#     return func(num) * func(num)
#
#
# print(func_2(func_1, 9))

# Задача 2. Таймер
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить скорость
# передачи данных на нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять
# время вам было лень, поэтому возникла идея написать «автотест», который всё сделает сам.
# С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время
# работы переданной функции func и выдаёт ответ на экран.
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.
#
# import  time
# def timer(func,*args):
#
#     def wrap(*args):
#         start=time.time()
#         result=func(*args)
#         end=time.time()
#         print('декорируем эту шалаву')
#         print(f'время за которое выполнилась функция {end-start}')
#         return result
#
#     return wrap
#
#
#
#
# @timer
# def my_func(num):
#     print('зашли и что то сделали')
#     return
#
#
# a=my_func(200)
# print(a)

# Задача 1. Двойной вызов
#
# def decorator(func):
#     def wrap(*args,**kwargs):
#         print('декарируем')
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#     return wrap
#
#
# @decorator
# def hi(num):
#     print('Привет, {}!'.format(num))
#
#
# hi('Tom')

# Задача 2. Таймер 2
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию
# , которая сделала всю работу за вас, что позволило большую часть времени смотреть видео с котиками в интернете.
# Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно написать намного красивее и удобнее.
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.

# import time
#
#
# def timer(func, *args):
#     def wrap(*args):
#         start = time.time()
#         func(*args)
#         end = time.time()
#         print('декоратор тайм')
#         print(f'время за которое выполнилась функция {end - start}')
#         return func
#     return wrap
#
#
# def logging(func, *args):
#
#     print('декоратор без врапа пиздец')
#     return func
#
#
# @timer
# @logging
# def my_func():
#     print('передачи различных данных на множество сайтов')


# my_func()

# Задача 2. Плагины

# plug=dict()
# def registration(func):
#     plug[func.__name__]=func
#     return func
#
#
# @registration
# def say_hi(name):
#     return f'привет {name}'
#
#
# @registration
# def say_bay(name):
#     return f'пока {name}'


# print(plug)
# print(say_hi('tom'))
# 7 сентября 10000
# 19 сентября 10000
# 5 октября 10000
# 22 октября 20000
# 9 ноября 33000
# 24 ноября 20000


# Задача 1. Сэндвич
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные
# ингредиенты вроде салата, помидоров и других. Всё это в свою очередь содержится между двух половинок булочки.
# Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.
# Пример результата работы программы при вызове функции sandwich:
# </----------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>


# def up_bun(func):
#     print('</----------\>')
#     return func
#
#
# def down_bun(func):
#     print('<\______/>')
#     return func
#
#
#
# @down_bun
# @up_bun
# def sandwich():
#     print('#помидоры#')
#     print('--ветчина--')
#     print('~салат~')
#
#
# sandwich()

# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print("<\______/>")
#     return wrapper
#
# def ingredients(func):
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#     return wrapper
#
# def sandwich(food="--ветчина--"):
#     print(food)
#
# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     print(food)
#
#
#
# sandwich()
# import functools
#
# def bread(func):
#     @functools.wraps(func)
#     def wrapper():
#         print()
#         func()
#         print("<\______/>")
#     return wrapper
#
# def ingredients(func):
#     @functools.wraps(func)
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#     return wrapper
#
# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     """документация"""
#     print(food)
#
# #
# #
# #
# # sandwich()
# print(sandwich.__name__)
# print(sandwich.__doc__)

# Задача 1. Как дела?

# import functools
#
#
# def how_are_you(func):
#     @functools.wraps(func)
#     def wrap():
#         print('как дела? Хорошо.')
#         print('А у меня не очень! Ладно, держи свою функцию.')
#         func()
#         return func
#
#     return wrap
#
#
# @how_are_you
# def test():
#     print('<Тут что-то происходит...>')
#
#
# test()

# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
# Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

# import functools
# import time
#
#
# def slow_time(func):
#
#     @functools.wraps(func)
#     def wrap(*args,**kwargs):
#         time.sleep(5)
#         func(*args,**kwargs)
#         return func
#
#     return wrap
#
#
# @slow_time
# def my_func():
#     print('проверка, изменились ли данные на веб-странице ')
#
# while True:
#     my_func()

# Задача 3. Логирование

# Реализуйте декоратор logging, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация. Если во время выполнения
# декорируемой функции возникла ошибка, то в файл function_errors.log записываются названия функции и ошибки.
# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

# import functools
# import datetime
# import random
#
#
# def logging(func):
#     @functools.wraps(func)
#     def wrap(*args, **kwargs):
#         try:
#             if random.randint(1,1) == 1:
#                 raise random.choice([ValueError,
#                                      IndexError,
#                                      TypeError,
#                                      SyntaxError,
#                                      AttributeError])
#             print('название функции', func.__name__)
#             print('документация', func.__doc__)
#             func(*args, **kwargs)
#         except (ValueError, IndexError, TypeError, SyntaxError, AttributeError) as e:
#             print('возникла ошибка', datetime.datetime.today())
#             with open('function_errors.log', 'a') as file:
#                 info = f'название функции {func.__name__}, ошибка {e.__class__.__name__}, время {datetime.datetime.today()}\n'
#                 file.write(info)
#         return func
#
#     return wrap
#
#
# @logging
# def f():
#     print('я функция 1')
#
# @logging
# def ff():
#     print('я функция 2')
#
#
# f()
# ff()

# Задача 4. Дебаг
# Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя
# (вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает.
# После этого выводится результат её выполнения.


# Пример декорируемой функции:
import functools


def decorator(func, *args, **kwargs):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        options_str = ''
        for arg in args:
            options_str = f"'{arg}'"
        for key, value in kwargs.items():
            options_str+=" "
            if isinstance(value,str):
                options_str+=f"'{value}'"
                options_str= options_str.strip()
            if isinstance(value,int):
                options_str += f"{key}={value}"

        print(f"вызывается {func.__name__} ({options_str})")
        call=func(*args, **kwargs)
        print(f'{func.__name__} вернула значение "{call}"')
        print(call)
        print()
        return func

    return wrap


@decorator
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


# Основной код:
print(greeting.a)
greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)


