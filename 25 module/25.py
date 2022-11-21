# # Задача 1. Координаты точки
#
# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         self.__x = x
#
#     def set_y(self, y):
#         self.__y = y
#
#     def __str__(self):
#         return f'x={self.get_x()},y={self.get_y()}'
#
#
# p = Point(1, 2)
# p.set_y(10)
# p.set_x(123)
# print(p)

# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем
# (имя должно состоять только из букв) и возрастом (должен быть в диапазоне от 0 до 100),
# а внутри класса считается общее количество инициализированных объектов. Реализуйте
# сокрытие данных для всех атрибутов (как статических, так и динамических), а для изменения
# и получения данных объекта напишите специальные геттеры и сеттеры.
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в уроке.

# class Person:
#
#     def __init__(self,name,age):
#         self.set_name(name)
#         self.set_age(age)
#
#     def set_name(self,name):
#         if name.isalpha():
#             self.__name=name
#         else:
#             raise 'в имени есть символы'
#
#     def set_age(self,age):
#         if 100>age>0:
#             self.__age=age
#         else:
#             raise 'некорректный возраст'
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# a=Person('Dima',24)
# a.set_age(12)
# print(a.get_age())

# Описание
# Задача 1. Корабли
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель,
# и каждый может сделать два действия: сообщить свою модель и идти по воде.
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля.
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
# Реализуйте классы грузового и военного кораблей.
# Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование.
# Не забудьте про функцию super в дочерних классах.

# class Ship():
#
#     def __init__(self, model):
#         self.__model = model
#
#     def float(self):
#         print('корабль куда то плывет')
#
#
# class Warship(Ship):
#
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.__gun = gun
#
#     def atack(self):
#         print('корабль атакует с помощью', self.__gun)
#
#
# class Cargoship(Ship):
#
#     def __init__(self, model):
#         super().__init__(model)
#         self.__full = 0
#
#     def load_cargo(self):
#         self.__full += 1
#         print('грузим корабль')
#
#     def unload_cargo(self):
#         if self.__full == 0:
#             print('корабль разгружен')
#         else:
#             self.__full -= 1
#             print('разгружаем корабль')
#
#
# warship=Warship('инстасамка','стринги')
# warship.float()
# warship.atack()
#
# cargoship=Cargoship('путин')
# cargoship.float()
# cargoship.load_cargo()
# cargoship.unload_cargo()

# Задача 2. Роботы

# class Robot:
#
#     def __init__(self, modele):
#         self.gun = None
#         self.bag = None
#         self.VacuumRob = None
#         self.Submarine = None
#         self.WarRob = None
#         self.modele = modele
#
#     def operate(self):
#         if self.WarRob:
#             print('защита обьекта с помощью', self.gun)
#         elif self.Submarine:
#             print('охрана ведётся под водой')
#         elif self.VacuumRob:
#             print('робот пылесосит пол')
#             self.bag += 1
#             print('заполненность мешка', self.bag)
#
#     def move(self):
#         return '{modele} двигается'.format(modele=self.modele)
#
#
# class VacuumRob(Robot):
#
#     def __init__(self, modele):
#         super().__init__(modele)
#         self.bag = 0
#         self.VacuumRob = True
#         # print('инициализация робота пылесоса')
#
#
# class WarRob(Robot):
#
#     def __init__(self, modele, gun):
#         super().__init__(modele)
#         self.WarRob = True
#         self.gun = gun
#         # print('инициализация боевого робота')
#
#
# class Submarine(WarRob):
#
#     def __init__(self, modele, gun):
#         super().__init__(modele, gun)
#         self.deep = 100
#         self.Submarine = True
#         # print('инициализация подводного робота')
#
#     def move(self):
#         info = super().move()
#         info = info+'на глубине {} меторов'.format(self.deep)
#         return info
#
#
# warob = WarRob('боевой робот', 'пушки')
# Submarine = Submarine('подлодка', 'тарпеды')
# print(warob.move())
# print(Submarine.move())

# Задача 3. Кастомные исключения
# Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое число на
# второе и выводит ответ на экран. Если первое число меньше второго,
# то программа выдаёт исключение DivisionError (нельзя делить большее на меньшее).
# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.

