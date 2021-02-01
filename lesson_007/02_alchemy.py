# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.part = 'Вода'

    def __str__(self):
        return self.part

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Wind:

    def __init__(self):
        self.part = 'Воздух'

    def __str__(self):
        return self.part

    def __add__(self, other):
        if isinstance(other, Fire):
            return Thunder()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:

    def __init__(self):
        self.part = 'Огонь'

    def __str__(self):
        return self.part

    def __add__(self, other):
        if isinstance(other, Wind):
            return Thunder()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None


class Earth:

    def __init__(self):
        self.part2 = 'Земля'

    def __str__(self):
        return self.part2

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        else:
            return None


class Storm:

    def __init__(self):
        self.storm = "шторм"

    def __str__(self):
        return 'Получился ' + self.storm


class Steam:

    def __init__(self):
        self.name = "пар"

    def __str__(self):
        return 'Получился ' + self.name


class Dirt:

    def __init__(self):
        self.name = "грязь"

    def __str__(self):
        return 'Получилась ' + self.name


class Thunder:

    def __init__(self):
        self.name = "молния"

    def __str__(self):
        return 'Получилась ' + self.name


class Dust:

    def __init__(self):
        self.name = "пыль"

    def __str__(self):
        return 'Получилась ' + self.name


class Lava:

    def __init__(self):
        self.name = "лава"

    def __str__(self):
        return 'Получилась ' + self.name


storm = Water() + Wind()
steam = Water() + Fire()
dirt = Water() + Earth()
thunder = Wind() + Fire()
dust = Wind() + Earth()
lava = Fire() + Earth()
print('\n', storm, '\n', steam, '\n', dirt, '\n', thunder, '\n', dust, '\n', lava)

#  В этом задании нужно реализовать именно сложение элементов,
#  которое должно работать примерно так:
#  steam = Water + Fire
#  В этом вам поможет функция isinstance, которая позволяет
#  определить является ли объект экземпляром определённого класса.
#  list1 = [1, 2, 3]
#  isinstance(list1, list) вернёт True
#  isinstance(list1, str) вернёт False
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# Зачёт!
