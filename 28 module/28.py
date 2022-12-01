# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих:
# разведывательного дрона и военного робота.
# Разведывательный дрон просто летает в поиске противника. При команде operate он выводит
# сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение
# о защите военного объекта с воздуха с помощью этого оружия.
# Напишите программу, которая реализует все необходимые классы роботов. Сущности
# «Робот» и «Может летать» должны быть вынесены в отдельные классы. Обычный робот
# имеет модель и может вывести сообщение «Я — Робот». Объект, который умеет летать,
# дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать, летать и приземляться.


# class Robot:
#
#     def __init__(self, model):
#         self.model = model
#
#     def info(self):
#         print('я робот')
#
#
# class Fly:
#     high = 0
#     speed = 0
#
#     def fly(self):
#         print('летит вперед')
#
#     def land(self):
#         if self.high > 0:
#             print('приземляется')
#             self.high = 0
#         else:
#             print('робот уже приземлился')
#
#     def take_off(self):
#         if self.high == 0:
#             print('робот взлетает')
#             self.high += 1
#         else:
#             print('робот уже взлетел')
#
#
# class SearchRobot(Robot, Fly):
#
#     def __init__(self, model):
#         super().__init__(model)
#
#     def operate(self):
#         self.fly()
#         print('Веду разведку с воздуха')
#
#
# class WarRobot(Robot, Fly):
#
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def operate(self):
#         print(f'защита военного объекта с воздуха с помощью {self.gun}')
#
#
# robot = Robot('обычный робот')
# searchrobot = SearchRobot('развед робот')
# warrobot = WarRobot('военный робот', 'пушка')
#
# robot.info()
# searchrobot.fly()
# searchrobot.take_off()
# searchrobot.land()
#
# warrobot.land()
# warrobot.operate()

# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
#     @abstractmethod
#     def move(self):
#         print(self.__class__.__name__)
#         print('двигается')
#
#     @abstractmethod
#     def gorn(self):
#         print(self.__class__.__name__)
#         print('сигналит')


# class Auto(Transport):
#
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         super().move()
#
#     def gorn(self):
#         super().gorn()
#
#
# class Boat(Transport):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         super().move()
#
#     def gorn(self):
#         super().gorn()
#
#
# class Play_music_Mixin:
#
#     def play(self):
#         print('слушаем музычку')
#
#
# class Amfibia(Transport, Play_music_Mixin):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         super().move()
#
#     def gorn(self):
#         super().gorn()
#
#
# b = Amfibia('r', 100)
# b.move()
# b.play()

# Задача 1. Работа с файлом
# Реализуйте класс File — контекстный менеджер для работы с файлами.
# Он должен принимать на вход имя файла и режим чтения/записи и открывать сам файл.
# В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.
#
# Пример основного кода:
# with File(‘example.txt’, ‘w’) as file:
#     file.write(‘Всем привет!’)

# class File:
#
#     def __init__(self, name, mode):
#         print('инициализируется контекстный менеджер и создается файл')
#         self.name = name
#         self.mode = mode
#         self.file=open(self.name,self.mode)
#
#     def __enter__(self):
#         print('вызывается ентер и возвращает файл')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('вызыввется екзит')
#         return self.file.close()
#
#
# with File('example.txt', 'w') as file:
#     file.write('всем привет')


# class Example:
#
#     def __init__(self):
#         print('вызов __init__')
#
#     def __enter__(self):
#         print('вызов __enter__')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('вызов __exit__')
#         print('тип ошибки:',exc_type)
#         print('значение ошибки:',exc_val)
#         print('"След" ошибки:',exc_tb)
#         return True
#
# my_obj = Example()
# with my_obj as obj:
#     print('Код внутри первого вызова контекст менеджера')
#     with my_obj as obj2:
#         raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
#
#     print('Я обязательно выведусь...')

