# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

point_triangle = sd.get_point(300, 300)
point_square = sd.get_point(50, 50)
point_pentagon = sd.get_point(30, 300)
point_hexagon = sd.get_point(250, 30)


def triangle(point, angle):
    for i in range(3):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
        v.draw(color=color)
        point = v.end_point
        angle = angle + 120


def square(point, angle):
    for i in range(4):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
        v.draw(color=color)
        point = v.end_point
        angle = angle + 90


def pentagon(point, angle):
    for i in range(5):
        v = sd.get_vector(start_point=point, angle=angle, length=110, width=3)
        v.draw(color=color)
        point = v.end_point
        angle = angle + 72


def hexagon(point, angle):
    for i in range(6):
        v = sd.get_vector(start_point=point, angle=angle, length=110, width=3)
        v.draw(color=color)
        point = v.end_point
        angle = angle + 60


colors = {
    '1': ['Красный', sd.COLOR_RED],
    '2': ['Оранжевый', sd.COLOR_ORANGE],
    '3': ['Желтый', sd.COLOR_YELLOW],
    '4': ['Зеленый', sd.COLOR_GREEN],
    '5': ['Сине-зеленый', sd.COLOR_CYAN],
    '6': ['Синий', sd.COLOR_BLUE],
    '7': ['Фиолетовый', sd.COLOR_PURPLE]
}


for key in colors:
    print(key, colors[key][0])

number = (input("Введите желаемое число> "))

if number in colors:
    color = colors[number][1]
    triangle(point=point_triangle, angle=5)
    square(point=point_square, angle=5)
    pentagon(point=point_pentagon, angle=0)
    hexagon(point=point_hexagon, angle=0)
else:
    print('НЕВЕРНО')
    print('Фигуры находятся только под числами от 1 до 7. Введите номер цвета от 1 до 7')


sd.pause()

# Зачёт!
