# class Toyota:
#     color = 'red'
#     prise = 1000000
#     max_speed = 200
#     corent_speed = 0
#
#
# import random
#
# car_1, car_2, car_3 = Toyota(),Toyota(),Toyota()
# car_1.corent_speed=random.randint(0,200)
# car_2.corent_speed=random.randint(0,200)
# car_3.corent_speed=random.randint(0,200)
#
# print(car_1.corent_speed,car_2.corent_speed,car_3.corent_speed)

# class Monitor:
#     monitor_name = ''
#     monitor_matrix = ''
#     monitor_res = ''
#     monitor_freq = 60
#
#     def print_info(self):
#         print(self.monitor_name, self.monitor_matrix, self.monitor_res, self.monitor_freq)
#
#
# class Headphones:
#     headphones_name = ''
#     headphones_sensitivity = 108
#     headphones_micro = False
#
#
# Monitor_1, Monitor_2, Monitor_3, Monitor_4 = Monitor(), Monitor(), Monitor(), Monitor()
# headphones_1, headphones_2, headphones_3 = Headphones(), Headphones(), Headphones()
#
# Monitor_1.monitor_name = 'Samsung'
# Monitor_1.monitor_matrix = 'VA'
# Monitor_1.monitor_res = 'WQHD'
#
# Monitor_1.print_info()
# Monitor_2.print_info()

# class Toyota:
#     color = ''
#     prise = 0
#     max_speed = 0
#     corent_speed = 0
#     def print_info(self):
#         print(self.corent_speed,self.max_speed,self.prise,self.color)
#
#     def corent_speed_set(self,speed):
#         print('установлена скорость {}'.format(speed))
#         self.corent_speed=speed
#
# import random
#
# car_1, car_2, car_3 = Toyota(),Toyota(),Toyota()
# car_1.print_info()
# car_1.corent_speed_set(200)
# car_1.print_info()

# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и
# «Наличие дома» и объекты которого могут выполнять следующие действия:
# 1.	Отобразить информацию о себе.
# 2.	Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# 3.	Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.
#
# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
#
# Family name: Common family
# Family funds: 100000
# Having a house: False
#
# Try to buy a house
# Not enough money!
#
# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0
#
# Family name: Common family
# Family funds: 0.0
# Having a house: True

# class Famili:
#     Famili_name = 'Karpov'
#     Famili_money = 100000
#     Having_a_house = False
#
#     def print_info(self):
#         print('Имя семьи {}\nКоличество денег {}\nНаличие дома {}\n'.format(self.Famili_name, self.Famili_money,
#                                                                             self.Having_a_house))
#
#     def earn_money(self, amount):
#         self.Famili_money += amount
#         print('Заработали {}\n'.format(amount))
#
#     def buy_house(self, price):
#         if price <= self.Famili_money:
#             self.Famili_money -= price
#             self.Having_a_house = True
#             print('дом куплен, денег осталось {}'.format(self.Famili_money))
#         else:
#             print('недостаточно денег')
#
#
# famili_1 = Famili()
# famili_1.print_info()
#
# famili_1.earn_money(500000)
# famili_1.print_info()
# famili_1.buy_house(100000)
# famili_1.print_info()

# class Toyota:
#
#     def __init__(self,color,price,max_speed,curent_speed):
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.curent_speed = curent_speed
#
#     def print_info(self):
#         print(self.curent_speed,self.max_speed,self.price,self.color)
#
#     def corent_speed_set(self,speed):
#         print('установлена скорость {}'.format(speed))
#         self.curent_speed=speed
#
#
# car_1=Toyota('red',10000,200,0)
# car_1.print_info()

# Задача 2. Координаты точки
# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         Point.count += 1
#         self.x = x
#         self.y = y
#
#     def info(self):
#         print(self.x, self.y)
#         print(Point.count,'точка(и)')
#
#
# one = Point()
# one.info()
# two=Point()
# three=Point()
# three.info()

