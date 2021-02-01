# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
color = {
    1 : sd.COLOR_DARK_CYAN,
    2 : sd.COLOR_GREEN
}


def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
    sd.circle(center_position=point, color=color[2], width=1)


point = sd.get_point(300, 300)
bubble(point=point, step=5, color=color[2])

# Нарисовать 10 пузырьков в ряд

for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5, color=color[2])

# Нарисовать три ряда по 10 пузырьков

for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5, color=color[2])

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5, color=color[2])

sd.pause()

# Зачёт!