# Вызов __init__
# Вызов __enter__
# Код внутри первого вызова контекст менеджера
# Вызов __enter__
# Вызов __exit__
# Тип ошибки: <class 'Exception'>
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
# "След" ошибки: <traceback object at 0x00000234E54CE4C0>
# Вызов __exit__
# Тип ошибки: <class 'Exception'>
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
# "След" ошибки: <traceback object at 0x00000234E54CE4C0>
# . . . . (тут сама ошибка красным цветом) . . . .
#
# Исходя их этих входных данных, реализуйте класс «Контекст-менеджер», который будет выдавать такой же результат.

# Задача 1. Транспорт 2
# Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс геттерами и сеттерами
# для соответствующих атрибутов. Используйте встроенные декораторы. Вот входные данные той задачи:
#
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться
# и подавать сигнал. В парке транспорта стоят:
# •	Автомобили. Они могут ездить только по земле.
# •	Лодки. Ездят только по воде.
# •	Амфибии. Могут перемещаться и по земле, и по воде.

# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#
#     def __init__(self, color, speed):
#         self._color = color
#         self._speed = speed
#
#     @abstractmethod
#     def move(self):
#         print(self.__class__.__name__)
#         print('двигается')
#
#     @abstractmethod
#     def gorn(self):
#         print(self.__class__.__name__)
#         print('сигналит')
#
#     @property
#     def color(self):
#         return self._color
#
#     @color.setter
#     def color(self, color):
#         self._color = color
#
#     @property
#     def speed(self):
#         return self._speed
#
#     @speed.setter
#     def speed(self, speed):
#         self._speed = speed
#
#
# class Auto(Transport):
#
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         super().move()
#
#     def gorn(self):
#         super().gorn()
#
#
# class Boat(Transport):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         super().move()
#
#     def gorn(self):
#         super().gorn()
#
#
# class Play_music_Mixin:
#
#     @classmethod
#     def non(cls):
#         print('я хуй')
#
#     def play(self):
#         print('слушаем музычку')
#
#
# class Amfibia(Transport, Play_music_Mixin):
#     def __init__(self, color, speed):
#         super().__init__(color, speed)
#
#     def move(self):
#         super().move()
#
#     def gorn(self):
#         super().gorn()
#
#
# amf = Amfibia('red', 0)
# print(amf.speed)
# amf.speed=100
# print(amf.speed)
#
# print(amf.color)
# amf.color='green'
# print(amf.color)

# Задача 1. Работа с файлом 2
# Реализуйте модернизированную версию контекст-менеджера File — теперь при попытке открыть
# несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи.
# На выходе из менеджера подавляются все исключения, связанные с файлами.
# import os
#
#
# class File:
#     def __init__(self, filename: str, mode: str) -> None:
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         if os.path.isfile(self.filename):
#             self.file = open(self.filename, self.mode)
#         else:
#             self.file = open(self.filename, 'w+')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         self.file.close()
#         # if exc_type is TypeError:
#         return True
#
#
# with File('example.txt', 'a+') as file:
#     file.write('Всем привет!')

# Задача 2. Математический модуль

# Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):
# •	нахождение длины окружности,
# •	площадь окружности,
# •	объём куба,
# •	площадь поверхности сферы.

# import math
# from abc import ABC
#
#
# class MyMath(ABC):
#     """Абстрактный класс MyMath"""
#
#     @classmethod
#     def circle_len(cls, radius: int) -> float:
#         return 2 * math.pi * radius
#
#     @classmethod
#     def circle_sq(cls, radius: int) -> float:
#         return math.pi * radius ** 2
#
#     @classmethod
#     def cube_value(cls, edge: int) -> float:
#         return edge ** 3
#
#     @classmethod
#     def sphere_area(cls, radius: int) -> float:
#         return 4 * math.pi * radius ** 2
#
# res_1 = MyMath.circle_len(radius=5)
# res_2 = MyMath.circle_sq(radius=6)
# print(res_1)
# print(res_2)

