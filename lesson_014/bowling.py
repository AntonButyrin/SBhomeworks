class Bowling:
    """

    Для старых правил

    """

    def __init__(self, results):
        self.good_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.wrong_numbers = None
        self.result = results
        self.score = 0
        self.frame = 0

    def resultec(self):
        print(f" игра:>{self.result}<", '\n', f"счёт:>{self.score}<")
        return self.score

    def play_the_game(self):
        for line in self.split_result(results=self.result):
            self.calculation(line)
            if self.frame == 11:
                raise ValueError("Неправильный фрейм")
            elif self.wrong_numbers is not None:
                raise SyntaxError('неверный символ')

    def strike(self):
        self.score += 20

    def spare(self):
        self.score += 15

    def normal_numbers(self, line):
        if line[0] in self.good_numbers and line[1] in self.good_numbers:
            if int(line[0]) + int(line[1]) >= 10:
                raise ValueError
            else:
                self.score += int(line[0])
                self.score += int(line[1])
        else:
            self.wrong_numbers = line[0]
            self.wrong_numbers = line[1]

    def split_result(self, results: str):
        while len(results) > 0:
            if results[0] == 'X':
                yield 'X'
                results = results[1:]
            else:
                yield results[:2]
                results = results[2:]

    def calculation(self, line):
        if 'X' in line:
            self.strike()
            self.frame += 1
        else:
            if '/' in line[1]:
                self.spare()
                self.frame += 1
            elif '/' in line[0]:
                raise IndexError
            elif '-' in line[0] and line[1] in self.good_numbers:
                self.score += 0
                self.score += int(line[1])
                self.frame += 1
            elif '-' in line[1] and line[0] in self.good_numbers:
                self.score += 0
                self.score += int(line[0])
                self.frame += 1
            elif '-' in line[0] and '-' in line[1]:
                self.score += 0
                self.frame += 1
            else:
                self.normal_numbers(line=line)


class NewGameBowl(Bowling):
    """

    Для новых правил

    """

    def __init__(self, results):
        super().__init__(results)

    def spare(self, line):
        if line[0] in self.good_numbers and line[1] == '/':
            self.score += 10
            if line[2] in self.good_numbers:
                self.score += int(line[2])

    def normal_numbers(self, line):
        if line[0] in self.good_numbers and line[1] in self.good_numbers:
            self.score += int(line[0]) + int(line[1])
        else:
            self.wrong_numbers = line[0]
            self.wrong_numbers = line[1]

    def half_frame(self, line):
        if '-' in line[0] and line[1] in self.good_numbers:
            self.score += 0
            self.score += int(line[1])

        elif '-' in line[1] and line[0] in self.good_numbers:
            self.score += 0
            self.score += int(line[0])

        elif '-' in line[0] and '-' in line[1]:
            self.score += 0

    def strike(self, line):
        if line[0] == 'X' and line[1] in self.good_numbers and line[2] == '/':
            self.score += 20
        elif line[0] == 'X' and line[1] == 'X' and line[2] == 'X':
            self.score += 30
        elif line[0] == 'X' and line[1] == 'X' and line[2] in self.good_numbers:
            self.score += 20 + int(line[2])
        elif line[0] == 'X' and line[1] in self.good_numbers and line[2] in self.good_numbers:
            self.score += 10 + int(line[1]) + int(line[2])

    def split_result(self, results: str):
        while len(results) > 0:
            if len(results) != 1:
                if results[0] == 'X':
                    var = 'X'
                    results = results[1:]
                    if results[0] == 'X':
                        var2 = 'X'
                        results = results[1:]
                        if results[0] == 'X':
                            var3 = 'X'
                            results = results[1:]
                            yield var, var2, var3
                        else:
                            var3 = results[0]
                            yield var, var2, var3
                    else:
                        var2 = results[0]
                        results = results[1:]
                        var3 = results[0]
                        yield var, var2, var3
                else:
                    var = results[:1]
                    results = results[1:]
                    var2 = results[:1]
                    if '/' in var2:
                        results = results[1:]
                        var3 = results[:1]
                        yield var, var2, var3
                    else:
                        results = results[2:]
                        yield var, var2
            else:
                yield results[:1]
                results = results[1:]

    def calculation(self, line):
        if len(line) != 1:
            if 'X' in line:
                self.strike(line)
                self.frame += 1
            else:
                if '/' in line[1]:
                    self.spare(line)
                    self.frame += 1
                elif '/' in line[0]:
                    self.frame += 1
                    pass
                elif '-' in line:
                    self.half_frame(line)
                    self.frame += 1
                else:
                    self.normal_numbers(line=line)
                    self.frame += 1
        else:
            if line == 'X':
                self.score += 10
                self.frame += 1
            elif line == '/':
                self.score += 10
                self.frame += 1
            else:
                self.score += int(line)
                self.frame += 1
