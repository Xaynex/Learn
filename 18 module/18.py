# Задача 1.1 Заказ
# name= input('Имя: ')
# number=input('Номер заказа: ')
#
# message='Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!'.format(name=name, number=number)
# print(message)

# Задача 1.2 Долги

# name= input('Имя: ')
# Debt=input('Долг: ')
#
# message='{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(name, Debt)
# print(message)

# Задача 1.3 IP-адрес
# def check(a):
#     if a > 255 or a < 0:
#         print('ошибка')
#         quit()
#
# a0 = int(input())
# check(a0)
# a1 = int(input())
# check(a1)
# a2 = int(input())
# check(a2)
# a3 = int(input())
# check(a3)
# ip_address = '{0}.{1}.{2}.{3}'.format(a0, a1, a2, a3)
# print(ip_address)

# Задача 2.1 Улучшенная лингвистика 2
# words, text = [input('введите слово ') for i in range(3)], input('введите текст ')
# for word in words:
#     print('слово {word} встречается в тексте'.format(word=word), text.count(word), 'раз')

# Задача 2.2 Бабушка
# text='У       нас         пошёл                    снег    !     '
# correct=text.split()
# print(*correct)

# Задача 2.3 Разделители символов

# template=input('# Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
# people=input('Список людей через запятую: ')
# age=input('Возраст людей через пробел: ')
# a=people.split(', ')
# b=age.split()
# for i in range(len(a)):
#     print(template.format(name=a[i],age=b[i]))

# Задача 3.2 Путь к файлу
# Пример:
# Путь к файлу: C:/user/docs/folder/new_file.txt
# На каком диске должен лежать файл: C
# Требуемое расширение файла: .txt
# Путь корректен!


# disk = input('на каком диске должен лежать файл ')
# file = input('Требуемое расширение файла: ')
# path = 'C:/user/docs/folder/new_file.txt'
#
# if not path.startswith(disk):
#     print('путь не верный')
# elif not path.endswith(file):
#     print('путь не верный')
# else:
#     print('путь корректный')

# Задача 3. Удаление части
# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы.
# Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных.
# Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.
# Подсказка: используйте методы islower() и/или isupper().
#
# Пример:
# Введите строку: ПитоН - этО хорошО
#
# Результат: питон - это хорошо
#
# Пример 2:
# Введите строку: ПиТоН - ЭтО УДоБнО
#
# Результат: ПИТОН - ЭТО УДОБНО
# listt = 'ПиТоН - ЭтО УДоБнО'
# lower = 0
# upper = 0
# for sym in listt:
#     if sym.islower():
#         lower += 1
#     if sym.isupper():
#         upper += 1
# if lower > upper:
#     print(listt.lower())
# else:
#     print(listt.upper())

# def foo(s: str) -> str:
#     alpha = list(filter(str.isalpha, s))
#     if sum(map(str.islower, s)) < len(alpha) // 2:
#         return s.upper()
#     return s.lower()
#
# print(foo(input()))

# ===================================================================================================
# Задача 1. Меню ресторана
# menu='утиное филе;фланк-стейк;банановый пирог;плов'
# print('у нас есть: ', menu.replace(';', ', '))

# Задача 2. Самое длинное слово
# Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, выведите  это слово и его длину.
# Если таких слов несколько, выведите первое из них.

# text=('утиное филе фланк-стейк банановый пирог плов').split()
# max=''
# for word in text:
#     if len(word)>len(max):
#         max=word
# print(max)
# print(len((max)))


# Задача 3. Файлы
# name = 'example.txt'
# forbiden = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
# for sym in forbiden:
#     if name.startswith(sym) or not (name.endswith('.txt') or name.endswith('.docx')):
#         print('Ошибка: название начинается на один из специальных символов или неверное расширение файла')
#         quit()
#
# print('Файл назван верно.')

# Задача 4. Заглавные буквы

# text='Кажется, я забыл выключить утюг'
# print(text.title())

# Задача 5. Капитан Флинт

# oy = input('По оси OY: ').split()
# ox = input('По оси OX: ').split()
#
# if 'South' == oy[0]:
#     oy[1] = '-'+oy[1]
# if 'West' == ox[0]:
#     ox[1] = '-'+ox[1]
#
# print(ox[1], oy[1])

# Задача 6. Пароль
# count_num = 0
# big_letter = False
# while True:
#     pas = input('Придумайте пароль ')
#     for sym in pas:
#         if sym.isupper():
#             big_letter = True
#     if big_letter:
#         for sym in pas:
#             if sym.isdigit():
#                 count_num += 1
#                 if count_num == 3:
#                     print('надежный пароль')
#                     quit()
#     print('не надежный пароль')

# Задача 7. Цифры в строке
# Пользователь вводит строку, которая, возможно, содержит пробелы.
# Напишите программу, которая извлекает из этой строки все символы, являющиеся цифрами и составляет из них новую строку.
#
# Пример:
# Введите строку: пр6и89вет#
# Цифры: 689

# stroka='пр6и89вет'
# stroka_num=''
# # stroka_num=[stroka_num+sym for sym in stroka if sym.isdigit()]
# for sym in stroka:
#     if sym.isdigit():
#         stroka_num=stroka_num+sym
# print(stroka_num)

# Задача 8. Сжатие
# Пример:
# Введите строку: aaAAbbсaaaA
#
# Закодированная строка: a2A2b2с1a3A1

# text = 'aaAAbbсcccccrrrraaaAAA'
# new=''
# count = 0
# end = 0
# start = 0
# for sym in range(len(text)-1):
#     end += 1
#     if text[sym+1] != text[sym]:
#         count = text[start:end]
#         start = start + len(count)
#         new=new+text[sym] + str(len(count))
# diff=end+1-start
# print(new+text[end:], end='')
# print(diff)

# Задача 9. IP - адрес 2

# Пример 1:
# Введите IP: 128.16.35.a4
# a4 - не целое число
#
# Пример 2:
# Введите IP: 240.127.56.340
# 340 превышает 255
#
# Пример 3:
# Введите IP: 34.56.42,5
# Адрес - это четыре числа, разделенные точками
#
# Пример 4:
# Введите IP: 128.0.0.255
# IP-адрес корректен

# error = False
# IP = '34.56.42,5'.split('.')
# for sym in IP:
#     # проверка на целове число
#     if not sym.isdigit():
#         print(sym, '- не целое число')
#         error = True
#     # проверка на 0-255
#     elif not 255 >= int(sym) >= 0:
#         print(sym, 'должно быть от 0 до 255')
#         error = True
# if len(IP) <= 3:
#     print('Адрес - это четыре числа, разделенные точками')
#     error = True
# if error == False:
#     print('IP-адрес корректен')
