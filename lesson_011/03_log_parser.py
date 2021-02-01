# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
from pprint import pprint


def op(file_name):
    with open(file_name, 'r') as file:
        last_nok = "None"
        counter = 1
        for line in file:  # создаем строчку
            if line.endswith('NOK\n'):  # если строчка НОК то:
                if line[1:17] == last_nok:  # если часть строки == последнему НОК то:
                    counter += 1  # делаем счетчик + 1
                else:
                    if last_nok == "None":
                        last_nok = line[1: 17]
                    else:
                        yield last_nok, counter
                        if line[1:17] != last_nok:
                            counter = 1
                            last_nok = line[1: 17]
                yield last_nok, counter


grouped_events = op(file_name='events.txt')
for group_time, event_count in grouped_events:
    pprint(f'[{group_time}] {event_count}')

# Зачёт!
