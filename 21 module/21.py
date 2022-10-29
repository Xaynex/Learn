# Задача 1. Challenge

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))

# Задача 2. Степень числа

# def power(a, n):
#     if n == 0:
#         return 1
#     return a * power(a, n-1)
#
#
# float_num = 1.5
# int_num = 5
# print(float_num, '**', int_num, '=', power(float_num, int_num))

# Задача 3. Поиск элемента
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def search(site, searched):
#     if searched in site:
#         global find
#         find=True
#         return print(site[searched])
#
#     for tag in site.values():
#         if isinstance(tag, dict):
#             search(tag, searched)
#

# find=False
# searched = 'h2'
# search(site, searched)
#
#
# if find == False:
#    print('нет')

# задача 1
# import random
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list[:], 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
#
# change_dict(common_dict)
# print(common_dict)
# print(nums_list,some_dict,uniq_nums)

# Задача 2. Непонятно!

# Пример 1:
# Введите данные: привет
#
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
#
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536


# string = input()
#
#
# def get_type(self):
#     ru_types = {
#         int: 'int (целое число)',
#         float: 'float (вещественное число)',
#         str: 'str (строка)',
#         tuple: 'tuple (кортеж)',
#         bool: 'bool (логический тип)',
#         list: 'list (список)',
#         dict: 'dict (словарь)',
#         set: 'set множество',
#     }
#     return ru_types.get(type(eval(self)), 'Неизвестный тип')
#
#
# if isinstance(string, (int, float, str, tuple, bool)):
#     try:
#         print('Тип данных', get_type(string))
#     except NameError:
#         print('Строки должны быть в кавычках "" или одинарных')
#     print('Неизменяемый (immutable)')
#
# elif isinstance(string, (list, dict, set)):
#     try:
#         print('Тип данных', get_type(string))
#     except NameError:
#         print('Строки должны быть в кавычках "" или одинарных')
#     print('Изменяемый (mutable)')
#
# print('ID объекта', id(string))

# Задача 1. Работа с файлом

# def ask(question, error='не правильный ввод, введите да или нет', tryy=2):
#     while True:
#         ancwer = input(question).lower()
#         if ancwer == 'да':
#             return 1
#         if ancwer == 'нет':
#             return 0
#         if tryy == 1:
#             print('кличество попыток истекло')
#             break
#         else:
#             print(error)
#             tryy -= 1
#         print('осталось попыток', tryy)
#
#
# ask('Удалить файл? ', error='Так удалить или нет? ', tryy=2)

# Задача 2. Накопление значений

# def add_num(num, lst=None):
#     lst=[]
#     lst.append(num)
#     print(lst)
#
# add_num(5)
# add_num(10)
# add_num(15)

# Задача 3. Помощь другу
# def create_dict(data):
#     template = dict()
#     if isinstance(data, dict):
#         return data
#     if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
#         template[data] = data
#         return template
#     else:
#         return None
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         new_list.append(create_dict(i_element))
#     result = [i for i in new_list if i is not None]
#     return result
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
#
# print(data)


# Задача 1. Challenge 2

# Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой задачу,
# но не сильно связанную с математикой, а именно: написать функцию, которая выводит все числа от 1
# до num без использования циклов. Помогите другу реализовать такую функцию.

# def f(num):
#     if num==0:
#         return 1
#     f(num-1)
#     print(num)
#
# f(10)

# Задача 2. Свой zip 2

# def zip_2(*args):
#     zip_tpl=[]
#     min_len = min(map(len, args))
#     zip_tpl = (list(elem[i] for elem in args) for i in range(min_len))
#     return zip_tpl
#
# a = [{'x': 4}, 'b', 'z', 'd']
# b = (10, {20, }, [30], 'z')
# zip_my = zip_2(a, b)
# print(list(zip_my))


# Задача 3. Ряд Фибоначчи Числа Фибоначчи — это ряд чисел, в котором каждое следующее число равно сумме двух
# предыдущих: 1, 1, 2, 3, 5, 8, 13, … Пользователь вводит num_pos. Напишите функцию, которая выводит число,
# которое стоит на позиции num_pos в ряде Фибоначчи.
#
# Пример 1:
# Введите позицию числа в ряде Фибоначчи: 6
# Число: 8
#
# def f(num_pos, lst=[1, 1]):
#     [lst.append(lst[i - 1] + lst[i]) for i in range(1, num_pos + 1)]
#     return lst[num_pos-1]
#
# print(f(10))

# Задача 4. Поиск элемента 2
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
# #
# #
# def find(structure, key, depth):
#     if depth>0:
#         for tag in structure:
#             if tag == key:
#                 return tag, structure[tag]
#             elif isinstance(structure[tag], dict):
#                 result = find(structure[tag], key, depth-1)
#                 if result:
#                     break
#         else:
#             result = 'такого ключа нет'
#         return result
# #
# #
# key = 'p9'
# depth = 3
# a = find(site, key, depth)
# print(a)

# Задача 5. Ускоряем работу функции
# def calculating_math_func(data,saved=dict()):
#     if data not in saved:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         result /= data ** 3
#         result = result ** 10
#         saved[data]=result
#         return result
#     else:
#         return saved[data]
#
# print(calculating_math_func(5))
# print(calculating_math_func(5))


# задача 6

# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам {} недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на {}}',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }
#
# def create(structure,product_name):
#     for tag in structure:
#         if tag == 'title':
#             structure[tag] = 'Куплю/продам {} недорого'.format(product_name)
#             return structure[tag]
#         if tag == 'h2':
#             structure[tag] = 'У нас самая низкая цена на {}'.format(product_name)
#             return structure[tag]
#         elif isinstance(structure[tag], dict):
#             create(structure[tag],product_name)
#     else:
#         return structure
#
#
#
# n=int(input('сколько будет сайтов '))
# for i in range(2):
#     product_name=input('имя товара ')
#     a=create(site,product_name)
#     for i in a:
#         print(i)
#         for ii in a[i]:
#             print(' ',ii)
#             for iii in a[i][ii]:
#                 print('     ',iii, '"',a[i][ii][iii],'"')
# def my_sum(*args):
#     result = 0
#     for i in range(len(args)):
#         result += args[i]
#     return result

# Задача 7. Продвинутая функция sum
# def my_sum(*args, result=0):
#     for i in args:
#         if isinstance(i, int):
#             for i in range(len(args)):
#                 result += args[i]
#             return result
#         else:
#             for ii in i:
#                 if isinstance(ii, int):
#                     result += ii
#                 else:
#                     result = my_sum(ii, result=result)
#         return result
#
#
# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, 2, 3, 4, 5))

# Задача 8. Список списков 2
# Мы уже работали с многомерными списками и решали задачи, где с помощью list comprehensions
# «выпрямляли» его в один. Однако такой фокус не пройдёт, если у элементов разные уровни вложенности
# и этих списков неограниченное количество.
#
# Дан вот такой список:
#
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
#
# Напишите рекурсивную функцию, которая раскрывает все вложенные списки, то есть оставляет только внешний список.
#
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#
# Подсказка: можно возвращать списки и срезы списков.

# def open(list,open_list=[]):
#     for i in list:
#         if isinstance(i, int):
#             open_list.append(i)
#         else:
#             open_list = open(i)
#     return open_list
#
#
# lst=open(nice_list)
# print(lst)

