import unittest
from uno.Game import Game


class TestGame(unittest.TestCase):

    # Game should raise value error when players <= 0
    def test_should_raise_value_error_for_invalid_player_count(self):
        self.assertRaises(ValueError, Game, 0)
        self.assertRaises(ValueError, Game, -2)
        self.assertRaises(ValueError, Game, -100)

