# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

point_triangle = sd.get_point(300, 300)
point_square = sd.get_point(50, 50)
point_pentagon = sd.get_point(30, 300)
point_hexagon = sd.get_point(250, 30)


#  Функция рисования многоугольника должна принимать 4 аргумента:
#  - точка: один объект sd.Point
#  - угол поворота фигуры: число
#  - длину стороны: число
#  - количество сторон: целое число.
#  Передавать списки точек и углов в эту функцию неправильно.
#  Обновлённые версии функций рисовния фигур должны принимать три аргумента и вызывать внутри себя общую функцию
#  и передать в неё три входных аргумента и количество сторон. Для треугольника три, для квадрата четыре, и т. д.
#  В итоге должно получиться 4 функции.
#  Название функции function лучше заменить на что-то отражающее её суть, например polygon или draw_figure.

def polygon(point, angle, length, sides):
    side = int(360 / sides)
    now_point = point
    now_length = length
    for m in range(0, 360, side):
        angle += m
        v = sd.get_vector(start_point=now_point, angle=m, length=now_length, width=3)
        v.draw()
        now_point = v.end_point
    sd.line(start_point=now_point, end_point=now_point, width=3)


#  3 Сейчас в функциях рисования фигур переменные, передаваемые в point_triangle используются неявно.
#  Т. е. ри работе функции мы надеемся, что где-то в области нашей видимости существует переменная
#  с нужным названием. При этом при изменении программы может возникнуть ситуация, что одна и та же переменная
#  используется в нескольких местах. При редактировании одной части кода может возникнуть ситуация,
#  что переменная изменится или будет удалена в одной части программы, а ошибка возникнет в другой.
#  Явная передача объевтов в функцию через аргументы снижает вероятность подобных проблем.


def triangle(point, angle, length):
    point = point
    angle = angle
    length = length
    polygon(point=point, angle=angle, length=length, sides=3)


def square(point, angle, length):
    point = point
    angle = angle
    length = length
    polygon(point=point, angle=angle, length=length, sides=4)


def pentagon(point, angle, length):
    point = point
    angle = angle
    length = length
    polygon(point=point, angle=angle, length=length, sides=5)


def hexagon(point, angle, length):
    point = point
    angle = angle
    length = length
    polygon(point=point, angle=angle, length=length, sides=6)


triangle(point=point_triangle, angle=0, length=100)
square(point=point_square, angle=0, length=100)
pentagon(point=point_pentagon, angle=0, length=100)
hexagon(point=point_hexagon, angle=0, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.

#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# Зачёт!
