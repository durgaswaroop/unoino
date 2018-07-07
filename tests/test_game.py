import unittest
from uno.Game import Game


class TestGame(unittest.TestCase):

    # Game should raise value error when players <= 0
    def test_should_raise_value_error_for_invalid_player_count(self):
        self.assertRaises(ValueError, Game, 0)
        self.assertRaises(ValueError, Game, -2)
        self.assertRaises(ValueError, Game, -100)

    # Game can't start without a deck. Expect ValueError
    def test_game_raises_error_for_no_deck(self):
        self.assertRaises(ValueError, Game, 10, None)

    # Game can't start with an empty deck. Expect ValueError
    def test_game_raises_error_on_empy_deck(self):
        self.assertRaises(ValueError, Game, 10, [])