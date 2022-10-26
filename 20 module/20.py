# Задача 1. Создание кортежей
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж.
# С помощью метода кортежа определите в нём количество нулей. Выведите на экран третий кортеж и количество нулей в нём.
#
# import random
# tuple_1=tuple([random.randint(0,5) for i in range(5)])
# tuple_2=tuple([random.randint(-5,0) for i in range(5)])
# print(tuple_1)
# print(tuple_2)
#
# tuple_3=tuple_1+tuple_2
# print(tuple_3)
# print(tuple_3.count(0))


# Задача 2. Цилиндр
# import math
#
#
# def count(r, h, s):
#     side = 2 * math.pi * int(r) * int(h)
#     full = side + 2 * int(s)
#     print('Площадь боковой поверхности ', side)
#     print('Полная площадь  ', full)
#
#
# r, h, s = input('введите рудиус, высоту и площидь круга').split()
# count(r, h, s)

# Задача 3. Неправильный код
# import random
#
#
# def change(my_nums):
#     index = random.randint(0, 4)
#     value = random.randint(10, 1000)
#     nums = list(my_nums)
#     nums[index] = value
#     nums = tuple(nums)
#     return nums, value
#
#
# my_nums = (1, 2, 3, 4, 5)
# tuple_1, value1 = change(my_nums)
# tuple_2, value2 = change(my_nums)
# print(tuple_1, value1)
# print(tuple_2, value2)
# print(value1 + value2)

# Задача 1. Саботаж!

# stroka = 'so~mec~od~e'
# for index, sym in enumerate(stroka):
#     if sym == "~":
#         print(index, end='')

# Задача 2. Словари из списков

# import random
# import string
#
# list_1 = ([random.choice(string.ascii_lowercase) for letter in range(10)])
# list_2 = ([random.choice(string.ascii_lowercase) for letter in range(10)])
# print(list_1)
# print(list_2)
#
# dict_1={}
# dict_2={}
# for index, sym in enumerate(list_1):
#     dict_1[index]=sym
# print(dict_1)
#
# for index, sym in enumerate(list_2):
#     dict_2[index]=sym
# print(dict_2)

# Задача 3. Универсальная программа
#
# spisok=[100, 200, 300, 'буква', 0, 2, 'а']
#
# lst=list()
# for index,sym in enumerate(spisok):
#     if index%2==0:
#         lst.append(sym)
#
# print(lst)

# Задача 1. Кризис миновал
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for fruct, price in incomes.items():
#     print(fruct,price)

# Задача 2. Сервер
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }

# for key,values in server_data.items():
#     print(key)
#     for settings, value in values.items():
#         print(' ',settings,value)

# Задача 3. В одну строчку
# print([ii for i,ii in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if ii % 2 == 0])

# Задача 1. Паспортные данные
# В базе данных поликлиники хранятся паспортные данные людей. Хранение реализовано с помощью словаря,
# состоящего из пар «Серия и номер паспорта — фамилия и имя». Серия и номер — составной ключ,
# а фамилия и имя — составное значение.
# #
# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
# Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека.

# s = map(int, input('паспорт ').split())
# s=tuple(s)
# for id, name in data.items():
#     if s == id:
#         print(*name)
#
# Задача 2. Контакты 2
#
# print('телефонный справочник')
# phone_dict=dict()
# name=''
# for i in range(4):
#     name=input('имя контакта и фамилия ').lower().split()
#     name=tuple(name)
#     if name in phone_dict.keys():
#         print('этот человек уже есть')
#         continue
#     phone_number=int(input('номер телефона '))
#     name=tuple(name)
#     phone_dict[name]=phone_number
#     for name,number in phone_dict.items():
#         print(*name,':',number)
#
# print(phone_dict)

# Задача 1. Ревью кода
# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
#
# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += dict[i]['interests']
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# [print('ID:', id, '; возраст', students[id]['age']) for id in students]
#
# my_lst, l = f(students)
# print(my_lst, l)

# Задача 2. Универсальная программа 2

# def crypto(checking_list):
#     return [v for i, v in enumerate(checking_list) if i >= 1 and is_prime(v)]
#
#
# def is_prime(x):
#     for i in range(2, (x//2)+1):
#         if x % i == 0:
#             return False
#     return True
#
#
# print(crypto([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # print(crypto('О Дивный Новый мир!'))
#
# Задача 3. Функция
# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент
# (его можно вводить с клавиатуры). Функция должна возвращать новый кортеж, начинающийся
# с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз,
# то вернуть кортеж, который начинается с него и идёт до конца исходного.

