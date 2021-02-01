from bowling import Bowling, NewGameBowl

path = 'tournament.txt'


class OldGame:
    def __init__(self, files):
        self.table_of_score = {}
        self.file = files

    def game(self):

        with open(self.file, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    if line.strip():
                        if line.startswith('###'):
                            self.table_of_score.clear()
                            result = line
                            yield result

                        elif line.startswith('winner'):
                            winner = max(self.table_of_score.values())
                            final_dict = {k: v for k, v in self.table_of_score.items() if v == winner}
                            result = f'winner is {str(list(final_dict))[2:-2]}'
                            yield result
                        else:
                            string1, string2 = line.split()
                            result = Bowling(results=string2)
                            result.play_the_game()
                            self.table_of_score[string1] = result.score
                            result = f'{string1} {string2} {result.score}'
                            yield result
                    else:
                        continue
                except ValueError:
                    result = f'ОШИБКА СТРОКИ: фреймов больше, чем надо>>> {line}'
                    yield result
                except IndexError:
                    result = f'ОШИБКА СТРОКИ: символ  не может стоять вначале фрейма {line}'
                    yield result
                except TypeError as Ty:
                    result = f'ОШИБКА СТРОКИ:{Ty}'
                    yield result
                except SyntaxError:
                    result = f'ОШИБКА СТРОКИ: Недопустимые символы >>> {line} '
                    yield result


class NewGame(OldGame):
    def __init__(self, files):
        super().__init__(files)

    def game(self):

        with open(self.file, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    if line.strip():
                        if line.startswith('###'):
                            self.table_of_score.clear()
                            result = line
                            yield result

                        elif line.startswith('winner'):
                            winner = max(self.table_of_score.values())
                            final_dict = {k: v for k, v in self.table_of_score.items() if v == winner}
                            result = f'winner is {str(list(final_dict))[2:-2]}'
                            yield result
                        else:
                            string1, string2 = line.split()
                            result = NewGameBowl(results=string2)
                            result.play_the_game()
                            self.table_of_score[string1] = result.score
                            result = f'{string1} {string2} {result.score}'
                            yield result
                    else:
                        continue
                except ValueError:
                    result = f'ОШИБКА СТРОКИ: фреймов больше, чем надо>>> {line}'
                    yield result
                except IndexError:
                    result = f'ОШИБКА СТРОКИ: символ  не может стоять вначале фрейма {line}'
                    yield result
                except TypeError as Ty:
                    result = f'ОШИБКА СТРОКИ:{Ty}'
                    yield result
                except SyntaxError:
                    result = f'ОШИБКА СТРОКИ: Недопустимые символы >>> {line} '
                    yield result


if __name__ == "__main__":
    old_game = OldGame(files=path)
    new_game = NewGame(files=path)
    for i in old_game.game():
        print(i)
    for i in new_game.game():
        print(i)
