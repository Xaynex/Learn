# Задача 1. Свой for (ну почти)
# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию, которая эмулирует работу цикла for
# с помощью цикла while и проходит во всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации»
#
# def my_for(iter_obj):
#     try:
#         iterator = iter_obj.__iter__()
#         while True:
#             print(next(iterator))
#     except StopIteration:
#         pass
#
#
# str = 'привет'
# lst = [1, 2, 3, 4, 5]
#
# my_for(str)

# Задача 1. Бесконечный итератор

# class CountIterator:
#
#     count=0
#
#     def __iter__(self):
#         print('метод итер')
#         return self
#
#
#     def __next__(self):
#         self.count+=1
#         return self.count
#
# my_iter = CountIterator()
# for i_elem in my_iter:
#     print(i_elem)

# Задача 2. Случайная сумма

# import random
#
#
# class Iterator:
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#         self.cur_v = random.random()
#         self.next_v = 0
#
#     def __iter__(self):
#         self.counter = 0
#         self.cur_v = random.random()
#         self.next_v = 0
#
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > self.limit:
#             raise StopIteration
#         else:
#             self.next_v += random.random() + self.cur_v
#             return round(self.next_v,2)
#
#
# # n=input('количество элементов: ')
# n = 5
# iter = Iterator(n)
#
# for i_elem in iter:
#     print(i_elem)
#
# for i_elem in iter:
#     print(i_elem)

# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые
# числа от 1 до N.
# Основной код:
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

# class Primes:
#
#     def __init__(self,limit):
#         self.limit=limit
#
#
#     def __iter__(self):
#         self.counter=0
#         self.cur_v=1
#         return self
#
#     def __next__(self):
#         self.counter+=1
#         if self.counter<50:
#             self.cur_v +=1
#             prime = True
#             for i in range(2, self.cur_v):
#                 if (self.cur_v % i == 0):
#                     prime = False
#             if prime:
#                 return self.cur_v
#             else:
#                 return ''
#         else:
#             raise StopIteration
#
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end='')
#
# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
# который также в цикле будет бесконечно выдавать значения.
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

# def generator_prime():
#     num = 2
#     while True:
#         if all(num % i != 0 for i in range(2, num)):
#             yield num
#             num += 1
#         else:
#             num+=1
#
# def generator():
#     count = 0
#     while True:
#         count += 1
#         yield count
#
#
# # for i in generator():
# #     print(i)
#
# for i in generator_prime():
#     print(i)

# Задача 2. Очень большой файл

# Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его открытии компьютер
# просто зависает, так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу,
# которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.

# def generator():
#     with open('numbers.txt','r') as file:
#         for line in file:
#             for num in line.split():
#                 yield int(num)
# print(generator())
# print(sum(generator()))
#
# Задача 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу, которая генерирует последовательность
# из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.

# from typing import Iterable
#
#
# def gen() -> Iterable[int]:
#     for num in range(1, N + 1):
#         yield num ** 2
#
#
# class iter:
#
#     def __init__(self, limit: int) -> None:
#         self.num = 1
#         self.limit = limit
#
#     def __iter__(self):
#         self.num = 0
#         return self
#
#     def __next__(self) -> int:
#         while self.num < self.limit:
#             self.num += 1
#             return self.num ** 2
#         else:
#             raise StopIteration
#
#
# N = 5
# print('генераторное выражение')
# print([num ** 2 for num in range(1, N + 1)])
# print('функция-генератор')
# for num in gen():
#     print(num, end=' ')
# print('\nкласс-итератор')
# for num in iter(N):
#     print(num, end=' ')

# Задача 2. Рефакторинг

# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
#
# def iter_list(list_one: list, list_two: list, search: int):
#     for num in list_one:
#         for y in list_two:
#             result = num * y
#             print(num, y, result)
#             if result == search:
#                 yield True
#             yield False
#
#
# solution = iter_list(list_1, list_2, to_find)
#
# for result in solution:
#     if result:
#         print('Found!!!')
#         solution.close()

