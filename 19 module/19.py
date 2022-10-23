# Задача 1. Словарь квадратов чисел

# s = {}
# num = 5
# for i in range(1, 5 + 1):
#     s[i] = i ** 2
# print(s)

# Задача 2. Студент
#
# Результат:
# Имя - Илья
# Фамилия - Иванов
# Город - Москва
# Место учёбы - МГУ
# Оценки - [5, 4, 4, 4, 5]
#
# student_str=input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ')

# rates=[]
# student_str = 'Илья Иванов Москва МГУ 5 4 4 4 5'
# student_info = student_str.split()
# student_info2=student_info[:]
# for i in student_info:
#     if i.isdigit():
#         rates.append(i)
#         student_info2.remove(i)
# rates=' '.join(rates)
# info = ['имя', 'фамилия', 'город', 'место учёбы', 'оценки']
# count = 0
# student_dict = {}
# for i in student_info2:
#     student_dict[info[count]] = i
#     count += 1
# student_dict[info[count]]=rates
# print(student_dict)
#
# for i in student_dict:
#     print(i, '-',student_dict[i], '\n',end='')

# Задача 3. Контакты
# Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему.
# И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.
# Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона,
# добавляет их в словарь и выводит на экран текущий словарь контактов.
# Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы).
# Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.
#
# Пример:
# Текущие контакты на телефоне:
# <Пусто>
# Введите имя: Иван
# Введите номер телефона: 100200300
#
# Текущие контакты на телефоне:
# Иван  100200300
#
# Введите имя: Лена
# Введите номер телефона: 8005555522
#
# Текущие контакты на телефоне:
# Иван  100200300
# Лена  8005555522
#
# Введите имя: Иван
# Ошибка: такое имя уже существует.
# phones = {}
# while True:
#     print('Текущие контакты на телефоне: ')
#     for i in phones:
#         print(i, phones[i])
#     name = input('Введите имя: ')
#     if name in phones:
#         print('Ошибка: такое имя уже существует')
#         quit()
#     number = input('Введите номер телефона: ')
#     phones[name] = number
# задача 1
# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
#
# big_storage.update(small_storage)
# print(big_storage)
# name= input('введите название товара ')
# if name in big_storage:
#     print(big_storage.get(name))
# else:
#     print('ошибка')

# Задача 2. Кризис фруктов
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'grapefruit': 300.40,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# total = sum(incomes.values())
# print('общий доход ', total)
# minn=''
# for key in incomes:
#     if incomes[key]==min(incomes.values()):
#         minn=key
# print('Самый маленький доход у', minn, 'он составляет', min(incomes.values()))
# incomes.pop(minn)
# print('иног', incomes)

# Задача 3. Гистограмма частоты
# text=input('введите текст ').lower()
# sym_dict=dict()
#
# for sym in text:
#     if sym in sym_dict:
#         sym_dict[sym]+=1
#     else:
#         sym_dict[sym] = 1
#
# for i in sym_dict:
#
#     print(i,':', sym_dict[i])
# print(max(sym_dict.values()))

# Задача 1. Член семьи

# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет,
# а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:

# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# print('Все члены команды из команды А, которые отдыхают ')
# for i in players_dict:
#     if players_dict.get(i).get('team')=='A' and players_dict.get(i).get('status')=='Rest':
#         print(players_dict.get(i).get('name'))
# print('Все члены команды из группы B, которые тренируются.')
# for i in players_dict:
#     if players_dict.get(i).get('team')=='B' and players_dict.get(i).get('status')=='Training':
#         print(players_dict.get(i).get('name'))
# print('Все члены команды из команды C, которые путешествуют.')
# for i in players_dict:
#     if players_dict.get(i).get('team')=='C' and players_dict.get(i).get('status')=='Travel':
#         print(players_dict.get(i).get('name'))