# def slicer(lst, sym):
#     if sym not in lst:
#         return ()
#     if lst.count(sym) == 1:
#         return lst[lst.index(sym):]
#     start=lst.index(sym)
#     end=lst.index(sym, lst.index(sym)+1)
#     return lst[start:end]
#
#
# print(slicer((1, 2, 3, 4, 2, 2, 7, 8, 2, 2, 9, 10), 2))


# Задача 4. Игроки
# У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «Ф. И. — очки»:
#
# players = {
#     ("Ivan", "Volkin"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }
#
# Один программист попросил нас для своей базы отправить ему немного другой вариант хранения этой информации.
# Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран.
# Постарайтесь использовать как можно более эффективное решение.
# Результат работы программы:
# [('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]

# res=tuple()
# i=list()
# for key,value in players.items():
#     i.append(key+value)
# print(i)


# print([sum((key, value), ()) for key, value in players.items()])


# Задача 5. Одна семья
# В одной базе данных хранится информация о членах нескольких разных семей.
# Хранение реализовано с помощью словаря с парами «Ф. И. — возраст».
# Напишите программу, которая запрашивает у пользователя фамилию и выводит на экран
# возраст всех членов одной семьи. Учтите, что, например, у двух людей разного пола
# фамилии различаются окончаниями. Поиск не должен быть регистрозависимым.
# Пример:
# Введите фамилию: Сидоров
#
# Сидоров Никита 35
# Сидорова Алина 34
# Сидоров Павел 10
# Действие «Поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты
# с такой фамилией и их номера телефонов. Поиск не должен зависеть от регистра символов.

# d = {
#     'Сидоров Никита': 35,
#     'Сидорова Алина': 34,
#     'Сидоров Павел': 10,
#     'Петров Виктор': 15,
#     'Петрова Дарья': 16
# }
#
# surname=input('введите фамилию ').lower()
# if surname.endswith('а'):
#     surname=surname[0:len(surname)-1]
#
# for name,age in d.items():
#     if surname in name.lower():
#         print(name,age)

# Задача 6. По парам
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

# a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# res=tuple()
# lst=list()
# count=0
# for i in a:
#     count+=1
#     res = res + (i,)
#     if count==2:
#         lst.append(res)
#         res=tuple()
#         count=0
# print(lst)

# original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# result = list(zip(original_list[::2], original_list[1::2]))
# print(f"Новый список: { result } ")

# Задача 7. Функция сортировки
# Напишите функцию, которая сортирует кортеж, состоящий из целых чисел, по возрастанию и возвращает его.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
#

# def tpl_sort(tpl):
#     for element in tpl:
#         if not isinstance(element, int):
#             return tpl
#     return tuple(sorted(tpl))


# Задача 8. Контакты 3
# Мы уже помогали Степану с реализацией телефонной книги (контактов) на телефоне, однако внезапно оказалось,
# что книге не хватает ещё одной очень полезной функции: поиска!
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить:
# добавить контакт или найти человека в списке контактов по фамилии.
# Действие «Добавить контакт»: программа запрашивает имя и фамилию контакта, затем номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов. Если этот человек уже есть
# в словаре, то выведите соответствующее сообщение.

# def add():
#     name = input('имя контакта и фамилия ').lower().split()
#     name = tuple(name)
#     if name in phone_dict.keys():
#         return print('этот человек уже есть')
#     phone_number = int(input('номер телефона '))
#     # создание словаря с номерами
#     phone_dict[name] = phone_number
#     for name, number in phone_dict.items():
#         return print(*name, ':', number)
#
#
# def find(d):
#     surname = input('введите фамилию ').lower()
#     for name, number in d.items():
#         if surname in name:
#             return print('номер:', number)
#     return print('нет в списке контактов')
#
#
# print('телефонный справочник')
# phone_dict = dict()
# while True:
#     print('\n1 - добавить контакт ')
#     print('2 - найти контакт \n')
#     choise = int(input())
#     if choise == 1:
#         add()
#     if choise == 2:
#         find(phone_dict)

# print(phone_dict)

# Задача 9. Протокол соревнований
# 1 запись: 69485 Jack
# 2 запись: 95715 qwerty
# 3 запись: 95715 Alex
# 4 запись: 83647 M
# 5 запись: 197128 qwerty
# 6 запись: 95715 Jack
# 7 запись: 93289 Alex
# 8 запись: 95715 Alex
# 9 запись: 95715 M


# N = 3
# protokol = dict()
# for i in range(1, N + 1):
#     rez, name = input(f'{i} запись: ').strip().split()
#     rez = int(rez)
#     if protokol.get(name):
#         if rez > protokol.get(name):
#             protokol[name] = rez
#     else:
#         protokol[name] = rez
#
#
# sorted_protokol = sorted(protokol, key=protokol.get, reverse=True)
# count=0
# for i in sorted_protokol[:3]:
#     count+=1
#     print(f'{count} место:',i, protokol[i])