# class DivisionError(Exception):
#     pass
#
# try:
#     with open('numbers.txt', 'r') as file:
#         for num in file:
#             num_1, num_2 = num.split()
#             num_1, num_2 = int(num_1), int(num_2)
#             if num_1 > num_2:
#                 raise DivisionError
#             else:
#                 res = num_1 / num_2
#                 print(round(res, 2))
# except DivisionError:
#     print('нельзя делить большее на меньшее')
#
# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
# Также есть два дочерних класса:
# •	Солдат: получает урон, равный переданному значению.
# •	Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
# (а также инкапсуляции и наследования, конечно же).

# class Unit:
#
#     def __init__(self, hp=100):
#         self.hp = hp
#
#     def get_hurt(self, hurt):
#         return 'получает урон, здоровья осталось', self.hp
#
#     def __str__(self):
#         return 'здорове {} '.format(self.hp)
#
#
# class Solgere(Unit):
#
#     def __init__(self, hp):
#         super().__init__(hp)
#
#     def get_hurt(self, hurt):
#         self.hp -= hurt
#         print('удар солдату')
#         return super().get_hurt(hurt)
#
#
# class Person(Unit):
#
#     def __init__(self, hp):
#         super().__init__(hp)
#
#     def get_hurt(self, hurt):
#         self.hp -= hurt * 2
#         print('удар человеку')
#         return super().get_hurt(hurt)
#
#
# s = Solgere(100)
# s.get_hurt(10)
# print(s)
# p = Person(100)
# p.get_hurt(20)
# print(p)

# Задача 1. Налоги
# class Property:
#
#     def __init__(self, worth):
#         self.countryHouse = None
#         self.car = None
#         self.apartment = None
#         self.worth = worth
#
#     def count_tax(self):
#         if self.apartment:
#             return round(self.worth / 1000,2)
#         if self.car:
#             return round(self.worth / 200,2)
#         if self.countryHouse:
#             return round(self.worth / 500,2)
#
#
# class Apartment(Property):
#
#     def __init__(self, worth):
#         super().__init__(worth)
#         self.apartment = True
#
#
# class Car(Property):
#
#     def __init__(self, worth):
#         super().__init__(worth)
#         self.car = True
#
#
# class CountryHouse(Property):
#
#     def __init__(self, worth):
#         super().__init__(worth)
#         self.countryHouse = True
#
#
# print('Имущество:\n'
#       '1. Квартира\n'
#       '2. Машина\n'
#       '3. Дом')
#
# # try:
# answer = int(input())
# if answer not in (1, 2, 3):
#     raise ValueError('попробуйте еще раз')
# worth = int(input('стоимость '))
# money=int(input('сколько у вас денег? '))
# obj = Apartment(worth) if answer == 1 else Car(worth) if answer == 2 else CountryHouse(worth)
# print('размер налога: ',obj.count_tax())
# if money<obj.count_tax():
#     print('не хватает',obj.count_tax()-money,'доларов')
# except:
#     print('ошибка')

# Задача 2. Карма
# Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа),
# чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(),
# которая возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
# •	KillError
# •	DrunkError
# •	CarCrashError
# •	GluttonyError
# •	DepressionError
# Напишите такую программу. Функцию оберните в бесконечный цикл,
# выход из которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.

# class KillError(Exception):
#     pass
#
#
# class DrunkError(Exception):
#     pass
#
#
# class CarCrashError(Exception):
#     pass
#
#
# class GluttonyError(Exception):
#     pass
#
#
# class DepressionError(Exception):
#     pass
#
#
# import random
#
# day = 0
# karma = 0
#
#
# def one_day():
#     crash = random.randint(1, 10)
#     if crash == 1:
#         raise random.choice([KillError('убийство'),
#                              DrunkError('пьянство'),
#                              CarCrashError('авария'),
#                              GluttonyError('чревоугодие'),
#                              DepressionError('депрессия')])
#     return random.randint(1, 7)
#
#
# while True:
#     try:
#         day += 1
#         karma += one_day()
#         if karma >= 500:
#             break
#     except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as err:
#         with open('karma.log', 'a') as karma_log:
#             karma_log.write('день {}, проступок: {} - {}\n'.format(day, err.__class__.__name__,err))

