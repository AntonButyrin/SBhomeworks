# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

point_start = sd.get_point(300, 300)


def triangle(point, angle):
    for z in range(3):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
        v.draw()
        point = v.end_point
        angle = angle + 120


def square(point, angle):
    for z in range(4):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
        v.draw()
        point = v.end_point
        angle = angle + 90


def pentagon(point, angle):
    for z in range(5):
        v = sd.get_vector(start_point=point, angle=angle, length=110, width=3)
        v.draw()
        point = v.end_point
        angle = angle + 72


def hexagon(point, angle):
    for z in range(6):
        v = sd.get_vector(start_point=point, angle=angle, length=110, width=3)
        v.draw()
        point = v.end_point
        angle = angle + 60


patterns = {
    '1': ['Треугольник', triangle, 5],
    '2': ['Квадрат', square, 5],
    '3': ['Пятиугольник', pentagon, 0],
    '4': ['Шестиугольник', hexagon, 0]
}

for i in patterns:
    print(i, patterns[i][0])

key = input("Введите желаемое число> ")

if key in patterns:
    draw_function = patterns[key][1]
    draw_function(point=point_start, angle=patterns[key][2])

sd.pause()

# Зачёт!
