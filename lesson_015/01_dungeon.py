# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600

#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
# чек лист:
# 1.сражение с монстрами ☑
# 2.проверить локации ☑
# 3.сделать время ☑
# 4.выйти к победе ☑
# 5.проиграть по времени ☑
import csv
import datetime
import json
import re
import time
from decimal import Decimal

path = 'rpg.json'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


class Dungeon:

    def __init__(self, file):
        """Создать основные переменные"""
        self.file = file
        self.roadmap = dict()
        self.remaining_time = Decimal("123456.0987654321")
        self.exp = 0
        self.dict_string = dict()
        self.string = dict()
        self.dict_loc = dict()
        self.choice = list()
        self.name_loc = str
        self.loc_choice = 0
        self.player_input = 0
        self.first_time = datetime.datetime.now().second
        self.loc = {'current_location': None, 'current_experience': None, 'current_date': None}
        self.start = time.monotonic()
        self.file_open = open('result_play.csv', 'a', newline='')

    def open_file(self):
        """Открыть файл и вернуть его в виде словаря."""
        with open(self.file, 'r') as read_file:
            loaded_json_file = json.load(read_file)
            self.roadmap = loaded_json_file
            return loaded_json_file

    def open_dict(self, name_loc):
        """Постепенно открыть словарь."""
        for keys in name_loc:
            for values in name_loc.values():
                count_mob = 0
                count_loc = 0
                for value in values:
                    if isinstance(value, dict):
                        self.dict_string[count_loc + 1] = value
                        count_loc += 1
                    elif isinstance(value, str):
                        self.string[count_mob + 1] = value
                        count_mob += 1
            self.name_loc = keys

    def actions(self):
        """Выбрать действие"""
        flag = True
        while flag:
            if len(self.string) > 0:
                print(f"{1}.Атаковать монстра")
                print(f"{2}.Перейти в другую локацию")
                print(f"{3}.Сдаться и выйти из игры")
                print("*" * 30)
                self.player_input = int(input("Введите число: "))
                print("*" * 30)
                print(f'Вы выбрали {self.player_input}')
                flag = False
            elif len(self.dict_string) > 0:
                print(f"{2}.Перейти в другую локацию: ")
                print(f"{3}.Сдаться и выйти из игры: ")
                print("*" * 30)
                self.player_input = int(input("Введите число: "))
                print("*" * 30)
                print(f'Вы выбрали {self.player_input}')
                flag = False
            else:
                print(f"{2}.Перейти в другую локацию: ")
                print(f"{3}.Сдаться и выйти из игры: ")
                print("*" * 30)
                print("Вы выбрали сражаться с монстром: ")
                flag = False

    def player_choice(self):
        """Открыть текущую локацию и дать выбор."""
        print(f'Вы находитесь в локации: {self.name_loc}')
        print(f'На данный момент у вас времени: {self.remaining_time} секунд')
        self.real_time_running()
        print(f'Внутри вы видите:')
        for i in self.string.values():
            print(f'- Монстр: {i}')
        for j in self.dict_string.values():
            for values in j.keys():
                print(f'- Вход в локацию: {values}')
        print("*" * 30)
        print("Выберите действие: ")
        self.actions()

    def type_choice(self):
        """Определить выбор игрока и дать возможность к действию."""
        flag = True
        while flag:
            if self.player_input == 1:
                print("*" * 30)
                print("Выберите монстра: ")
                for n, i in self.string.items():
                    print(f'{n} Монстр: {i}')
                self.loc_choice = int(input("Введите число: "))
                print("*" * 30)
                if self.loc_choice in self.string.keys():
                    self.name_mob = self.string[self.loc_choice]
                    print(f"вы выбрали Монстра : {self.name_mob}")
                    self.kill_monster_exp(self.name_mob)
                    self.spent_time(self.name_mob)
                    del self.string[self.loc_choice]
                    if len(self.string) == 0:
                        return self.change_loc()
                    else:
                        print("Дальше убиваем монстров?")
                        print(" 1 да, 2 нет")
                        self.player_input = int(input("Выберите букву :"))
                        if self.player_input == 1:
                            flag = True
                        else:
                            return self.change_loc()

                elif len(self.string.keys()) == 0:
                    print("*" * 30)
                    print("Здесь мобов нет:(")
                    flag = False
            elif self.player_input == 2:
                return self.change_loc()

            elif self.player_input == 3:
                flag = False

    def ultra_game(self):
        """Организовать игровой цикл."""
        writer = csv.DictWriter(self.file_open, delimiter=',', fieldnames=field_names)
        writ = csv.writer(self.file_open)
        writ.writerow(field_names)
        self.open_file()
        self.open_dict(rpg.roadmap)
        self.player_choice()
        while True:
            a = self.loc = {'current_location': self.name_loc, 'current_experience': self.exp,
                            'current_date': self.remaining_time}
            writer.writerow(a)
            self.open_dict(self.type_choice())
            self.player_choice()
            if self.player_input == 3:
                print("*" * 30)
                print('Конец игры. Ты проиграл.')
                self.file_open.close()
                break

    def kill_monster_exp(self, monster):
        """Найти в имени монстра строку опыта и убить монстра."""
        find_exp = r'exp\d{1,15}'
        alignment = re.search(find_exp, monster).group()
        only_exp = int(alignment[3:])
        self.exp += only_exp
        print(f'Добавлено опыта {only_exp}')
        print(f'Огого, опыта уже {self.exp}')

    def spent_time(self, object_rpg):
        """Найти в объекте строку времени."""
        find_time = r"tm[-+]?(?:\d+(?:\.\d*)?|\.\d+)"
        alignment = re.search(find_time, object_rpg).group()
        only_time = Decimal(alignment[2:])
        self.remaining_time -= only_time
        format_time = '{:f}'.format(self.remaining_time)
        print(f'Времени потрачено {only_time}')
        print(f'Осталось : {format_time} секунд.')
        if self.remaining_time < 0:
            print("*" * 30)
            print('Конец игры. Ты проиграл.')
            exit()

    def change_loc(self):
        """Выбрать локацию"""
        print("*" * 30)
        print("Выберите локацию: ")
        for n, j in self.dict_string.items():
            for value in j.keys():
                print(f"{n} Локация : {value}")
                print("*" * 30)
        self.loc_choice = int(input("Введите число: "))
        print("*" * 30)
        if self.loc_choice in self.dict_string:
            key = self.dict_string.setdefault(self.loc_choice)
            new_name_loc = ', '.join(list(key.keys()))
            print(f"вы выбрали локацию {new_name_loc}")
            print("*" * 30)
            if new_name_loc == "Hatch_tm159.098765432" and self.exp >= 280:
                self.win(key=key)

            elif new_name_loc == "Hatch_tm159.098765432" and self.exp < 280:
                print(f"Ты был близок, но опыта маловато. Надо 280, у тебя {self.exp}. Ты проиграл")
                exit()
            self.spent_time(new_name_loc)
            self.string.clear()
            self.dict_string.clear()
            return key

    def win(self, key):
        """Победить"""
        self.spent_time("Hatch_tm159.098765432")
        if self.remaining_time > 0:
            value_winner = key.values()
            winner = ', '.join(list(value_winner))
            print(winner)
            format_time = '{:f}'.format(self.remaining_time)
            print(f'Времени осталось {format_time}')
            print(f'Опыта собрано {self.exp}')
            writer = csv.DictWriter(self.file_open, delimiter=',', fieldnames=field_names)
            a = self.loc = {'current_location': "Hatch_tm159.098765432", 'current_experience': self.exp,
                            'current_date': format_time}
            writer.writerow(a)
            self.file_open.close()
            exit()
        else:
            print(f"Ты был близок, но врезя закончилось {self.remaining_time}. Ты проиграл")

    def real_time_running(self):
        """Определить разницу времени"""
        elapsed = time.monotonic() - self.start
        minutes = round(elapsed / 60, 2)
        print(f'Прошло реального времени : {minutes} минут/секунд')


rpg = Dungeon(file=path)
rpg.ultra_game()

# Зачёт!
