# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


point = sd.get_point(10, 10)

top_point = sd.get_point(100, 50)
bottom_point = sd.get_point(0, 0)


for i, y in enumerate(range(0, sd.resolution[0], point.y)):
    if i % 2 == 0:
        top_point.x = 150
        bottom_point.x = 50
    else:
        top_point.x = 100
        bottom_point.x = 0

    for x in enumerate(range(0, sd.resolution[0], point.x)):
        sd.rectangle(left_bottom=bottom_point, right_top=top_point, color=sd.COLOR_GREEN, width=1)
        top_point.x += 100

    top_point.y += 50
    bottom_point.y += 50


# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()

# Зачёт!
