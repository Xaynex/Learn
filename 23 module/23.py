# Задача 1. Пятый элемент
# В курсе по программированию студенту дали простую задачу: умножить константу (число 42)
# на пятый элемент строки, введённой пользователем. Вот код студента:
#
#
# Модифицируйте этот код, обработав исключения для произвольных входных параметров:
# •	ValueError — невозможно преобразовать к числу,
# •	IndexError — выход за границы списка,
# •	остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.

# BRUCE_WILLIS = 42
#
# try:
#     input_data = input('Введите строку: ')
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
#
# except ValueError:
#     print('невозможно преобразовать к числу')
#
# except IndexError:
#     print('выход за границы списка')
# except:
#     print('ошибка')

# Задача 2. Возраст
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
# Напишите программу, которая считывает файл, даёт имя для каждого возраста
# (можно просто использовать буквы алфавита) и выводит результат в новый файл result.txt в формате «имя — возраст».
# Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:
# 1.	Попытка создания файла, который уже существует.
# 2.	На чтение ожидался файл, но это оказалась директория.
# 3.	Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

# import random
# import string
#
#
# def generate_random_string(length):
#     letters = string.ascii_lowercase
#     rand_string = ''.join(random.choice(letters) for i in range(length))
#     return rand_string
#
#
# my_dict = dict()
# try:
#     file = open('ages.txt', 'r')
#     for i_line in file:
#         name = generate_random_string(5)
#         my_dict[name] = int(i_line.strip('\n'))
# except ValueError:
#     print('Неверный тип данных и некорректное значение')
#
# try:
#     file_result = open('result.txt', 'w')
#     for key, v in my_dict.items():
#         print(key, v)
#         file_result.write('{} {}\n'.format(key, v))
# except FileExistsError:
#     print('файл уже существует')
#
# Задача 1. Простая программа
# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
# Используйте операторы try except else finally. Обработайте возможные ошибки:
# 1.	Проблема при открытии файла.
# 2.	Нельзя преобразовать данные в целое.
# 3.	Неожиданная ошибка.

# import os
#
# file = open('text.txt', 'w')
# try:
#     txt = input('введите строку ')
#     file.write(txt)
#     print('файл успешно записан')
# except (FileNotFoundError,FileExistsError):
#     print('Проблема при открытии файла')
# except TypeError:
#     print('Нельзя преобразовать данные в целое')
# except OSError:
#     print('системная ошибка')
# finally:
#     if os.path.exists('text.txt'):
#         file.close()
#         print('файл закрыт')

# Задача 1. Имена
# file = open('people.txt', 'r')
# count = 0
# total = 0
# try:
#     for name in file:
#         name = name.strip('\n')
#         count += 1
#         if len(name) < 3:
#             raise TypeError('имя меньше чем из трёх букв в {} строке'.format(count))
#         total += len(name)
#     print('длинна символов', total)
# except FileExistsError:
#     print('ошибка')
# finally:
#     file.close()

# Задача 2. Логирование

# chars = set()
#
#
# def f(file):
#     for word in file:
#         word = word.strip('\n')
#         if not word.isalpha():
#             raise ValueError
#         for sym in word:
#             if sym in chars:
#                 chars.remove(sym)
#             else:
#                 chars.add(sym)
#         print(word, end='')
#         print(('- Можно', ' - Нельзя')[len(chars) > 1], 'сделать полиндром')
#         chars.clear()
#
#
# file = open('words.txt')
# try:
#     f(file)
# except ValueError:
#     log = open('errors.log', 'a')
#     log.write('ValueError,в слове встречается число\n')
# finally:
#     file.close()

# Задача 1. Имена 2
# Есть файл people.txt, в котором построчно хранится N имён пользователей.
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение,
# в какой именно строке ошибка возника. Программа при этом не завершается и обрабатывает все имена файла.
# Также при желании можно вывести все ошибки в отдельный файл errors.log.

# line_count = 0
# total = 0
# with open('people.txt', 'r') as people:
#     for name in people:
#         try:
#             line_count += 1
#             name = name.strip('\n')
#             if len(name) < 3:
#                 raise SystemError('ошибка в {0} имени'.format(line_count))
#             total += len(name)
#             print('в {i} имени {a} символов'.format(i=line_count,a=total))
#         except SystemError:
#             print(('ошибка в {0} имени'.format(line_count)))
#
# print('количество символов',total)

# Задача 2. Координаты
# import random
#
#
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return x / y
#
#
# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)
#     return y / x
#
#
# try:
#     with open('coordinates.txt', 'r') as file:
#         for line in file:
#             nums_list = line.split()
#             res1 = f(int(nums_list[0]), int(nums_list[1]))
#             res2 = f2(int(nums_list[0]), int(nums_list[1]))
#             number = random.randint(0, 100)
#             with open('result.txt', 'a') as file_2:
#                 my_list = sorted([res1, res2, number])
#                 for i in my_list:
#                     file_2.write(str(i) + ' ')
#                 file_2.write('\n')
# except ZeroDivisionError:
#     print("ошибка - нельзя делить на 0")

