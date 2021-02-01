# -*- coding: utf-8 -*-
import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
#
#
# class Snowflake:
#
#     def __init__(self):
#         self.sd = sd
#         self.x = sd.random_number(200, 1000)
#         self.y = sd.random_number(800, 1000)
#
#
#     def clear_previous_picture(self):
#         return self.sd.clear_screen()
#
#     def move(self):
#         if self.y > 0:
#             self.y -= 10
#             self.x -= 10
#
#     def draw(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, length=100, color=sd.COLOR_WHITE)
#
#     def can_fall(self):
#         return self.y > 0
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.01)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


use_list = []
list_down = []
index_list = []


def delete_snowflake():
    return index_list.clear()


def get_fallen_flakes():
    for i in enumerate(use_list):
        if not flake.can_fall():
            list_down.append(i)
            index_list.append(list_down.index(i))
    return len(index_list)


class Snowflake:

    def __init__(self, counter):
        self.counter = counter
        self.sd = sd
        self.x = sd.random_number(200, 1000)
        self.y = sd.random_number(800, 1000)

    def create_snowflake(self):
        p = 0
        while p <= self.counter:
            use_list.append(Snowflake(counter=20))
            p += 1

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=50, color=sd.background_color)

    def move(self):
        if self.y > 0:
            self.y -= 10
            self.x -= 5

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=50, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y > 0


flake = Snowflake(counter=20)
flake.create_snowflake()
flakes = use_list
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    get_fallen_flakes()
    if get_fallen_flakes():
        delete_snowflake()
        flake = Snowflake(counter=get_fallen_flakes())
        flake.create_snowflake()  # добавить еще сверху
    sd.sleep(0.001)
    if sd.user_want_exit():
        break
sd.pause()

# Зачёт!
