Задача 1. Сумма чисел 2

def summa_n(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

n=int(input('enter the number '))
first = summa_n(n)
second=summa_n(first)
print(first)
print(second)


задача 3
def numeral_count(x):
    maxnum = 0
    maximum = 0
    for i in range(x):
        count = 0
        num = int(input('введите число '))
        lastnum = num
        while num != 0:
            num = num//10
            count += 1
        if count > maximum:
            maximum = count
            maxnum = lastnum
    print('самое длинное кол цифр', maximum)
    return maxnum


n = int(input('введите количество задач '))
main = numeral_count(n)
print('Первая задача на обработку: ', main)


задача 13.3

Задача 1. Возможности компьютера
rez = 1
count = 1
while rez > 0:
    count += 1
    rez = rez / 2
    print(rez)
print(count)

Задача 2. Тестирование
x = 1
num = float(input('Введите число в эксп. форме: '))
count = 0
while x < 2:
    x += num
    count += 1
print('прибавлений', count)

Задача 3. Урок информатики
x = float(input('введите число больше 10 '))
maximum = 0
count = -1
num = x
while x != 0:
    x = x // 10
    count += 1
    print(x)
print('Формат плавающей точки: x = ', num / (10 ** count), '* 10 **', count)

13.4
задача 1 опять налоги
def func(tax, new_tax):
    s=tax+new_tax
    if s!=tax:
        print('бюджет увеличится')
    else:
        print('бюджет не изменится')


tax = float(input('введите бюджет страны '))
new_tax = float(input('Новые поступления налог '))
func(tax, new_tax)

Задача 2. Сравнение

def eqv(a, b, compare):
    if round(a + b, 15) == round(compare, 15):
        return True
    else:
        return False


a = float(input('введите 1 число '))
b = float(input('введите 2 число '))
compare = float(input('введите 3 число '))

print(eqv(a, b, compare))

домашнее задание
задача 1 урок инф 2

x = float(input('введите число больше 10 '))
maximum = 0
count = -1
num = x
if x > 10:
    while x != 0:
        x = x // 10
        count += 1
        print(x)
    print('Формат плавающей точки: x = ', num / (10 ** count), '* 10 **', count)
elif 10 > x > 0:
    count = -2
    while x != 0:
        x = x // 10
        count -= 1
        print(x)
    print('Формат плавающей точки: x = ', num / (10 ** count), '* 10 **', count)

Задача 2. Генеалогическое древо
def get_parent_names_total_length(family):
    count = 0
    for i in family:
        count += 1
    return count


father = input('ФИО отца ')
mother = input('ФИО матери ')

a = get_parent_names_total_length(father)
print('количество символов', a)
b = get_parent_names_total_length(mother)
print('количество символов', b)
print('всего символов', a+b)

Задача 3. Функция максимума

def max_two(first,sekond):
    if first>sekond:
        return first
    else:
        return sekond


first=int(input('введите 1 число '))
sekond=int(input('введите 2 число '))
third=int(input('введите 3 число '))
rez=max_two(first,sekond)
total=max_two(rez,third)
print(total)

Задача 4. Число наоборот 2

def inverse(num):
    rez = ''
    while num != '':
        num = int(num)
        ost = str(num % 10)  # взяли последнюю цифру
        num = str(num)
        num = num[:-1]
        rez += ost  # прибавили ее
    rez = int(rez)
    return rez  # вывели


num1 = int(input('введите число 1 '))
num2 = int(input('введите число 2 '))

print('первое число наоборот', inverse(num1))
print('второе число наоборот', inverse(num2))

print('сумма', inverse(num1) + inverse(num2))
print('cумма наоборот', inverse(inverse(num1) + inverse(num2)))

Задача 5. Урок информатики 3

На вход подаётся строка — это экспоненциальная форма числа. Напишите программу,
которая выводит отдельно мантиссу и отдельно порядок этого числа.

text = input('Введите число в экспоненциальной форме: ')
parts = text.split('e')

print('Манттиса:', parts[0])
print('Порядок числа:', parts[1])

Задача 6. Число Эйлера
# Напишите программу, которая находит сумму нижеприведённого ряда с точностью до 1e-5.
import math
precision=1e-5
argument=1
i=0
e=0
while argument>precision:
    argument=1/math.factorial(i)
    i+=1
    e+=argument
print(e)

Задача 7. Поехали по Марсу
x = 1.496e9
y = 0
while True:
    print('Марсоход на позиции ', x, y, 'Введите команду: ')
    akt = input('')
    if akt == 'w':
        y += 1
    elif akt == 's':
        y -= 1
    elif akt == 'a':
        x -= 1
    elif akt == 'd':
        y += 1

Задача 8. Недоделка 2

def inverse(num):
    num_count = count(num)
    last_digit = num % 10
    first_digit = num // 10 ** (num_count - 1)
    between_digits = num % 10 ** (num_count - 1) // 10
    num = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое число:', num)

    return num


counter = 0


def count(num):
    global counter
    counter += 1
    num_count = 0
    temp = num
    while temp > 0:
        num_count += 1
        temp = temp // 10
    check(num_count, counter)

    return num_count


def check(num_count, counter):
    if num_count < 3 and counter == 1:
        print("В первом числе меньше трёх цифр.")
        quit()
    elif num_count < 4 and counter == 2:
        print("Во втором числе меньше четырёх цифр.")
        quit()


first_n = int(input("Введите первое число: "))
first_n = inverse(first_n)

second_n = int(input("\nВведите второе число: "))
second_n = inverse(second_n)

print('сумма', first_n + second_n)

Задача 9. Степень числа
Дано вещественное положительное число a и целоe число n.
Вычислите a в степени n, не используя циклы, возведение в степень через **
и функцию math.pow() (да, такая тоже есть). Решение оформите в виде функции power(a, n).
import math


def power(a, n):
    print(math.pow(a, n))


a = float(input('введите вещественное число '))
n = int(input('введите целое число '))

power(a, n)

Задача 10. Маятник

def check(start, end):
    if (start < 0 or end < 0) or (start == 0 and end == 0):
        print('ошибка ввода')
        quit()


start = float(input('введите начальную амплитуду '))
end = float(input('введите конечную амплитуду '))
check(start, end)
count = 0

while start > end:
    start = start - (start / 100 * 8.4)
    count += 1

print('Маятник считается остановившимся через', count, ' колебаний')

Задача 11. Яйца
def calc_depth(depth_top, depth_bottom):
    return depth_top + (depth_bottom - depth_top) / 2


def calc_danger(depth):
    return depth ** 3 - 3 * depth ** 2 - 12 * depth + 10


max_danger = float(input('Введите максимально допустимый уровень опасности: '))
depth_top = 0.0
depth_bottom = 4.0

if max_danger <= 0:
    print('Ошибка. Максимально допустимый уровень должен быть больше 0')
else:
    depth = calc_depth(depth_top, depth_bottom)
    danger = calc_danger(depth)
    # print('Глубина:', depth, 'Опастность:', danger)
    while abs(danger) > max_danger:
        if danger > 0:
            depth_top = depth
        else:
            depth_bottom = depth
        depth = calc_depth(depth_top, depth_bottom)
        danger = calc_danger(depth)
        # print('Глубина:', depth, 'Опастность:', danger)
    print('Приблизительная глубина безопасной кладки: ', depth, 'm')

Задача 12. Сумма ряда
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def degree(x, n):
    degree1 = 1
    for i in range(1, n + 1):
        degree1 = degree1 * x
    return degree1


precision = float(input('введите точность '))
x = int(input('введите х '))
precision = 0.001
x = 5
count = 0
part = 1
summ = 0
count2 = 1
while abs(part) > precision:
    count2 += 1
    count += 2
    part = degree(x, count) / factorial(count)
    if count2 % 2 == 0:
        summ = summ + part
    elif count2 % 2 != 0:
        summ = summ - part

print(1-summ)