# Задача 3. Счастливое число
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма этих чисел не станет
# больше либо равна 777. Каждое введённое число при этом дозаписывается в файл. Сделайте так,
# чтобы перед дозаписью программа с вероятностью 1 к 13 выбрасывала пользователю случайное исключение и завершалась.
# import random
# summ = 0
#
# try:
#     while summ <= 777:
#         with open('numbers.txt', 'a') as file:
#             num = int(input('введите число '))
#             chance = random.randint(1, 3)
#             if chance == 3:
#                 rnd_exception = random.randint(1, 5)
#                 if rnd_exception == 1:
#                     raise IndexError('Индекс не входит в диапазон элементов.')
#                 elif rnd_exception == 2:
#                     raise GeneratorExit('Порождается при вызове метода close объекта generator.')
#                 elif rnd_exception == 3:
#                     raise ArithmeticError('Арифметическая ошибка.')
#                 elif rnd_exception == 4:
#                     raise FloatingPointError('Порождается при неудачном выполнении операции с плавающей запятой.')
#                 elif rnd_exception == 5:
#                     raise ZeroDivisionError('Деление на ноль.')
#             file.write(str(num) + '\n')
#             summ += num
# except Exception as e:
#     print('вас постигла неудача',e)


# Задача 4. Регистрация
# У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt
# Каждая строка содержит: ИМЯ ИМЕЙЛ ВОЗРАСТ, разделённые пробелами.
# Например:
# Василий test@test.ru 27
#
# Напишите программу, которая проверяет данные из файла для каждой строки:
# •	Присутствуют все три поля.
# •	Поле имени содержит только буквы.
# •	Поле «Имейл» содержит @ и . (точку).
# •	Поле «Возраст» является числом от 10 до 99.
# В результате проверки сформируйте два файла:
# •	registrations_good.log — для правильных данных, записывать строки как есть,
# •	registrations_bad.log — для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
# •	НЕ присутствуют все три поля: ValueError.
# •	Поле имени содержит НЕ только буквы: NameError.
# •	Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.
# •	Поле «Возраст» НЕ является числом от 10 до 99: ValueError.

# def check(name,email,age):
#     print('проверка',name,email,age)
#     if not name.isalpha():
#         raise NameError('Поле имени содержит НЕ только буквы')
#     if not '@' in email or not'.' in email:
#         raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
#     if not 99>=int(age)>10 :
#         raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
#
#
#
#
# try:
#     with open('registrations.txt', 'r') as registrations_file:
#         for _ in registrations_file:
#             a = [x for x in _.split()]
#             name,email,age=a[0],a[1],a[2]
#             check(name,email,age)
#
# except IndexError as e:
#     print('ошибка',e)
#     raise ValueError('не присутствуют все 3 поля')

# Задача 5. Текстовый калькулятор
# def f(file):
#     for expression in file:
#         error = False
#         expression_list = [x for x in expression.split()]
#         oper1, operation, oper2 = expression_list[0], expression_list[1], expression_list[2]
#         if not oper1.isdigit() or not oper2.isdigit():
#             raise ValueError
#         if '+' not in operation and '-' not in operation and '*' not in operation and '/' not in operation:
#             raise ValueError
#         if expression_list[1] == '+':
#             res = int(oper1) + int(oper2)
#             print(res)
#         elif expression_list[1] == '-':
#             res = int(oper1) - int(oper2)
#             print(res)
#         elif expression_list[1] == '/':
#             res = int(oper1) // int(oper2)
#             print(res)
#         elif expression_list[1] == '*':
#             res = int(oper1) * int(oper2)
#             print(res)
#
#
# with open('calc.txt', 'r') as file:
#     try:
#         f(file)
#     except Exception as e:
#         print('ошибка',e)
#     finally:
#         f(file)


import colorama
from colorama import Fore, Back


def get_action():
    choice = -1
    print(Fore.GREEN + 'Доступные действия:')
    print('1 - Посмотреть текущий текст чата;')
    print('2 - Отправить сообщение;')
    print(Fore.WHITE + '0 - Выход.')
    try:
        choice = int(input('> '))
    except ValueError as e:
        print(Fore.RED + Back.YELLOW + 'Ошибка:', Fore.RESET + Back.RESET, ' ', e, sep='')
    return choice


colorama.init()
user = input(Fore.YELLOW + 'Введите имя: ')
action = -1

while True:
    if action not in range(0, 3):
        action = get_action()

    if action == 0:
        break

    elif action == 1:
        try:
            with open('chat.txt', 'r', encoding='utf-8') as f_chat:
                print(Fore.WHITE + Back.RESET, end='')
                for i_message in f_chat:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста.')

    elif action == 2:
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as f_chat:
            f_chat.write(f'{user}: {message}\n')
    action = -1