#
# Задача 1. Пунктуация
# Напишите программу, которая считает количество знаков пунктуации в символьной строке.
# К знакам пунктуации относятся символы из набора ".,;:!?". Набор должен храниться в виде множества.
#
# Пример:
# Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
#
# Количество знаков пунктуации: 6

# a = set('.,;:!?')
# stroka = 'Я! Есть. Грут?! Я, Грут и Есть.'
# k = 0
# for x in stroka:
#     if x in a:
#         k += 1
# print(k)

# Задача 2. Семинар
# На одном семинаре по теории множеств нужно показать наглядный пример, как эти множества работают.
# Для начала было сгенерировано два набора чисел:
#
# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

# Напишите программу, которая преобразует списки во множества и убирает повторяющиеся элементы.
# Затем удаляет минимальный элемент из каждого множества и добавляет туда случайное число в диапазоне от 100 до 200.
# Затем выполните следующие действия со множествами:
# 1.	Вывести все элементы множеств (объединение).
# 2.	Вывести только общие элементы (пересечение).
# 3.	Вывести элементы, входящие в nums_2, но не входящие в nums_1.
# import random
# set_1=set(nums_1)
# set_2=set(nums_2)
#
# print('1 множество', set_1)
# print('2 множество', set_2)
#
# print('минимальный элемент 1 множества', min(set_1))
# print('минимальный элемент 2 множества', min(set_2))
#
# set_1.remove(min(set_1))
# set_2.remove(min(set_2))
#
# set_1.add(random.randint(100,200))
# set_2.add(random.randint(100,200))
#
# print(set_1 | set_2)
# print(set_1 & set_2)
# print(set_2 - set_1)

# Задача 3. Различные цифры
# Напишите программу, которая находит все различные цифры в символьной строке.
# Для решения используйте множество (цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
#
# Подсказка: можно использовать вот такое сравнение '0'<=x<='9'
#
# Пример:
# Введите строку: ab1n32kz2
# Различные цифры строки: 123

# stroka = 'ab1n32kz2'
# b = set()
# for i in stroka:
#     if '0' <= i <= '9':
#         b.add(i)
# for i in b:
#     print(i, end='')

# ===============================================================================================================
# Задача 1. Песни 2
# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
#
# n = 2
# time = 0.0
# for i in range(n+1):
#     song = input('название песни: ').lower()
#     for ii in violator_songs:
#         if ii.lower() == song.lower():
#             time += violator_songs[ii]
#
# print(round(time,2))

# Задача 2. География
#
# Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся,
# в одну строку. Затем пользователь вводит три названия городов. Реализуйте такую программу и для каждого
# из трёх городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
#
# Пример:
# Кол-во стран: 2
# 1 страна: Россия Москва Петербург Новгород
# 2 страна: Германия Берлин Лейпциг Мюнхен
#
# data_set = {}
# amount_country = int(input('Кол-во стран: '))
#
# for i in range(amount_country):
#     value = input('{} страна: '.format(i + 1)).split()
#     for city in value[1:]:
#         data_set[city] = value[0]
#
# for i in range(3):
#     city = input('\n{} город: '.format(i + 1))
#     country = data_set.get(city)
#     if country:
#         print(f'Город {city} расположен в стране {country}.')
#     else:
#         print(f'По городу {city} данных нет.')

