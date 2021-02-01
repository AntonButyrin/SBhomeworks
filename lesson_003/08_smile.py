# -*- coding: utf-8 -*-
# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
color = sd.COLOR_DARK_RED
radius = 100
radius_eyes = 6


def smile(x, y, color):
    sd.circle(center_position=point, radius=radius, color=color, width=1)
    point.x += 30
    point.y += 30
    r_eyes_z = sd.get_point(point.x, point.y)

    sd.circle(center_position=r_eyes_z, radius=radius_eyes, color=color, width=1)
    point.x -= 60
    point.y += 0
    l_eyes_z = sd.get_point(point.x, point.y)

    sd.circle(center_position=l_eyes_z, radius=radius_eyes, color=color, width=1)
    point.x -= 0
    point.y -= 60
    l_month_z = sd.get_point(point.x, point.y)

    point.x += 60
    point.y += 0
    r_month_z = sd.get_point(point.x, point.y)
    sd.line(start_point=l_month_z, end_point=r_month_z, color=color, width=4)



for _ in range(10):
    point = sd.random_point()
    smile(x=point.x, y=point.y, color=color)

sd.pause()

# Зачёт!
