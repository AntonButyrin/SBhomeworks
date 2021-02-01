# -*- coding: utf-8 -
import my_burger


# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger


def cheeseburger():
    print("Делаем бургер:")
    my_burger.bun()
    my_burger.ketcup()
    my_burger.mustard()
    my_burger.onion()
    my_burger.cucumber()
    my_burger.cucumber()
    my_burger.cheese()
    my_burger.cutlet()
    my_burger.cutlet()
    my_burger.cheese()
    my_burger.bun()
    print("Сделали двойной Чизбургер с картинки")


cheeseburger()

print("-------------------")


def burger():
    print("Делаем бургер от шеф-повара:")
    my_burger.bun()
    my_burger.cheese()
    my_burger.ketcup()
    my_burger.cucumber()
    my_burger.tomato()
    my_burger.sauce()
    my_burger.mustard()
    my_burger.cutlet()
    my_burger.bun()
    print("Сделали свой бургер")


burger()

# Зачёт!