# Задача 3. Свой словарь
# В силу обстоятельств Васе постоянно приходится работать со словарями и их данными.
# В том числе и с методом get, который по умолчанию возвращает None, если такого ключа в словаре нет.
# Однако Васю это не устраивает: для нормальной работы ему нужно возвращать число 0.
# Реализуйте класс MyDict, который будет вести себя точно так же, как и обычный словарь,
# за исключением того, что метод get по умолчанию будет возвращать не None, а число 0.


# class MyDict(dict):
#
#     def get(self,__key):
#         return super().get(__key,0)
#
#
# a = MyDict()
# a[1] = 'первый'
# a['2'] = 2
# print(a.get(1))
# print(a.get('1'))

# Задача 4. Компания

# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return str(self.__name)
#
#     def get_age(self):
#         return str(self.__age)
#
#     def __str__(self):
#         return self.__name
#
#
# class Employee(Person):
#
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def count_salary(self):
#         return 'зарплата {} ({})'.format(self.get_name(),self.position)
#
#     def __str__(self):
#         return self.get_name()+' '+self.position
#
#
# class Manager(Employee):
#     position = 'менеджер'
#
#     def count_salary(self):
#         return 13000
#
#
#
# class Agent(Employee):
#     position = 'агент'
#
#     def count_salary(self):
#         __sales = 12300
#         __salary = 5000 + ((__sales / 100) * 5)
#         return __salary
#
#
# class Worker(Employee):
#     position = 'рабочий'
#
#     def count_salary(self):
#         __hours = 100
#         __salary = 100 * __hours
#         return __salary
#
#
# Dima = Manager('дима', 24)
# Alena = Manager('Алена', 20)
# Vita = Agent('витя', 25)
# Kata = Agent('катя', 34)
# Anton= Worker('Антон',27)
# Tanya= Worker('Таня',21)
#
#
# lst=[Dima,Alena,Vita,Kata,Anton,Tanya]
# total_salary=0
# for Employee in lst:
#     print(Employee.get_name(), end=' ')
# for Employee in lst:
#     total_salary+=Employee.count_salary()
#
# print('\n',total_salary)

# Задача 5. А-а-автомобиль!
# import math
# import random
# class Car:
#
#     def __init__(self, x:int, y:int, a:float):
#         self.x = x
#         self.y = y
#         self.a = a
#
#     def move(self,dist):
#         self.x = self.x + dist * math.cos(self.a)
#         self.y = self.y + dist * math.sin(self.a)
#
#     def __str__(self):
#         return f'Координаты: X={round(self.x, 2)} Y={round(self.y, 2)}'
#
#
#
# class Bus(Car):
#
#     def __init__(self, x, y, a):
#         super().__init__(x, y, a)
#         self.money = 0
#         self.passangers = 0
#         self.PAY_COEFFICIENT=0.2
#         self.max_passangers=60
#
#     def get_on(self,quontity):
#         if self.passangers>=self.max_passangers:
#             print('автобус заполнен')
#             quit()
#         else:
#             self.passangers += quontity
#
#     def get_off(self,quontity):
#         if self.passangers<=0:
#             print('автобус пустой')
#         else:
#             self.passangers -= quontity
#
#     def move(self,distance):
#         self.money += self.PAY_COEFFICIENT * self.passangers * distance
#         super().move(distance)
#
#     def __str__(self):
#         return 'денег: {} \nпассажиров {}'.format(round(self.money,2), self.passangers)\
#                +  f'\nКоординаты: X={round(self.x, 2)} Y={round(self.y, 2)}'
#
#
#
# bus = Bus(1, 2, 40)
#
# for i in range(random.randint(10,20)):
#     bus.get_on(random.randint(3,10))
#     bus.get_off(random.randint(2,5))
#     bus.move(10)
#     print('остановка',i+1)
#     print(bus)
#     print()


