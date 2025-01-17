#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

# NOTE: Молодец что использовал .5, вместо 0.5 для обозначения float значения.
moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5
london_paris = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** .5


distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Paris'] = london_paris
distances['London']['Moscow'] = moscow_london

distances['Paris'] = {}
distances['Paris']['London'] = london_paris
distances['Paris']['Moscow'] = moscow_paris

pprint(distances)

# NOTE: Должна быть ровно одна пустая строка в конце файла.
# Сейчас с вас стиль не требуем, но будем требовать в дальнейшем.

# А так молодец,
# Зачёт!