# Задача 3. Весёлая ферма
# два класса: класс «Картошка» и класс «Грядка картошки».
# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о
# своей зрелости и расти. Всего у картошки может быть четыре стадии зрелости.
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать
# всю эту картошку, а также предоставлять информацию о зрелости всей картошки на своей территории.
#
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.
# Пример результата (проверка на зрелость и три взращивания):
# Картошка ещё не созрела!
# Картошка прорастает!
# Картошка 1 сейчас Росток
# Картошка 2 сейчас Росток
# Картошка 3 сейчас Росток
# Картошка 4 сейчас Росток
# Картошка 5 сейчас Росток
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Зелёная
# ;;;;;;
# Картошка ещё не созрела!
#
# Картошка прорастает!
# Картошка 1 сейчас Зрелая
# Картошка 2 сейчас Зрелая
# Картошка 3 сейчас Зрелая
# Картошка 4 сейчас Зрелая
# Картошка 5 сейчас Зрелая
# Вся картошка созрела. Можно собирать!

# from garden import PotatoGarden
#
# potato=PotatoGarden(5)
# potato.info()
# potato.grow_all()
# potato.info()
# potato.grow_all()
# potato.info()
# Задача 1. Драка
# Вы работаете в команде разработчиков мобильной игры, и вам досталась вот такая часть от ТЗ заказчика:
# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
# Реализуйте такую программу.

# class Warrior:
#     count=1
#
#     def __init__(self, helth=100):
#         self.helth = helth
#         self.index = Warrior.count
#         Warrior.count += 1
#
#     def atack(self,another_warrior):
#         another_warrior.helth-=20
#         print(self.index,'войн ударяет',another_warrior.index)
#
#     def info(self):
#         print('здоровье',self.index,'война',self.helth)
#
#
# one=Warrior()
# two=Warrior()
# one.info()
# two.info()
# one.atack(two)
# two.info()
#
# Задача 2. Студенты
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов и отсортируйте его по возрастанию среднего балла.
# Выведите результат на экран.
# spisok = []
#
#
# class Student:
#
#     def __init__(self, Name, Num, *Rates):
#         self.name = Name
#         self.num = Num
#         self.rates = Rates
#         self.avarege = Rates
#         spisok.append(self)
#
#     def info(self):
#         print('имя:', self.name, '\nсредний балл:', self.give_average())
#
#     def give_average(self):
#         return sum(self.avarege) / 5
#
#
# Dima = Student('Dima', 18, 1, 2, 3, 43, 5)
# Vita = Student('Vita', 18, 1, 3, 4, 4, 5)
# Kata = Student('Kata', 23, 4, 3, 4, 11, 5)
# Polina = Student('Polina', 23, 4, 1, 4, 5, 5)
#
# # Student.info()
#
# for student in spisok:
#     print(student.info())
#
#
# spisok.sort(key=lambda x: x.give_average())
# print('\nСписок студентов отсортированный:')
# for student in spisok:
#     print(student.info())

# Задача 3. Окружность
# На координатной плоскости рисуются окружности, у каждой окружности следующие параметры:
# координаты X и Y центра окружности и значение R ― это радиус окружности.
# По умолчанию центр находится в (0, 0), а радиус равен 1.
#
# Реализуйте класс «Окружность», который инициализируется по этим параметрам. Круг также может:
# 1.	Находить и возвращать свою площадь.
# 2.	Находить и возвращать свой периметр.
# 3.	Увеличиваться в K раз.
# 4.	Определять, пересекается ли он с другой окружностью.
# import math
#
#
# class Circle:
#
#     def __init__(self, x=0, y=0, R=1):
#         self.x = x
#         self.y = y
#         self.R = R
#
#     def S(self):
#         return math.pi * self.R ** self.R
#
#     def P(self):
#         return 2 * math.pi * self.R
#
#     def increase(self, K):
#         self.R *= K
#
#     def info(self):
#         print('y =', self.y, '\nx =', self.x)
#
#     def cross(self, another_circle):
#         # Две окружности пересекаются тогда и только тогда когда расстояние между их центрами равно сумме
#         # и разности их радиусов
#         return (self.x - another_circle.x) ** 2 + (self.y - another_circle.y) ** 2 <= (self.R + another_circle.R) ** 2
#
#
# circle_1 = Circle(2,2,2)
# circle_2 = Circle(3,3,3)
# # circle_1.info()
# # print(circle_1.P())
# # print(circle_1.S())
# # circle_1.increase(3)
# print(circle_1.cross(circle_2))