# Задача 3. Пути файлов
# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам
# указанной директории (по умолчанию — корневой диск),
# находит указанный пользователем каталог и генерирует пути всех встреченных файлов.
# import os
#
# def gen_files_path(path_dir, catalog):
#     list_dir = os.listdir(path_dir)
#     for file in list_dir:
#         path_file = os.path.join(path_dir, file)
#         print(path_file)
#         if os.path.isdir(path_file):
#             if file == catalog:
#                 print('указанный пользователем каталог')
#                 quit()
#             gen_files_path(path_file, catalog)
#
#
# print('укажите директорию: /Users/saynex/Documents')
#
# path = '/Users/saynex/Documents'
# print('укажите каталог: python_projects')
# catalog = 'python_projects'
# print('пути встречных файлов')
#
# gen_files_path(path,catalog)
# Задача 4. Последовательность Хофштадтера
# Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором). Сама последовательность выглядит
# так:
# Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))
# В итератор (или генератор) передаётся список из двух чисел. Например, QHofstadter([1, 1])
# генерирует точную последовательность Хофштадтера. Если передать значения [1, 2], то последовательность
# должна немедленно завершиться.

# class qsequence:
#     def __init__(self, sequence: list):
#         self.sequence = sequence[:]
#         if sequence != [1, 1]:
#             raise ValueError('Не верно указано число последовательностей.')
#         if self.sequence[0] != self.sequence[1]:
#             raise ValueError('Значения последовательности не совпадают.')
#
#     def __str__(self) -> str:
#         # return ', '.join(str(elem) for elem in self.sequence)
#         return str(self.sequence)
#
#     def __next__(self):
#         try:
#             q = self.sequence[-self.sequence[-1]] + self.sequence[-self.sequence[-2]]
#             self.sequence.append(q)
#             return q
#         except IndexError:
#             raise StopIteration()
#
#     def __iter__(self):
#         return self
#
#     def current_state(self):
#         return self.sequence
#
#
# q1 = qsequence([1, 1])
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# next(q1)
# print(q1)

# Задача 5. Количество строк
# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет
# общее количество строк кода, игнорируя пустые строки и строчки комментариев.
# import os
# import pathlib
#
#
# def quontity_py_str(path):
#     list_dir = os.listdir(path)
#     for file in list_dir:
#         path_file = os.path.join(path, file)
#         if os.path.isfile(path_file):
#             if pathlib.Path(path_file).suffix == '.py':
#                 with open(path_file, 'r') as file:
#                     for stroka in file:
#                         if stroka != '\n' and stroka != '#\n':
#                             # print(stroka)
#                             yield 1
#         if os.path.isdir(path_file):
#             yield from quontity_py_str(path_file)
#
#
# my_dir = os.path.abspath('..')
# total = 0
# for stroka in quontity_py_str(my_dir):
#     total += stroka
# print(total)

# class LinkedList:
#     class __Node:
#         def __init__(self, value):
#             self.value = value
#             self.nxt = None
#
#     def __init__(self, *args):
#         length = len(args)
#         self.__length = length
#         self.__head = self.__Node(args[0]) if length > 0 else None
#         self.__tail = self.__head
#         for i in range(1, length):
#             self.__tail.nxt = self.__Node(args[i])
#             self.__tail = self.__tail.nxt
#
#     def __iter__(self):
#         current = self.__head
#         while current is not None:
#             yield current.value
#             current = current.nxt
#
#     def __str__(self):
#         return f"[{' '.join(str(i) for i in self)}]"
#
#     def __len__(self):
#         return self.__length
#
#     def __index_check(self, index):
#         if not 0 <= index < self.__length:
#             raise IndexError
#
#     def append(self, value):
#         if self.__length > 0:
#             self.__tail.nxt = self.__Node(value)
#             self.__tail = self.__tail.nxt
#         else:
#             self.__head = self.__tail = self.__Node(value)
#         self.__length += 1
#
#     def get(self, index):
#         self.__index_check(index)
#         current = self.__head
#         for _ in range(index):
#             current = current.nxt
#         return current.value
#
#     def remove(self, index):
#         self.__index_check(index)
#         if self.__length == 1:
#             self.__head = self.__tail = None
#         elif index == 0:
#             self.__head = self.__head.nxt
#         else:
#             current = self.__head
#             for _ in range(index - 1):
#                 current = current.nxt
#             current.nxt = current.nxt.nxt
#             if index == self.__length - 1:
#                 self.__tail = current
#         self.__length -= 1
#
#
# my_list = LinkedList()
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print('Новый список:', my_list)


