import io
import sys
import unittest

from uno.Deck import Deck
from uno.Game import Game
from uno.Player import Player

empty_deck = []
deck = Deck().cards
empty_players = []


class TestGame(unittest.TestCase):

    # Game should raise value error when num players < 2
    def test_should_raise_value_error_for_zero_or_One_players(self):
        self.assertRaises(ValueError, Game, [], deck)
        self.assertRaises(ValueError, Game, [1], deck)

    # Game should raise value error when num player > 10
    def test_should_raise_value_error_for_more_than_10_players(self):
        self.assertRaises(ValueError, Game, [Player()] * 11, deck)
        self.assertRaises(ValueError, Game, [Player()] * 111, deck)

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

    # Shuffled deck should be different from the original deck on start
    def test_shuffeled_deck_is_different_from_original(self):
        game = Game([Player(), Player()], deck)
        game.start()
        shuffled_deck = game.shuffled_deck
        self.assertNotEqual(len(shuffled_deck), 0)
        self.assertNotEqual(shuffled_deck, deck)

    # When the game starts the players names should be printed
    def test_players_names_are_printed(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        # players = [Player()]
        game = Game(players, deck)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        game.start()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(),
                         f"Players: {players[0].name}, {players[1].name}")

    # After shuffling, the cards should be distributed to each player
    def test_each_player_has_7_cards(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck)
        game.start()
        for player in players:
            self.assertEqual(len(player.cards), 7)