# Задача 4. Отцы, матери и дети
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# 1.	Имя.
# 2.	Возраст.
# 3.	Список детей.
# И он может:
# 1.	Сообщить информацию о себе.
# 2.	Успокоить ребёнка.
# 3.	Покормить ребёнка.
#
# У ребёнка есть:
# 1.	Имя.
# 2.	Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# 3.	Состояние спокойствия.
# 4.	Состояние голода.
# Реализация состояний на ваше усмотрение! Это может быть и простой «флаг», и словарь состояний

# class Parent():
#
#     def __init__(self, name, age, *cildren):
#         self.name = name
#         self.age = age
#         self.cildren = cildren
#
#     def info(self):
#         print('Имя:', self.name, '\nВозраст:', self.age, '\nДети: ', end='')
#         for cild in range(len(self.cildren)):
#             print(self.cildren[cild].name, end=' ')
#
#     def calm_child(self, child):
#         child.stage_calm = 'спокойный'
#         print('успокаивает', child.name)
#
#     def feed_child(self, child):
#         child.stage_hungry = 'сытый'
#         print('кормит', child.name)
#
#
# class Child():
#
#     def __init__(self, name, age, stage_calm='не спокойный', stage_hungry='голодный'):
#         self.name = name
#         self.age = age
#         self.stage_calm = stage_calm
#         self.stage_hungry = stage_hungry
#
#     def info(self):
#         print('\nИмя:', self.name, '\nВозраст:', self.age, '\nCпокойствие:', self.stage_calm, '\nПотребность:',
#               self.stage_hungry)
#
#
# dima = Child('Дима', 24)
# bogdan = Child('Богдан', 10)
# mama = Parent('Таня', 45, dima, bogdan)
#
# mama.info()
# # bogdan.info()
# dima.info()
# mama.feed_child(dima)
# mama.calm_child(dima)
# dima.info()

# Задача 5. Весёлая ферма 2
# class PotatoGarden:
#
#     def __init__(self, count):
#         print('садим картошку')
#         self.potatos = [Potato(index) for index in range(1, count + 1)]
#
#     def info(self):
#         for potato in self.potatos:
#             print('Картошка', potato.index, 'сейчас', potato.get_info())
#         if not self.potatos:
#             print('картошки нет')
#
#     def grow_all(self):
#         for potato in self.potatos:
#             potato.grow()
#         print('Картошка прорастает!')
#
#
# class Potato:
#     stages = {0: 'не созрела', 1: 'зреет', 2: 'созрела'}
#
#     def __init__(self, index):
#         self.index = index
#         self.stage = 0
#
#     def get_info(self, index=0):
#         return self.stages[self.stage]
#
#     def grow(self):
#         self.stage += 1
#         if self.stage == 3:
#             print('картошка созрела')
#
#
# class Gardener:
#
#     def __init__(self,name,someGarden):
#         self.name=name
#         self.garden=someGarden
#
#     def care_garden(self):
#         print('Садовник ухаживает за грядкой')
#
#     def gather(self,someGarden):
#         someGarden.potatos.clear()
#         print('Садовник собирает картошку')
#
#
# p = PotatoGarden(3)
# p.info()
# p.grow_all()
# p.grow_all()
# p.info()
# s=Gardener('Vitya',p)
# s.care_garden()
# s.gather(p)
# p.info()
# Задача 6. Магия
# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые:
# «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
#
# Вот таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
#
# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
# Если результат не определён, то возвращается None.


# class Water:
#     title = 'вода'
#
#     def __add__(self, other):
#         if isinstance(other,Air):
#             return Storm()
#         if isinstance(other,Fire):
#             return Stream()
#         if isinstance(other,Earth):
#             return Dirt()
#
#
# class Air:
#     title = 'воздух'
#
#     def __add__(self, other):
#         if isinstance(other,Water):
#             return Storm()
#         if isinstance(other, Fire):
#             return Ligth()
#         if isinstance(other,Earth):
#             return Ach()
#
# class  Fire:
#     title='огонь'
#
#     def __add__(self, other):
#         if isinstance(other,Stream):
#             return Storm()
#         if isinstance(other, Air):
#             return Ligth()
#         if isinstance(other,Earth):
#             return Lava()
#
# class Earth:
#     title='земля'
#
#     def __add__(self, other):
#         if isinstance(other,Water):
#             return Dirt()
#         if isinstance(other, Air):
#             return Ach()
#         if isinstance(other,Fire):
#             return Lava()
#
# class Storm:
#      title='шторм'
#      def __str__(self):
#         return Storm.title
#
#
# class Stream:
#     title = 'пар'
#
# class Lava:
#     title = 'лава'
#
# class Ach:
#     title = 'пепел'
#
# class Dirt:
#     title = 'грязь'
#
# class Ligth:
#     title = 'молния'
#
# w = Water()
# a = Air()
# # s=a+w
# print(f'смешиваем {a.title} c {w.title} и получаем {a+w}')

