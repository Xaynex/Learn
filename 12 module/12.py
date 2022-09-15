#1 задача
"""
def summa_n(N):
 sum=0
 for i in range(1,N+1):
  sum= sum+i
 print('я знаю что сумма чисел от 1 до', N,'равна',sum)

N=int(input('введите число '))
summa_n(N)

#Задача 2. Функция в функции

def negative():
 print('отричательное')
def positive():
 print('положительное')

def test():
    num=int(input('введите целове число: '))
    if num>0:
     positive()
    else:
     negative()

test()

#3
import math
def sircle():
    r=int(input('введите радиус '))
    print(math.pi*r**2)
def kv():
    a = int(input('введите сторону а '))
    b = int(input('введите сторону b '))
    print(a*b)
def tr():
    a = int(input('введите сторону а '))
    b = int(input('введите сторону b '))
    aa = int(input('введите угол '))
    print(1/2*a*b*math.sin(aa))


choise=int(input('1- круг, 2 - квадрат, 3 - треугольник '))

if choise==1:
     sircle()
elif choise==2:
     kv()
elif choise==3:
     tr()

# 4
def summ(num):
    sum=0
    for i in range(num):
        sum=sum+i
    print(sum)
def maxmin(num):
    minimum, maximum = 9, 0
    while num:
        num, n = divmod(num, 10)
        minimum = min(minimum, n)
        maximum = max(maximum, n)

    print(f"Minimum = {minimum}, Maximum = {maximum}")

while True:
    num = int(input('введите число '))
    action = int(input('1 - вывести сумму его цифр,  2 - макс и мин цифра '))
    if action==1:
        summ(num)
    elif action==2:
        maxmin(num)
"""

def inverse(num):
    rez=''
    for i in range(4):
        num=int(num)
        ost = str(num%10)#взяли последнюю цифру
        num = str(num)
        num=num[:-1]
        rez+=ost          #прибавили ее
        print (rez)       #вывели

while True:
    num = int(input('введите число '))
    inverse(num)