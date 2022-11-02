# Задача 1. Сисадмин
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
#
# Пример результата:
# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
#
# Относительный путь до файла: Skillbox\access\admin.bat
# import os
# searched_file='admin.bat'
# dir='Skillbox'
# dir2='access'
# print(os.path.abspath(searched_file))
# print(os.path.join(dir,dir2,searched_file))
#
# Задача 2. Содержимое

# import os
#
# path=os.path.abspath(os.path.join('..'))
# print('содержимое каталога',path)
# lst=os.listdir(path)
# for i in lst:
#     print(' ',i)
#     # print(i)

# Задача 3. Корень диска
# Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
#
# Результат программы на примере диска G:
# Корень диска: G:\\
#
# import os
# print(os.path.abspath(os.sep))


# Задача 1. Иконки
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт
# import os
#
#
# def check_path(my_path):
#     if os.path.exists(my_path):
#         if os.path.isfile(my_path):
#             print('это файл')
#             print('вес файла',os.path.getsize(my_path),'байт')
#         elif os.path.islink(my_path):
#             print('это ссылка')
#         elif os.path.isdir(my_path):
#             print('это директория')
#     else:
#         print('такого пути нет')
#
#
# my_path = '/Users/saynex/Documents/learn/мои работы /projects/22 module/22.py'
# # my_path = '/Users/saynex/Documents/learn/мои работы /projects/'
# print('путь',my_path)
# check_path(my_path)

# Задача поиск
# def search(dir_path,file_name):
#     if os.path.isdir(dir_path):
#         folder_containts = os.listdir(dir_path)
#         # print('проверяем папку',dir_path )
#         for file in folder_containts:
#             # print('проходимся по файлу',file)
#             if file_name in file:
#                 if os.path.isfile(os.path.join(dir_path, file)):
#                     print('нашел ',os.path.join(dir_path, file))
#         for file in folder_containts:
#             search(os.path.join(dir_path,file), file_name)
#
#
#
# import os
# dir_path='/Users/saynex/Documents/learn/мои работы /projects/'
# print('Ищем в:',dir_path)
# file_name='test'
# print('Файл:',file_name,'\n')
# search(dir_path,file_name)

# Задача 1. Результаты
import os
# print(os.path.abspath(''))
# file = open('/Users/saynex/Documents/learn/мои работы /projects/task/group_1.txt', 'r')
# summa = 0
# for i_line in file:
#     info = i_line.split()
#     summa += int(info[2])
# file.close()
# file = open('/Users/saynex/Documents/learn/мои работы /projects/task/group_1.txt', 'r')
# diff = 0
# for i_line in file:
#     info = i_line.split()
#     diff -= int(info[2])
# file.close()
# file_2 = open('/Users/saynex/Documents/learn/мои работы /projects/task/Additional_info/group_2.txt', 'r')
# count=0
# for i_line in file_2:
#     count+=1
#     info = i_line.split()
#     if count==1:
#         compose = int(info[2])
#     else:
#         compose*=int(info[2])
# print(summa)
# print(diff)
# print(compose)

# Задача 2. Поиск файла 2
# import os
#
#
# def open_file(saved_path):
#     file = open(saved_path, 'r')
#     for i_line in file:
#         print(i_line, end='')
#     print()
#     file.close()
#
#
# def search(dir_path, file_name, saved_path=[]):
#     if os.path.isdir(dir_path):
#         folder_containts = os.listdir(dir_path)
#         # print('проверяем папку',dir_path )
#         for file in folder_containts:
#             # print('проходимся по файлу',file)
#             if file_name in file:
#                 if os.path.isfile(os.path.join(dir_path, file)):
#                     print('нашел ', os.path.join(dir_path, file))
#                     saved_path = os.path.join(dir_path, file)
#                     open_file(saved_path)
#         for file in folder_containts:
#             search(os.path.join(dir_path, file), file_name)
#
#
# dir_path = '/Users/saynex/Documents/learn/мои работы /projects/'
# print('Ищем в:', dir_path)
# file_name = 'test'
# print('Файл:', file_name, '\n')
# search(dir_path, file_name)

# Задача 1. Сумма чисел
import os
# file_numbers=open('numbers.txt','r')
# file_answer=open('answer.txt','a')
# summa=0
# for i_line in file_numbers:
#     summa+=int(i_line)
# file_answer.write(str(summa))
# file_numbers.close()
# file_answer.close()

# Задача 2. Всё в одном

# Напишите программу, которая копирует код каждого скрипта
# в папке проекта python_basic в файл scripts.txt, разделяя код строкой из 40 символов *.
# import os
#
#
# def open_to_read(folder, file):
#     scripts = open('scripts.txt', 'a')
#     my_path = os.path.abspath(os.path.join('..', folder, file))
#     print(my_path)
#     if os.path.exists(my_path):
#         my_file = open(my_path, 'r')
#         for i_line in my_file:
#             scripts.write(i_line)
#         scripts.write('*' * 40)
#         scripts.write('\n')
#     scripts.close()
#
#
# for i in range(11, 23):
#     ii = str(i) + '.py'
#     open_to_read(f'{i} module', str(ii))
# ==================================================================
# Задача 1. Сумма чисел 2