# Задача 3. Моделирование
# В проекте по 3D-моделированию используются две фигуры — куб и пирамида.
# Для моделирования этих фигур используются соответствующие 2D-фигуры, а именно квадрат и треугольник.
# Вся поверхность 3D-фигуры может храниться в виде списка, например: для куба это будет
# [Square, Square, Square, Square, Square, Square].
# Квадрат инициализируется длинами сторон, а треугольник — основанием и высотой.
# Каждая из 2D-фигур умеет находить свои периметр и площадь, а 3D-фигуры, в свою очередь,
# могут находить площадь своей поверхности.
#
# Используя входные данные о фигурах и знания математики, реализуйте соответствующие классы и методы.
# Для базовых классов также реализуйте геттеры и сеттеры.
# import math
# from abc import ABC
#
#
# class Figure(ABC):
#     figure_name = 'Фигура'
#
#     def __init__(self, figure_name):
#         self.figure_name = figure_name
#
#     def show_name(self):
#         print(self.figure_name)
#
#
# class Square(Figure):
#
#     def __init__(self, a):
#         self.figure_name = 'квадрат'
#         self._a = a
#
#     @property
#     def a(self):
#         return self._a
#
#     @a.setter
#     def a(self, a):
#         self.a = a
#
#     def P(self):
#         return 4 * self._a
#
#     def S(self):
#         return self._a * self._a
#
#
# class Triangle(Figure):
#
#     def __init__(self, b, h):
#         self.figure_name = 'треугольник'
#         self._h = h
#         self._b = b
#
#     @property
#     def h(self):
#         return self.h
#
#     @h.setter
#     def h(self, h):
#         self._h = h
#
#     @property
#     def b(self):
#         return self._b
#
#     @b.setter
#     def b(self, b):
#         self._b = b
#
#     def S(self):
#         return 0.5 * self._b * self._h
#
#     def P(self):
#         return 2 * math.sqrt(self._h ** 2 + (self._b / 2) ** 2) + self._b
#
#
# class Cube(Square):
#     def __init__(self, a):
#         super().__init__(a)
#         self.figure_name = 'Куб'
#
#     @property
#     def square(self):
#         return 6 * super().S()
#
#     @property
#     def perimeter(self):
#         return 3 * super().P()
#
# class Pyramid(Triangle):
#     def __init__(self, b,h):
#         super().__init__(b,h)
#         self.figure_name = 'Пирамида'
#
#     @property
#     def square(self):
#         side_square = 4 * super().S()
#         base_square = self._b ** 2
#         return side_square + base_square
#
#     @property
#     def perimeter(self):
#         return 2 * super().P() + 2 * self._b
#
#
# p = Pyramid(6, 4)
# print(p.square)
# print(p.perimeter)
#
# p = Cube(5)
# print(p.square)
# print(p.perimeter)
#
# class Date:
#     def __init__(self, day: int = 0, month=0, year: int = 0) -> None:
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self) -> str:
#         return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'
#
#     @classmethod
#     def _split_date(cls, date: str) -> None:
#         dmy_list = []
#         if '-' in date:
#             dmy_list = date.split('-')
#         elif '/' in date:
#             dmy_list = date.split('/')
#         elif '.' in date:
#             dmy_list = date.split('.')
#         if len(dmy_list) != 3:
#             cls.day = None
#             cls.month = None
#             cls.year = None
#         else:
#             cls.day, cls.month, cls.year = map(int, dmy_list)
#
#     @classmethod
#     def is_date_valid(cls, date: str) -> bool:
#         cls._split_date(date)
#         return 0 < cls.day <= 31 and 0 < cls.month <= 12 and 0 < cls.year <= 9999
#
#     @classmethod
#     def from_string(cls, date: str) -> 'Date':
#         cls._split_date(date)
#         date_obj = cls(cls.day, cls.month, cls.year)
#         return date_obj
#
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-12-2077'))
# print(Date.is_date_valid('40-12-2077'))