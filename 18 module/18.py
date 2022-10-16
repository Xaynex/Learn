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
