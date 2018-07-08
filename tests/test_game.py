import io
import sys
import unittest

from uno.Card import Card
from uno.Deck import Deck
from uno.Game import Game
from uno.GameRules import is_played_card_valid
from uno.Player import Player

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
        dummy_game = Game([Player(), Player()], deck, disable_output=True)
        players = dummy_game.players
        for player in players:
            self.assertIsInstance(player, Player)

    # Before the game setup the players should have no cards
    # def test_players_have_no_cards_at_start(self):
    #     game = Game([Player(), Player()], deck)
    #     game_players = game.players
    #     for player in game_players:
    #         self.assertEqual(len(player.cards), 0)

    # Shuffled deck should be different from the original deck at setup
    def test_shuffeled_deck_is_different_from_original(self):
        game = Game([Player(), Player()], deck, disable_output=True)
        shuffled_deck = game.shuffled_deck
        self.assertNotEqual(len(shuffled_deck), 0)
        self.assertNotEqual(shuffled_deck, deck)

    # When the game is being setup the players names should be printed
    def test_players_names_are_printed(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Game(players, deck)
        sys.stdout = sys.__stdout__
        players_string = f"Players: {players[0].name}, {players[1].name}"
        self.assertTrue(players_string in captured_out.getvalue())

    # After shuffling, the cards should be distributed to each player
    def test_each_player_has_7_cards_after_setup(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        Game(players, deck, disable_output=True)
        for player in players:
            self.assertEqual(len(player.cards), 7)

    # After distribution of cards to players, the remaining should become the pile
    def test_pile_has_1_card_at_beginnin_cards(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        self.assertEqual(len(game.discard_pile), 1)

    # When the game is setup, the first (zeroth index) player should be the dealer
    def test_first_player_is_the_dealer_at_setup(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        self.assertEqual(game.dealer, 0)  # Zero for the first player

    # At the end of game setup the top card should be the last card in the pile
    def test_top_card_is_the_last_card_of_discard_pile(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        self.assertEqual(game.top_card, game.discard_pile[-1])

    # At the end of setup the direction of the game should be clockwise
    def test_initial_direction_is_clockwise(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        self.assertTrue(game.is_clockwise)

    # With Player 0 being the dealer, player 1 should have the first turn
    def test_player_1_has_the_first_turn(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        self.assertEqual(game.current_player, 1)

    # When it is a players turn, they should play a card
    def test_current_player_has_played_a_card(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        game.top_card = Card("BLUE", 4)
        game.discard_pile = [Card("BLUE", 4)]

        players[1].cards = [Card("RED", action="REVERSE"), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", 8),
                            Card("BLUE", 8), Card("GREEN", action="DRAW_TWO"),
                            Card("GREEN", action="DRAW_TWO")]
        game.start()  # Start the game after setup
        self.assertEqual(len(players[1].cards), 6)  # 1 less than 7

    # When the players has played his turn, the pile should have one card more
    def test_pile_has_one_extra_card_after_players_turn(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)
        game.top_card = Card("BLUE", 4)
        game.discard_pile = [Card("BLUE", 4)]

        players[1].cards = [Card("RED", action="REVERSE"), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", 8),
                            Card("BLUE", 8), Card("GREEN", action="DRAW_TWO"),
                            Card("GREEN", action="DRAW_TWO")]
        game.start()  # Start the game after setup
        self.assertEqual(len(game.discard_pile), 2)

    # The card played by player should be a valid card for the existing top card
    def test_player_played_a_valid_card(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", 4)
        game.discard_pile = [Card("BLUE", 4)]

        players[1].cards = [Card("RED", action="REVERSE"), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", 8),
                            Card("BLUE", 8), Card("GREEN", action="DRAW_TWO"),
                            Card("GREEN", action="DRAW_TWO")]
        game.start()  # Start the game after setup
        self.assertTrue(
            is_played_card_valid(game.discard_pile[1], game.discard_pile[0]))

    # If there are no matching cards, the player must take a card from the deck
    def test_player_has_an_extra_card_if_there_Are_no_valid_cards(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", 4)
        game.discard_pile = [Card("BLUE", 4)]

        players[1].cards = [Card("RED", 5)] * 7
        game.start()
        self.assertEqual(len(players[1].cards), 8)

    # Last players decision should be kept track of
    def test_last_player_decision_is_play_if_player_plays(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", 4)
        game.discard_pile = [Card("BLUE", 4)]
        players[1].cards = [Card("RED", action="REVERSE"), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", 8),
                            Card("BLUE", 8), Card("GREEN", action="DRAW_TWO"),
                            Card("GREEN", action="DRAW_TWO")]

        game.start()
        self.assertEqual(game.last_player_decision, "PLAY")

    # Last players decision should be kept track of
    def test_last_player_decision_is_take_if_player_takes(self):
        players = [Player(name="DSP", cards=[]), Player(name="SPD", cards=[])]
        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", 4)
        game.discard_pile = [Card("BLUE", 4)]
        players[1].cards = [Card("RED", 5)] * 7
        game.start()
        self.assertEqual(game.last_player_decision, "TAKE")
