# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>
import argparse
from tournament_bowl import OldGame, NewGame


def work_with_files(input_file, output_file, game):
    old_game = OldGame(files=input_file)
    new_game = NewGame(files=input_file)
    with open(output_file, 'a', encoding='utf-8') as f:
        if game == 'newgame':
            for i in new_game.game():
                f.write(i + '\n')
        elif game == 'oldgame':
            for i in old_game.game():
                f.write(i + '\n')
        else:
            print("Введена неправильная команда")


if __name__ == "__main__":
    file = 'tournament.txt'
    files = 'resut_tourn.txt'
    parser = argparse.ArgumentParser(description='Bowling')
    parser.add_argument('--input', default=file, type=str, required=True)
    parser.add_argument('--output', default=files, type=str, required=True)
    parser.add_argument('--game', default=files, type=str, required=True,
                        help='NewRules command : >newgame< '
                             '  OldRules command: >oldgame<'
                        )
    args = parser.parse_args()
    work_with_files(input_file=args.input, output_file=args.output, game=args.game)

# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+

# Зачёт!
