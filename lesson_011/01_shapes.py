# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    side = int(360 / n)

    def polygon(point, angle, length):
        now_point = point
        now_length = length
        for m in range(0, 360, side):
            angle += m
            v = sd.get_vector(start_point=now_point, angle=m, length=now_length, width=3)
            v.draw()
            now_point = v.end_point
        sd.line(start_point=now_point, end_point=now_point, width=3)

    return polygon


draw_triangle = get_polygon(n=3)
draw_square = get_polygon(n=4)
draw_pentagon = get_polygon(n=5)
draw_hexagon = get_polygon(n=6)
draw_triangle(point=sd.get_point(300, 300), angle=13, length=100)
draw_square(point=sd.get_point(50, 50), angle=13, length=100)
draw_pentagon(point=sd.get_point(30, 300), angle=13, length=100)
draw_hexagon(point=sd.get_point(250, 30), angle=13, length=100)

sd.pause()

# Зачёт!