# import os
#
# file = open('numbers.txt', 'r')
# total = 0
# for i_line in file:
#     for i in i_line:
#         if i.isdigit():
#             total += int(i)
# file_2 = open('answer.txt', 'w')
# file_2.write(str(total))

# Задача 2. Дзен Пайтона
# file = open('zen.txt', 'r')
# zen_invert=file.readlines()[::-1]
# for i_line in zen_invert:
#     print(i_line,end='')

# Задача 3. Дзен Пайтона 2
# file = open('zen.txt', 'r')
# line_count=0
# sym_count=0
# words_count=0
# for i_line in file:
#     line_count+=1
#     for sym in i_line:
#         if sym.isalpha():
#             sym_count+=1
#         if sym==' ':
#             words_count+=1
#
#
# print('количество букв:',sym_count)
# print('количество слов:',words_count)
# print('количество строк:',line_count)


# Задача 4. Файлы и папки
# Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска)
# и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога
# в килобайтах (1 килобайт = 1024 байт).
# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.
#
# Результат работы программы на примере python_basic\Module14:
# Размер каталога (в Кб): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15
# import os
#
# def size(path):
#     global total_size
#     global folders
#     global files
#     if os.path.exists(path):
#         for folder_or_files in os.listdir(path):
#             files += 1
#             if os.path.isfile((os.path.join(path, folder_or_files))):
#                 total_size += os.path.getsize((os.path.join(path, folder_or_files)))
#             elif os.path.isdir((os.path.join(path, folder_or_files))):
#                 folders += 1
#                 size((os.path.join(path, folder_or_files)))
#     else:
#         print('путь не верный')
#
#
# files = 0
# total_size = 0
# folders = 0
# path = '/Users/saynex/Documents/Портфолио'
# size = size(path)
# print('содержимое каталога', path)
# print('размер', round((total_size / 1073741824), 4))
# print('подкаталоги', folders)
# print('файлы', files)

# Задача 5. Сохранение
# Введите строку: testiruyem
#
# Куда хотите сохранить документ? Введите последовательность папок (через пробел):
# Users Roman PycharmProjects Skillbox Module22
#
# Введите имя файла: my_document
# Файл успешно сохранён!
#
# Содержимое файла:
# programm test
# import os
#
#
# def check(path):
#     if os.path.isfile(path):
#         choise = input('перезаписать файл? ')
#         if choise == 'yes':
#             file = open(os.path.join(path), 'w')
#             file.write(stroka)
#             print('файл успешно перезаписан')
#             return True
#         else:
#             quit()
#     else:
#         return False
#
#
# stroka = input('введите строку: ')
# user_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').replace(' ',
#                                                                                                                os.sep)
# # Users saynex Documents learn My_projekts python_projects
# path = os.path.sep + user_path
# if os.path.exists(path):
#     file_name = input('\nВведите имя файла: ')
#     path += os.path.sep + file_name
#     if not check(path):
#         file = open(os.path.join(path), 'w')
#         file.write(stroka)
#         file.close()
#         print('файл успешно сохранен')
# else:
#     print('путь не существует')

# задача 6

import string

# abc = string.ascii_lowercase
# count = 0
# index = []
# protected_word = ''
# file = open('text.txt', 'r')
# print('Содержимае файла')
# for i_line in file:
#     count += 1
#     print(i_line, end='')
#     for i in i_line:
#         if i in abc:
#             index.append(abc.index(i))
#     for i in index:
#         protected_word += abc[i + count]
#     cipher_text = open('cipher_text.txt', 'a')
#     protected_word += '\n'
#     cipher_text.write(protected_word)
#     protected_word = ''
#     index = []
# Задача 7. Турнир

# first_tour = open('first_tour.txt', 'r')
# K = int(first_tour.readline())
#
# players = dict()
# for i_line in first_tour:
#     rate = ''
#     name = ''
#     for sym in i_line:
#         if sym.isalpha() or sym == ' ':
#             name += sym
#         if sym.isdigit():
#             rate += sym
#     first_letter = name.split()
#     first_letter = first_letter[1][0] + '.'
#     surname = name.split()
#     players[first_letter + surname[0]] = int(rate)
#
# winers = dict()
# for i in players:
#     if players[i] > K:
#         winers[i] = players[i]
#
# second_tour = open('second_tour.txt', 'w')
# for i in winers:
#     second_tour.write(i + ' ')
#     second_tour.write(str(winers[i]) + '\n')

# Задача 8. Частотный анализ
# Содержимое файла text.txt:
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083
# import operator
# import re
#
# file = open('text.txt', 'r')
# text = file.read().lower()
# text = re.sub("[^A-Za-z]", '', text)
# print(text)
# part = round(1 / len(text), 3)
# print('одна буква это:', part)
#
# result = dict()
# for sym in text:
#     if sym in result:
#         result[sym] += part
#     else:
#         result[sym] = part
#
# print(result)
# sorted_result = sorted(result.items())
# print(sorted_result)
# sorted_result.sort(key=lambda x: x[0], reverse=True)
# print(sorted_result)
# analysis = open('my_analysis.txt', 'w')
# for key, v in sorted_result:
#     print(key, v)
#     analysis.write(key + ' ' + str(v) + '\n')