# Задача 7. Совместное проживание
# Человек может:
# 1.	Есть (+ сытость, − еда).
# 2.	Работать (− сытость, + деньги).
# 3.	Играть (− сытость).
# 4.	Ходить в магазин за едой (+ еда, − деньги).
# import random
#
# class House:
#     food = 50
#     money = 50
#
#     def info(self):
#         print(self.food,self.money)
#
# class Person:
#
#     def __init__(self, name, satiety=50):
#         self.name = name
#         self.satiety = satiety
#
#     def eat(self):
#         House.food -= 1
#         self.satiety += 1
#         print('кушает')
#
#     def work(self):
#         House.money += 1
#         self.satiety -= 1
#         print('работает')
#
#     def play(self):
#         self.satiety -= 1
#         print('играет')
#
#     def buy_food(self):
#         House.food += 1
#         House.money -= 1
#         print('купил продуктов')
#
#     def info(self):
#         print('\nинформация о',self.name)
#         print('сытость:',self.satiety,'\nденьги:',House.money,'\nзапас еды:',House.food)
#
#
# artem = Person('Артем')
# # anton=Person('Антон')
#
#
# for day in range(365):
#     choise = random.randint(1, 6)
#     print('день', day)
#     if artem.satiety < 0:
#         print(artem.name, 'умер от голода')
#     if artem.satiety < 20:
#         artem.eat()
#         # anton.eat()
#     elif House.food < 10:
#         artem.buy_food()
#         # anton.buy_food()
#     elif House.money < 50:
#         artem.work()
#         # anton.work()
#     elif choise == 1:
#         artem.work()
#         # anton.work()
#     elif choise == 2:
#         artem.eat()
#         # anton.eat()
#
# artem.info()
# anton.info()

# Задача 8. Блек-джек

# import random
#
#
# class Computer:
#     name = 'компьютер'
#     hand = []
#     points = 0
#
#     def take_card(self):
#         choise = random.randint(2, 14)
#         self.hand.append(Player.cards[choise][0])
#         self.points += Player.cards[choise][1]
#
#     def info(self):
#         print('имя:', self.name, '\nкарты:', *self.hand)
#         print('очки', self.points, '\n')
#
#
# class Player():
#     cards = {2: ['двойка', 2], 3: ['тройка', 3], 4: ['четверка', 4], 5: ['пятерка', 5],
#              6: ['шестерка', 6], 7: ['семерка', 7], 8: ['восьмерка', 8], 9: ['девятка', 9],
#              10: ['десятка', 10], 11: ['туз', 11], 12: ['король', 10], 13: ['дама', 10], 14: ['валет', 10]}
#
#     def __init__(self, name=input('Введите имя игрока: ')):
#         self.name = name
#         self.hand = []
#         self.points = 0
#
#     def info(self):
#         print('имя:', self.name, '\nкарты:', *self.hand)
#         print('очки', self.points, '\n')
#
#     def take_card(self):
#         choise = random.randint(2, 14)
#         self.hand.append(Player.cards[choise][0])
#         self.points += Player.cards[choise][1]
#
#
# person = Player()
# computer = Computer()
# for _ in range(2):
#     computer.take_card()
#     person.take_card()
#
# while True:
#     choise = input('взять карту или остановиться?\n1-взять,2-остановиться ')
#     if choise == '1':
#         person.take_card()
#         # computer.take_card()
#     if choise == '2':
#         break
#
# if person.points > 21:
#     print(person.name, 'сгорает')
# if computer.points > 21:
#     print(computer.name, 'сгорает')
#
# person.info()
# computer.info()
#
# if person.points > computer.points:
#     print('выиграл', person.name)
# else:
#     print('выиграл', computer.name)
#
# if person.points == computer.points:
#     print('ничья')

