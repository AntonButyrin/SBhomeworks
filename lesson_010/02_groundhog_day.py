# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class MainException(Exception):
    pass


class IamGodError(MainException):

    def __str__(self):
        return "Стал похож на одного бородатого мужика, только без суперспособностей"


class DrunkError(MainException):

    def __str__(self):
        return "Дед, ты пьян, иди домой"


class CarCrashError(MainException):

    def __str__(self):
        return "Ну конечно, мы же миллионеры, что ты еще разобьешь"


class GluttonyError(MainException):

    def __str__(self):
        return "Жирный, жирный, жирный, как поезд пассажирный..."


class DepressionError(MainException):

    def __str__(self):
        return "Снова родился в моей родной стране? Тут все так живут,привыкай"


class SuicideError(MainException):

    def __str__(self):
        return "restart after 5...4...3...2...1..."


hell_days = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]


def one_day():
    counter_carma = random.randint(1, 7)
    chance_error = random.randint(1, 13)
    if chance_error == 13:
        raise random.choice(hell_days)
    return counter_carma


carma = 0
while True:
    try:
        one_day()
        carma += one_day()
        if carma >= ENLIGHTENMENT_CARMA_LEVEL:
            break
    except MainException as exc:
        print(exc)
print(carma)

# Зачёт!
