# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

root_point = sd.get_point(300, 30)

def branch(point, angle, length,delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    next_angle_right = angle - 30
    next_length_right = length * 0.75
    next_point_right =v1.end_point
    branch(point=next_point_right,angle=next_angle_right,length=next_length_right, delta=delta)

    v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v2.draw()

    next_length_left = length * 0.75
    next_angle_left = angle + 30
    next_point_left = v1.end_point
    branch(point=next_point_left, angle=next_angle_left, length=next_length_left, delta=delta)


for delta in range(0, 51, 10):
    branch(point=root_point, angle=60, length=100, delta=delta)
for delta in range(-50, 1, 10):
    branch(point=root_point, angle=120, length=100, delta=delta)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()

# Зачёт!
