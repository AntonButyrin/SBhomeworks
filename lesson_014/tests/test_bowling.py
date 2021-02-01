from lesson_014 import bowling
import unittest

for_normal = "4/-5XX27-6"
for_symbol = "asd345-642"
for_long = '4/675-XX23-/55392345'


class TestBowling(unittest.TestCase):

    def test_normal(self):
        result = bowling.Bowling(results=for_normal)
        result.play_the_game()
        self.assertEqual(75, result.resultec())

    def test_symbol(self):
        with self.assertRaises(SyntaxError):
            bowling.Bowling(results=for_symbol).play_the_game()

    def test_long(self):
        with self.assertRaises(ValueError):
            bowling.Bowling(results=for_long).play_the_game()

    def test_normal_new(self):
        result = bowling.NewGameBowl(results=for_normal).play_the_game()
        self._getAssertEqualityFunc(41, result)

    def test_symbol_new(self):
        with self.assertRaises(SyntaxError):
            bowling.NewGameBowl(results=for_symbol).play_the_game()


if __name__ == '__main__':
    unittest.main()
