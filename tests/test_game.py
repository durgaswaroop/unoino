import unittest
from uno.Game import Game


class TestGame(unittest.TestCase):

    def test_invalid_players(self):
        # Game should raise value error when players <= 0
        self.assertRaises(ValueError, Game, 0)
        self.assertRaises(ValueError, Game, -2)
        self.assertRaises(ValueError, Game, -100)

    def test_player_numbers(self):
        # If Game has non-zero players, game should have non-zero players
        self.assertEqual(10, Game(players=10).players)
        self.assertEqual(100, Game(players=100).players)
    