# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


x_list = []

for m in range(0, 500, 30):
    random_number = sd.random_number(200, 1000)
    x_list.append(random_number)

y_list = []

for n in range(0, 500):
    random_number = sd.random_number(0, 1000)
    y_list.append(random_number)


def snowflake():
    while True:
        sd.start_drawing()
        for i, (x, y) in enumerate(zip(x_list, y_list)):
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=50, color=sd.background_color)
            if y > 0:
                y -= 10
                x -= 10
            else:
                x = sd.random_number(500, 1000)
                y = sd.random_number(500, 1000)
            y_list[i] = y
            x_list[i] = x
            point_2 = sd.get_point(x, y)
            sd.snowflake(center=point_2, length=50, color=sd.COLOR_WHITE)
        if sd.user_want_exit():
            break
        sd.finish_drawing()
        sd.sleep(0.1)


snowflake()

sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# Зачёт!
