import unittest

from uno.Deck import Deck
from uno.Game import Game
from uno.Player import Player

empty_deck = []
deck = Deck().cards
empty_players = []


class TestGame(unittest.TestCase):

    # Game should raise value error when players < 2
    def test_should_raise_value_error_for_zero_or_One_players(self):
        self.assertRaises(ValueError, Game, [], deck)
        self.assertRaises(ValueError, Game, [1], deck)

    # Game can't start without a deck. Expect ValueError
    def test_game_raises_error_for_no_deck(self):
        self.assertRaises(ValueError, Game, [1], None)

    # Game can't start with an empty deck. Expect ValueError
    def test_game_raises_error_on_empy_deck(self):
        self.assertRaises(ValueError, Game, [1], [])

    # Players should be a list of Player objects
    def test_players_has_objects_of_player_class(self):
        dummy_game = Game([Player(), Player()], deck)
        players = dummy_game.players
        for player in players:
            self.assertIsInstance(player, Player)

    # When the game starts the players should have no cards
    def test_players_have_no_cards_at_start(self):
        game = Game([Player(), Player()], deck)
        game_players = game.players
        for player in game_players:
            self.assertEqual(len(player.cards), 0)
