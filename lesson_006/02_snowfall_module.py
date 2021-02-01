# -*- coding: utf-8 -*-

import simple_draw as sd

from lesson_006.snowfall import create_snowflake, painting_snowflake, delete_snowflake, list_fall, shift

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

create_snowflake(counter=20)
while True:
    sd.start_drawing()
    painting_snowflake(color=sd.background_color)
    shift()
    painting_snowflake(color=sd.COLOR_WHITE)
    number = list_fall()
    if number:
        delete_snowflake(index_list=number)
        create_snowflake(counter=len(number))
    sd.finish_drawing()
    if sd.user_want_exit():
        break
sd.pause()

# Зачёт!
