#1 вода
"""
def lol(x):
    print('название: КлирВотер')
    print('Производитель: ВодЗавод')
    print('цена', x)


lol(25)
lol(30)
lol(40)

#Задача 2. Вот это объёмы 2
import math
def sphereArea(r):
    print('площадь',round(4*math.pi*r**2,2))

def sphereValume(r):
    print('обьем', round((4*math.pi*r**3)/3,2))
r=float(input('введите радиус планеты '))

sphereArea(r)
sphereValume(r)

#Задача 3 функция
import math

def func(x):
    if -5<=x<=5:
        y=math.exp(x)
    elif x<-5:
        y=2-abs(x)-1
    elif x>5:
        y=2*x
    print('при x = ', x, 'у =', y)

for x in range(-10,11):
    func(x)

#Задача 1. Среднее арифметическое
def avr(a,b):
    print((a+b)/2)
a=int(input('ведите левую границу: '))
b=int(input('Введите правую границу: '))

avr(a,b)


#Задача 3. навигатор
import math
def distance():
    print('введите координаты точки')
    x=int(input('коордитаны икс '))
    y = int(input('коордитаны игрек '))
    print('расстояние ', math.sqrt(x**2+y**2))
def betwdistaanse():
    print('введите координаты точки')
    x1 = int(input('коордитаны икс1 '))
    y1 = int(input('коордитаны игрек1 '))
    x2 = int(input('коордитаны икс2 '))
    y2 = int(input('коордитаны игрек2 '))
    print('расстояние ', math.sqrt((x2-x1)**2+(y2-y1)**2))

ch=int(input(('1-от себя до точки/ 2- между точками ')))
if ch ==1:
    distance()
elif ch ==2:
    betwdistaanse()
else:
    print('ошибка ввода')

import sympy
n=int(input('введите количество чисел: '))
for i in range(n):
    num=int(input('введите число: '))
    if sympy.isprime(num) == True:
        print('число простое')
    else:
        print('число не простое ')



#Задача 6. Текстовый редактор

def count_letters(text):
    search_num = input('какую цифру ищем ')
    search_sym = input('какую букву ищем ')
    count_num=0
    count_sym=0
    for i in text:
        if i ==search_num:
            count_num+=1
    for i in text:
        if i ==search_sym:
            count_sym+=1

    print('количество цифр', search_num, ':', count_num)
    print('количество букв', search_sym, ':', count_sym)

text = input('введите текст ')
count_letters(text)

#Задача 7. Вторая цифра

def func(x):
    rez=x*100
    rez=int(rez)
    rez=rez%10
    print(rez)

x=float(input('введите число '))
func(x)

#Задача 8. Монетка


def search(x,y):
    if x <= 1 and y <= 1:
        print('монетка где то рядом')
    else:
        print('монетки в области нет')

x=abs(float(input('введите координату х: ')))
y=abs(float(input('введите координату y: ')))

search(x,y)

#Задача 10. НОД
def nod (f,s):
    max = 0
    for d in range(1, f + s):
        if f % d == 0 and s % d == 0:
            if d > max:
                max = d
    print('максимальный общий делитель', max)
f=int(input('введите 1 число '))
s=int(input('введите 2 число '))
nod(f,s)

#задача 11
def sum(k1,k5,k10,k50):
    sum=1*k1+5*k5+10*k10+50*k50
    print('всего',sum/100,'рубля')

k1 = int(input('монет по 1 копейке '))
k5= int(input('монет по 5 копеек '))
k10= int(input('монет по 10 копеек '))
k50= int(input('монет по 50 копеек '))

sum(k1,k5,k10,k50)

import random
#задача 12
def rock_paper_scissors():
    #Здесь будет игра "Камень, ножницы, бумага"
    possible_actions = ['камень', 'бумага', 'ножницы']
    computer_action = random.choice(possible_actions)
    choise=int(input('1-камень, 2-бумага, 3-ножницы '))
    if choise==1:
        my_action='камень'
    elif choise==2:
        my_action='бумага'
    elif choise == 3:
        my_action = 'ножницы'
    print('вы выбрали', my_action,'компьютер выбрал', computer_action)
    if my_action==computer_action:
        print('ничья')
    elif my_action=='камень':
        if computer_action=='бумага':
            print('вы проиграли')
    elif my_action=='ножницы':
        if computer_action=='камень':
            print('вы проиграли')
    else:
        print('вы выиграли')

def guess_the_number():
    #Здесь будет игра "Угадай число"
    num=random.randint(1,100)
    print(num)
    my_num=0
    while my_num!=num:
        my_num=int(input('угадайте число '))
        if my_num>num:
            print('ваше число больше')
        else:
            print('ваше число меньше')
    print('угадал')

def mainMenu():
    #Здесь главное меню игры
    choise=int(input('выберите игру. 1 - угадай число. 2 - камень ножницы бумага '))
    if choise ==1:
        guess_the_number()
    elif choise ==2:
        rock_paper_scissors()

mainMenu()
"""