# Задача 6. Совместное проживание 2
# import random
#
#
# class House:
#     money = 100
#     food = 50
#     cat_food = 30
#     dirt = 0
#
#     def __str__(self):
#         return 'денег: {}, еды: {}, еды для кота: {}, грязи: {}'.format(self.money, self.food, self.cat_food, self.dirt)
#
#
# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         self.satiety = 30
#
#     def eat(self):
#         if House.cat_food > 10:
#             House.cat_food -= random.randint(5, 10)
#             self.satiety += 3
#             print(self.name, 'кушает')
#
#     def sleep(self):
#         self.satiety -= 1
#         print(self.name, 'сладко сопит')
#
#     def tear_wallpaper(self):
#         self.satiety -= 1
#         House.dirt += 5
#         print(self.name, 'дерет обои')
#
#     def satiety_info(self):
#         if self.satiety < 0:
#             print(self.name, 'умер от голода')
#
#     def __str__(self):
#         return '{}, сытость: {}'.format(self.name, self.satiety)
#
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         self.happynes = 100
#         self.satiety = 30
#
#     def pet_cat(self):
#         self.happynes += 5
#         print(self.name, 'тискает кота')
#
#     def eat(self):
#         if House.food > 30:
#             eat = random.randint(15, 30)
#             House.food -= eat
#             info.eaten_food += eat
#             self.satiety += 3
#             print(self.name, 'кушает')
#
#     def satiety_info(self):
#         if self.satiety < 0:
#             print(self.name, 'умер от голода на', day, 'день')
#             quit()
#
#     def dirt_info(self):
#         if House.dirt > 90:
#             self.happynes -= 10
#
#     def happines_info(self):
#         if self.happynes < 10:
#             print(self.name, 'умер от депрессии')
#
#     def __str__(self):
#         return '{}, сытость: {}, счастье: {}'.format(self.name, self.satiety, self.happynes)
#
#
# class Info:
#     count_coat = 0
#     eaten_food = 0
#     count_money = 0
#
#     def __str__(self):
#         return f'куплено шуб: {self.count_coat}, сьедено еды: {self.eaten_food}, заработано денег: {self.count_money}'
#
#
# class Husbend(Person):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def play(self):
#         self.satiety -= 1
#         self.happynes += 20
#         print(self.name, 'задротит весь день')
#
#     def work(self):
#         self.satiety -= 1
#         House.money += 150
#         info.count_money += 150
#         print(self.name,'пошел на работу')
#
#
# class Wife(Person):
#
#     def __init__(self, name):
#         super().__init__(name)
#         self.count_coat = 0
#
#     def buy_food(self):
#         if House.money > 60:
#             self.satiety -= 1
#             House.food += 50
#             House.cat_food += 10
#             House.money -= 60
#             print(self.name, 'купила продуктов')
#
#     def buy_coat(self):
#         if House.money > 350:
#             self.satiety -= 1
#             House.money -= 350
#             self.happynes += 60
#             info.count_coat += 1
#             print(self.name, 'купила очередную шубу')
#
#     def clean_house(self):
#         if House.dirt > 90:
#             self.satiety -= 1
#             House.dirt -= random.randint(50, 100)
#             print(self.name, 'прибралась дома')
#         print(self.name, 'нихуя не делает')
#
#
# info = Info()
# house = House()
# cat = Cat('Мурзик')
# husband = Husbend('Антон')
# wife = Wife('Карина')
#
# for day in range(365):
#     print('день',day)
#     cat_choise = random.randint(1, 3)
#     husband_choise = random.randint(1, 4)
#     wife_choise = random.randint(1, 5)
#     cat.eat() if cat_choise == 1 else cat.sleep() if cat_choise == 2 else cat.tear_wallpaper()
#     husband.eat() if husband_choise == 1 else husband.play() if husband_choise == 2 else husband.work() \
#         if husband_choise == 3 else husband.pet_cat()
#     wife.eat() if wife_choise == 1 else wife.buy_coat() if wife_choise == 2 else wife.buy_food() if wife_choise == 3 \
#         else wife.clean_house() if wife_choise == 4 else wife.pet_cat()
#     wife.dirt_info()
#     wife.satiety_info()
#     wife.happines_info()
#     husband.dirt_info()
#     husband.satiety_info()
#     husband.happines_info()
#     print()
#
# print(info)