# Задача 3. Криптовалюта
# data = {
#     "address": "0x544444444444",
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#     },
#     "count_txs": 2,
#     "tokens": [
#         {
#             "fst_token_info": {
#                 "address": "0x44444",
#                 "name": "fdf",
#                 "decimals": 0,
#                 "symbol": "dsfdsf",
#                 "total_supply": "3228562189",
#                 "owner": "0x44444",
#                 "last_updated": 1519022607901,
#                 "issuances_count": 0,
#                 "holders_count": 137528,
#                 "price": False
#             },
#             "balance": 5000,
#             "totalIn": 0,
#             "totalOut": 0
#         },
#         {
#             "sec_token_info": {
#                 "address": "0x44444",
#                 "name": "ggg",
#                 "decimals": "2",
#                 "symbol": "fff",
#                 "total_supply": "250000000000",
#                 "owner": "0x44444",
#                 "last_updated": 1520452201,
#                 "issuances_count": 0,
#                 "holders_count": 20707,
#                 "price": False
#             },
#             "balance": 500,
#             "totalIn": 0,
#             "total_out": 0
#         }
#     ]
# }
# # Напишите программу, которая выполняет следующий алгоритм действий:
# # 1.	Вывести списки ключей и значений словаря.
# # 2.	В “ETH” добавить ключ “total_diff” со значением 100.
# # 3.	Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
# # 4.	Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
# # 5.	Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
# # 1
# print(data.keys())
# print(data.values())
# # 2
# data['ETH']['total_diff'] = 100
# # 3
# data['tokens'][0]['fst_token_info']['name'] = 'doge'
# print(data['tokens'][0]['fst_token_info'])
# # 4
# data['ETH']['total_out'] = data['tokens'][1]['total_out']
# del data['tokens'][1]['total_out']
# print(data['tokens'][1])
# # 5
# data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info']['price']
# del data['tokens'][1]['sec_token_info']['price']
#
# print(data)

# Задача 4. Товары
# В базе данных магазина вся необходимая информация по товарам делится на два словаря:
# первый отвечает за коды товаров, второй — за списки количества разнообразных товаров на складе:

# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
# print('результат работы программы ')
# quantity=0
# price=0
# for good in goods:
#     for code in store:
#         if goods[good] == code:
#             for i in range(len(store[code])):
#                 quantity += store[code][i]['quantity']
#                 price=quantity*store[code][i]['price']
#             print(good,'-',quantity,'шт,','стоимость',price)
#             quantity = 0

# Задача 5. Гистограмма частоты 2

# text='Здесь что-то написано'.lower()
# sym_dict=dict()
# sym_dict_inv=dict()
# max=0
# for sym in text:
#     if sym in sym_dict:
#         sym_dict[sym]+=1
#     else:
#         sym_dict[sym] = 1
#
# count=0
# for i in sym_dict:
#     count+=1
#     print(i,':', sym_dict[i])
#     # print(sym_dict[i],max)
#     if sym_dict[i]>max:
#         max=count
#
#
#
# for i in range(1,max):
#     letters=[]
#     for sym in sym_dict:
#         if sym_dict[sym]==i:
#             letters.append(sym)
#     sym_dict_inv[i]=letters
#
#
# for i in sym_dict_inv:
#     print(i,':',sym_dict_inv[i])

# Задача 6. Словарь синонимов
# Одна библиотека поручила вам написать программу для оцифровки словарей слов-синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом к парному ему слову.
# Реализуйте код, который составляет словарь слов-синонимов (все слова в словаре различны),
# затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода:
# если такого слова нет, то выведите ошибку и запросите слово ещё раз.
# При этом проверка не должна зависеть от регистра символов.
#
# Пример:
# Введите количество пар слов: 3
# 1 пара: Привет - Здравствуйте
# 2 пара: Печально - Грустно
# 3 пара: Весело - Радостно
#
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет
# count = 0
# there_is = False
# n = 3
# synonims_dict = dict()
# for i in range(1, n + 1):
#     synonims = input(f'{i} пара ').lower().split(' - ')
#     synonims_dict[i] = synonims
# # добавляем пары синонимов в словать
# word = input('введите слово ').lower()
# for i in synonims_dict:
#     count = 0
#     if word in synonims_dict[i]:
#         if word == synonims_dict[i][count]:
#             print('синоним', synonims_dict[i][count + 1])
#             there_is = True
#             break
#         print('синоним', synonims_dict[i][count])
#         there_is = True
#         break
# #
# if not there_is:
#     print('Такого слова в словаре нет.')

