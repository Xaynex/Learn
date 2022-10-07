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

