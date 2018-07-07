import unittest

from uno.Deck import Deck
from uno.Game import Game

empty_deck = []
deck = Deck().cards
empty_players = []

class TestGame(unittest.TestCase):

    # Game should raise value error when players = 0
    def test_should_raise_value_error_for_zero_players(self):
        self.assertRaises(ValueError, Game, [], deck)

    # Game can't start without a deck. Expect ValueError
    def test_game_raises_error_for_no_deck(self):
        self.assertRaises(ValueError, Game, [1], None)

    # Game can't start with an empty deck. Expect ValueError
    def test_game_raises_error_on_empy_deck(self):
        self.assertRaises(ValueError, Game, 10, [])