# Задача 7. Пицца
#
# 1 заказ: Иванов Пепперони 1
# 2 заказ: Петров Де-Люкс 2
# 3 заказ: Иванов Мясная 3
# 4 заказ: Иванов Мексиканская 2
# 5 заказ: Иванов Пепперони 2
# 6 заказ: Петров Интересная 5
# Иванов:
#     Мексиканская: 2
#     Мясная: 3
#     Пепперони: 3
# Петров:
#     Де-Люкс: 2
#     Интересная: 5

# n = 6
# data = {}
# names = []
# for i in range(n):
#     same_pizza = False
#     name, pizza, count = input(f'{i + 1} заказ ').lower().split()
#     if name not in names:
#         data[name] = {}
#     elif pizza in data[name]:
#         data[name][pizza] += int(count)
#         same_pizza = True
#     if not same_pizza:
#         data[name][pizza] = int(count)
#     names.append(name)
#
#
# for name in sorted(data):
#     print(name)
#     for pizza in sorted(data[name]):
#         print('   ',pizza, data[name][pizza])

# Пример реализации:
# Введите максимальное число: 10
#
# Нужное число есть среди вот этих чисел: 1 2 3 4 5
# Ответ Артёма: Да
#
# Нужное число есть среди вот этих чисел: 2 4 6 8 10
# Ответ Артёма: Нет
#
# Нужное число есть среди вот этих чисел: Помогите!
# Артём мог загадать следующие числа: 1 3 5

# import random
#
#
# def help(guess):
#     print('Артём мог загадать следующие числа: ',*guess)
#
#
# def check(searched_set, searched):
#     global guess
#     searched_set = set([int(item) for item in searched_set])
#     if searched in searched_set:
#         print('Ответ Артема: да')
#         guess = searched_set
#     else:
#         print('Ответ Артема: нет')
#         guess = guess - searched_set
#     return guess
#
#
# max_num = int(input('введите мксимальное число '))
# searched = random.randint(0, max_num)
# print("артем загадал число")
# Help = False
# guess = set()
# while not Help:
#     searched_set = set((input('нужное число есть среди вот этих чисел? (введите числа через пробел): ').split()))
#     if 'помоги' in searched_set:
#         help(guess)
#         Help = True
#     else:
#         guess = check(searched_set, searched)

# задача 9
# n = int(input())
#
# p_tree = {}  # это будет словарь {ребёнок=родитель}
#
# # создаём словарь p_tree
# for _ in range(1, n):  # читаем строки
#     line = input()
#     child, parent = line.split()  # ребёнок,родитель = 'str1 str2'.split()
#     p_tree[child] = parent  # p_tree[ребёнок]='родитель'
#
# # all_man = множество, все люди
# all_man = set(p_tree.keys()) | set(p_tree.values())  # (все имена в единственном числе) = (все родители) + (все дети)
#
# heights = {}  # будет словарь {предок=поколение}
#
#
# # вычисляет поколение, попутно создаёт словарь, чтоб не вычислять одно и тоже
# def f(name):  # передаём имя
#     if name not in p_tree:  # если нет родителя
#         heights[name] = 0  # предок = 0,запись в словарь heights
#         return 0  # значение поколения для дальнейшего вычисления
#     parent = p_tree[name]  # родитель = смотрим в (ребёнок=родитель)
#     if parent in heights:  # если известно поколение родителя
#         value = heights[parent] + 1  # поколение = (поколение родителя)+1
#     else:
#         value = f(
#             parent) + 1  # поколение = поколение родителя +1, имя родителя отдаём функции, она вернёт поколение родителя
#     heights[name] = value  # добавляем в словарь heights нового предка [имя] = поколение
#     return value  # значение поколения для дальнейшего вычисления
#
#
# # создадим словарь (предок=поколение)
# for name in all_man:  # возьмем всех по очереди
#     if name not in heights:  # берём только тех, кого нет в словаре (предок=поколение)
#         f(name)  # дать имени поколение попутно создавая словарь (предок-поколение)
#
# for name in sorted(heights):
#     print(name, heights[name])
#
# # как новичёк запутался в сжатом коде решения, переписал


