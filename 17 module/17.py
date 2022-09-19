# Задача 1
# L=int(input('левая граница '))
# R=int(input('правая граница '))
# left_list=[x**3 for x in range(L,R+1) ]
# print(left_list)
# Right_list=[x**2 for x in range(L,R+1) ]
# print(Right_list)

# задача 2
# stroka=input('введите строку ')
# sym=input('введите символ ')
#
# list_1=[x+x for x in stroka]
# print(list_1)
# list_1=[x+x+sym for x in stroka]
# print(list_1)

# Задача 3. Повышение цен
# items=[1.09,23.56,57.84,4.56,6.78]
#
# year_1=int(input('повышение 1 год: '))
# year_2=int(input('повышение 2 год: '))
#
# total=year_1+year_2
# items_new=[round(i+(total/100*i),2) for i in items]
# print(items_new)