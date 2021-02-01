# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self):
        self.name = "Антон"
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def clear_dirt(self):
        self.house.dirt -= 5
        self.fullness -= 10

    def buy_cat_eat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='blue')

    def take_the_cat(self, meow):
        self.cat = meow
        cprint('{} взял кота'.format(self.name), color='cyan')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, home):
        self.house = home
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 20:
            self.buy_cat_eat()
        elif self.house.dirt > 0:
            self.clear_dirt()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class Cat:

    def __init__(self):
        self.name = "Люцифер"
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def go_to_the_house(self, home):
        self.house = home
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        cprint('{} пошел есть'.format(self.name), color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint('{} пошел спать'.format(self.name), color='blue')

    def tear(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} пакостит'.format(self.name), color='green')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.tear()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 50
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {},кошачей еды {},грязь {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


cat = Cat()
house = House()
man = Man()
man.go_to_the_house(home=house)
man.take_the_cat(meow=cat)
cat.go_to_the_house(home=house)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    cat.act()
    print('--- в конце дня ---')
    print(house)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# Зачёт!
