# Задача 1. Зоопарк
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1,'bear')
# zoo.remove('elephant')
# print(zoo)
# print(zoo.index('lion')+1)
# print(zoo.index('monkey')+1)

# Задача 2. Сокращения

# N=int(input('кол-во сотрудников '))
# listt=[]
# count=0
# for i in range(1,N+1):
#     print('зарплата',i,'сотрудника ',end='')
#     salary=int(input())
#     if salary != 0:
#         listt.append(salary)
#         count+=1
#
# print(count)
# print(listt)
# print(max(listt))
# print(min(listt))

# Задача 1. Задачи компаний
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
# count=main.count(0)
# print(main)
# print(count)

# Задача 2. Вредоносное ПО
# first_massage=input('Первое сообщение ')
# second_massage=input('Второе сообщение ')
#
# first_count=first_massage.count('!')+first_massage.count('?')
# second_count=second_massage.count('!')+second_massage.count('?')
#
# if first_count>second_count:
#     print(first_massage+second_massage)
#
# else:
#     print(second_massage+' '+first_massage)

# Задача 1. Матрица
# matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
#
# for ii in range(len(matrix)):
#     for i in range(len(matrix)):
#         print(matrix[ii][i], end='')
#     print()

# Задача 2. Олимпиада
# N=int(input('введите количество участников '))
# people=list(range(1,N+1))
# teams=[]
# num=1
# K=int(input('введите количество человек в команде '))
# if N%K==0:
#     for i in range(N//K):
#         teams.append(list(range(num,num+ K)))
#         num+=K
#     print(teams)
# else:
#     print(N, 'участников невозможно поделить на команды по ',K, 'человек')

# Задача 3. Лавка
# new_box=[]
# box=[["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
# print('текущий ассортимент',box)
# print('новый фрукт ', end='')
# fruit_name =input()
# print('цена ',end='')
# price=int(input())
# new_box.append(fruit_name)
# new_box.append(price)
# box.append(new_box)
#
# print('новый ассортимент',box)
# for ii in range(len(box)):
#         box[ii][1] = box[ii][1]+ box[ii][1]*0.08
#
# print('новый ассортимент с увеличенной ценой',box)
# =====================================================
# Задача 1 страшный код
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
#
# a.extend(b)
# print(a.count(5))
# a = [1, 5, 3]
# a.extend(c)
# print(a.count(3))
# a = [1, 5, 3]
# a.extend(b)
# a.extend(c)
# print(a)

# Задача 2. Шеренга
# Два класса стоят в две отдельные шеренги. В каждом классе ученики выстроены по росту (по возрастанию):
# в одном классе от 160 см до 176 см с шагом 2, во втором классе — от 162 см до 180 см с шагом 3.
# Спустя какое-то время два класса объединяют в одну шеренгу и тоже выстраивают их по возрастанию.
# Напишите программу, которая генерирует списки роста для каждого в классе, затем объединяет их в один список
# и сортирует его в порядке возрастания. Выведите отсортированный список на экран.

# class1 = list(range(160, 176, 2))
# class2 = list(range(162, 180, 3))
#
# print(class1)
# print(class2)
# class1.extend(class2)
# max = 0
# min = 0
# print(class1)
# for ii in range(len(class1)):
#     for i in range(0,len(class1)-1,1):
#         if class1[i] > class1[i+1]:
#             class1[i], class1[i + 1] = class1[i + 1], class1[i]
#
# print(class1)

# Задача 3. Детали
# В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# Продавец решил, что считать количество и стоимость деталей вручную не очень удобно, поэтому решил попросить помощи у программиста, чтобы оптимизировать этот процесс.
# Напишите программу, которая запрашивает у пользователя деталь, считает их количество, а также общую стоимость.
#
# Пример:
# Название детали: седло

# Кол-во деталей - 3
# Общая стоимость - 4500

# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# name=input('название детали: ')
# count=0
# total=0
# for i in range(len(shop)):
#     if shop[i][0] == name:
#         count+=1
#         price=shop[i][1]
#         total+=price
#
# print(count)
# print(price)

# задача 4

# def check(ask):
#     if (ask != 'ушел' or ask == 'пришел') and len(guests)>5:
#         print('места нет')
#
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# ask=str
# while ask!='пора спать':
#     ask = input('гость пришел или ушел? ')
#     if ask == 'пора спать':
#         quit()
#     name = input('имя гостя ')
#     check(ask)
#     if ask == 'пришел' and len(guests)<=5:
#         guests.append(name)
#         print('заходи')
#         print(guests)
#     if ask == 'ушел':
#         guests.remove(name)
#         print('пока')
#         print(guests)


# Задача 5. Песни
# def search(song):
#     time = 0
#     for i in range(9):
#         if violator_songs[i][0] == song:
#             return violator_songs[i][1]
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]]
# N = int(input('сколько песен выбрать '))
# total = 0
# for i in range(1, N + 1):
#     print('название', i, 'песни ', end='')
#     song = input()
#     time = search(song)
#     total += time
# print('общее время', round(total,2))

# Задача 6. Уникальные элементы
# first_list = [1,2,3]
# # second_list = [2, 4, 6, 3, 3, 2, 1]
# second_list = [3,4,3,3]
#
#
# print('Первый список:', first_list, '\nВторой список:', second_list)
# first_list.extend(second_list)
# for number in first_list:
#     for quantity_remove in range(first_list.count(number) - 1):
#         first_list.remove(number)
#         print(first_list)

# Задача 7. Ролики
# ski=[41,40,39,42]
# leg=[41,41,42,33,44]
# count=0
# for i in range(len(leg)):
#     print('нога',leg[i-count])
#     for ii in range(len(ski)):
#         print('коньки',ski[ii])
#         if ski[ii]>=leg[i-count] and ski!=0 and leg!=0:
#             leg.remove(leg[i-count])
#             ski.remove(ski[ii])
#             print('подошло')
#             count+=1
#             break
#         else:
#             print('не подошло')
#
# print(count)