# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#  есть,
#  играть в WoT,
#  ходить на работу,
# Жена может:
#  есть,
#  покупать продукты,
#  покупать шубу,
#  убираться в доме,

# Все они живут в одном доме, дом характеризуется:
# кол-во денег в тумбочке (в начале - 100)
# кол-во еды в холодильнике (в начале - 50)
# кол-во грязи (в начале - 0)

# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).

# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class Human:
    death_message = None

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = house

    def __str__(self):
        return "сытость {}, счастье {}".format(self.fullness, self.happy)

    def eat(self):
        self.house.counter_food += 20
        self.fullness += 20
        self.house.food -= 20
        cprint("{} поел.".format(self.name))

    def pet_the_cat(self):
        self.happy += 5
        cprint("Кошка поглажена")

    def act(self):
        self.house.dirt += 5
        if self.fullness <= 0:
            cprint(f'{self.name} {self.death_message} от голода', color='yellow')
            return
        elif self.happy <= 10:
            cprint(f'{self.name} {self.death_message} от депрессии', color='yellow')
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.dirt >= 90:
            self.happy -= 10
        dice = randint(1, 3)
        if dice == 1:
            self.pet_the_cat()


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.counter_coat = 0
        self.counter_food = 0
        self.counter_money = 0
        self.cat_food = - 30

    def __str__(self):
        cprint("Всего пока что : {} заработано денег. {} съедено еды. {} куплено шуб ".format(
            self.counter_money, self.counter_food, self.counter_coat
        ))
        return "В доме: денег: {}, еды: {}, грязи: {}".format(self.money, self.food, self.dirt)


class Husband(Human):
    death_message = "умер"

    def act(self):
        super().act()
        dice = randint(1, 3)
        if self.happy < 20:
            self.gaming()
        elif dice == 1:
            self.work()
        else:
            self.gaming()

    def work(self):
        self.house.counter_money += 150
        self.house.money += 150
        self.fullness -= 10
        cprint("{} сходил на работу.".format(self.name))

    def gaming(self):
        self.happy += 20
        self.fullness -= 10
        cprint("{} поиграл.".format(self.name))


class Wife(Human):
    death_message = "умерла"

    def act(self):
        super().act()
        if self.happy < 20:
            self.buy_fur_coat()
        elif self.house.food <= 30:
            self.shopping()
        elif self.house.cat_food <= 50:
            self.cat_shopping()
        elif self.house.dirt >= 70:
            self.clean_house()
        else:
            cprint("{} делает непонятные мужскому мозгу женские дела".format(self.name))
            self.fullness -= 10
            self.happy -= 5

    def shopping(self):
        self.house.food += 50
        self.house.money -= 50
        self.fullness -= 10
        cprint("{} сходила в магазин.".format(self.name))

    def buy_fur_coat(self):
        self.house.money -= 350
        self.house.counter_coat += 1
        self.fullness -= 10
        self.happy += 60
        cprint("{} купила пальто.".format(self.name))

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 10
        cprint("{} убрала квартиру.".format(self.name))

    def cat_shopping(self):
        self.house.cat_food += 60
        self.house.money -= 60
        self.fullness -= 10
        cprint("{} сходила в магазин  для кота.".format(self.name))


#  после реализации первой части - отдать на проверку учителю
# ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:
    death_message = " умер"

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return "сытость {}".format(self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} {self.death_message} от голода', color='yellow')
            return
        if self.fullness < 20:
            self.eat()
        dice = randint(1, 3)
        if dice == 1:
            self.sleep()
        elif dice == 3:
            self.soil()
        elif dice == 2:
            self.eat()

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        cprint("Кошка поела")

    def sleep(self):
        self.fullness -= 10

    def soil(self):
        self.house.dirt += 5
        self.fullness -= 10


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
murzik = Cat(name='Мурзик', house=home)
for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='green')


# ####################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


class Child:

    def __init__(self, name, house):
        self.name = name
        self.happy = 100
        self.fullness = 50
        self.house = house

    def __str__(self):
        return "сытость {}, счастье {}".format(self.fullness, self.happy)

    def act(self):
        if self.fullness <= 20:
            self.eat()
        dice = randint(1, 3)
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        self.fullness += 10
        self.house.food -= 10
        print("Child eating")

    def sleep(self):
        self.fullness -= 10
        print("Child sleeping")


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='green')
# ####################################################### Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='green')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# Зачёт!
