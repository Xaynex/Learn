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
# Задача страшный код
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print(a.count(5))
a = [1, 5, 3]
a.extend(c)
print(a.count(3))
a = [1, 5, 3]
a.extend(b)
a.extend(c)
print(a)
