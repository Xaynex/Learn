# Задача 1.1
# L=int(input('левая граница '))
# R=int(input('правая граница '))
# left_list=[x**3 for x in range(L,R+1) ]
# print(left_list)
# Right_list=[x**2 for x in range(L,R+1) ]
# print(Right_list)

# задача 1.2
# stroka=input('введите строку ')
# sym=input('введите символ ')
#
# list_1=[x+x for x in stroka]
# print(list_1)
# list_1=[x+x+sym for x in stroka]
# print(list_1)

# Задача 1.3 Повышение цен
# items=[1.09,23.56,57.84,4.56,6.78]
#
# year_1=int(input('повышение 1 год: '))
# year_2=int(input('повышение 2 год: '))
#
# total=year_1+year_2
# items_new=[round(i+(total/100*i),2) for i in items]
# print(items_new)

# Задача 2.1. Список чётных чисел
# A = int(input('введите число А '))
# B = int(input('введите число B '))
# print('список из четных чисел')
# listt = [i for i in range(A, B) if i % 2 == 0]
# print(listt)

# Задача 2.2. Магазин

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_prices=[(0 if original_prices[i] < 0 else original_prices[i]) for i in range(len(original_prices))]
# print(new_prices)

# Задача 2.3 Отряды
# import random
#
# squad_1=[random.randint(50,80) for _ in range(10)]
# squad_2=[random.randint(30,60) for _ in range(10)]
#
# squad_3=[('Погиб' if (squad_1[i]+squad_2[i])>100 else 'Выжил') for i in range(10)]
#
# print(squad_1)
# print(squad_2)
# print(squad_3)

# Задача 3.1 Анализ цен

# import random
#
# original_prices = [random.randint(-10,10) for i in range(5)]
# new_prices = original_prices[:]
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print(original_prices)
#
# print("Мы потеряли: ",  abs(sum(original_prices) - sum(new_prices)))

# Задача 3.2 Срезы

# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#
# # 1.	В первой строке выведите первые пять элементов списка.
# # 2.	Во второй строке выведите весь список, кроме последних двух элементов.
# # 3.	В третьей строке выведите все элементы с чётными индексами.
# # 4.	В четвёртой строке выведите все элементы с нечётными индексами.
# # 5.	В пятой строке выведите все элементы в обратном порядке.
# # 6.	В шестой строке выведите все элементы списка через один в обратном порядке, начиная с последнего.
#
# print(nums[:5])
# print(nums[:8])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[::-2])

# Задача 3. Удаление части
# import random
# listt=[random.randint(0,10) for i in range(10)]
# B=random.randint(7,10)
# A=random.randint(0,6)
#
# new=listt[:]
#
# print(new)
# print(A,B)
# print(new[:A]+new[B+1:])

# ============================================================================
# Задача 1. Гласные буквы

# def check_vowel_letters(text):
#     vowel_letters = 'аоуыэеёиюя'
#     letters = [i for i in text if i in vowel_letters]
#     print(letters)
#
#
# text = list(input('введите текст '))
#
# check_vowel_letters(text)

# Задача 2. Генерация
# Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел,
# на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего
# номера на 5.
#
# Пример:
# Введите длину списка: 10
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]

# N = int(input('длинна списка '))
# listt = [(1 if i % 2 == 0 else i % 5) for i in range(10)]
# print(listt)

# Задача 3. Случайные соревнования
# Пример:
# Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
# Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
# Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]

# import random
# team_1=[round(random.uniform(5,10),2) for i in range(20)]
# team_2=[round(random.uniform(5,10),2) for i in range(20)]
#
# team_3=[team_1[i] if team_1[i]>team_2[i] else team_2[i] for i in range(len(team_1))]
# print(team_1)
# print(team_2)
# print(team_3)

# Задача 4. Тренируемся со срезами
# Дана строка, в которой хранятся первые семь букв английского алфавита.
# alphabet = 'abcdefg'
# Напишите программу, которая выводит на экран 10 вот таких результатов:
# 1.	Копия строки.
# 2.	Элементы строки в обратном порядке.
# 3.	Каждый второй элемент строки (включая самый первый).
# 4.	Каждый второй элемент строки после первого.
# 5.	Все элементы до второго.
# 6.	Все элементы, начиная с конца до предпоследнего.
# 7.	Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
# 8.	Последние три элемента строки.
# 9.	Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
# 10.	То же, что и в предыдущем пункте, но в обратном порядке.
# Для получения и вывода результатов используйте только команду print и срезы.

# alphabet = 'abcdefg'
# alphabet_copy = alphabet[:]
# print('правильно',alphabet_copy)
# print('правильно',alphabet[::-1])
# print('правильно',alphabet[0::2])
# print('правильно',alphabet[1::2])
# print('правильно',alphabet[:1])
# print('правильно',alphabet[6:])
# print('правильно',alphabet[3:4])
# print('правильно',alphabet[4:])
# print('правильно',alphabet[3:5])
# print('правильно',alphabet[4:2:-1])

# Задача 5. Разворот
# На вход в программу подаётся строка, в которой буква h встречается
# как минимум два раза. Реализуйте код, который разворачивает последовательность
# символов, заключённую между первым и последним появлением буквы h, в противоположном порядке.
#
# stroka='abhabchabchk'
# first_index=stroka.index('h')
# last_index=stroka.rfind('h')
# stroka2=stroka[last_index-1:first_index:-1]
# print(stroka2)

# Задача 6. Сжатие списка
# Дан список из N целых чисел. Напишите программу, которая выполняет «сжатие списка» —
# переставляет все нулевые элементы в конец массива.
# При этом все ненулевые элементы располагаются в начале массива в том же порядке.
# Затем все нули из списка удаляются.

# import random
# count = 0
# stroka = [random.randint(0, 2) for i in range(20)]
# print(stroka)
# for i in range(20):
#     for i in stroka:
#         if count == 19:
#             break
#         if i == 0:
#             stroka[count], stroka[count + 1] = stroka[count + 1], stroka[count]
#         count += 1
#     count = 0
# print(stroka)
# count0 = 0
# for i in stroka:
#     if i == 0:
#         count0 += 1
# a = len(stroka) - count0
# print(stroka[:a])

# Задача 7. Двумерный список
# Как мы говорили ранее, в программировании часто приходится писать код исходя
# из результата, который требует заказчик. В этот раз заказчику нужно получить
# вот такой двумерный список:
#
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
# Напишите программу, которая генерирует такой список и выводит его на экран.
# Используйте только list comprehensions.

# lst=[]
# [lst.append([i+1,5+i,9+i]) for i in range(4)]
# print(lst)

# Задача 8. Развлечение N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем по
# этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно. Определите,
# какие палки остались стоять на месте. Напишите программу, которая получает на вход количество палок N и количество
# бросков K. Далее идёт K пар чисел L_i, R_i, при этом 1≤ L_i≤ R_i≤ N. Программа должна вывести последовательность из
# N символов, где j-й символ есть “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

# import random
# N=int(input('введите количество палочек '))
# lst=[]
# [lst.append('I') for _ in range(N)]
# print(*lst)
# K=int(input('введите количество бросков '))
# for i in range(K):
#     L_i=random.randint(1,N//2)
#     R_i=random.randint(N//2,N)
#     # print(L_i, R_i)
#     lst[L_i:R_i]='.'*(R_i-L_i)
# print(*lst)

# Задача 9
# lst=[]
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# lst=[iii for i in nice_list for ii in i for iii in ii]
# # for i in nice_list:
# #     for ii in i:
# #         for iii in ii:
# #             lst.append(iii)
# print(lst)


