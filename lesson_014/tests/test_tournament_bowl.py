from lesson_014 import tournament_bowl
import unittest


class TestBowling(unittest.TestCase):

    def test_normal(self):
        result = tournament_bowl.open_file(files='for_normal.txt')
        self._getAssertEqualityFunc(95, result)

    def test_symbol(self):
        result = tournament_bowl.open_file(files="for_symbol.txt")
        self._getAssertEqualityFunc(SyntaxError, result)

    def test_value(self):
        result = tournament_bowl.open_file(files="for_value.txt")
        self._getAssertEqualityFunc(ValueError, result)


if __name__ == '__main__':
    unittest.main()
