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

    # Check the next player in clockwise
    def test_next_player_in_clockwise(self):
        game = Game([Player()] * 3, deck, disable_output=True)
        game.is_clockwise = True

        # Current Player = 1, Next player should be = 2
        game.current_player = 1
        self.assertEqual(game.get_next_player(), 2)

        # Current Player = 2, Next player = 0
        game.current_player = 2
        self.assertEqual(game.get_next_player(), 0)

    # Check the next player in anti-clockwise
    def test_next_player_in_anti_clockwise(self):
        game = Game([Player()] * 3, deck, disable_output=True)
        game.is_clockwise = False

        # Current Player = 1, Next player should be = 0
        game.current_player = 1
        self.assertEqual(game.get_next_player(), 0)

        # Current Player = 2, Next player = 1
        game.current_player = 2
        self.assertEqual(game.get_next_player(), 1)

        # Current Player = 0, Next player = 2
        game.current_player = 0
        self.assertEqual(game.get_next_player(), 2)

    # The card played by a player should become the new top card
    def test_top_card_should_be_updated_when_a_player_plays(self):
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
        self.assertEqual(game.top_card, game.discard_pile[-1])

    # When a player plays skip, the next player should be skipped
    def test_skip_should_skip_the_next_player(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="SKIP")
        game.discard_pile = [Card("BLUE", action="SKIP")]

        players[1].cards = [Card("RED", action="REVERSE"), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", action="SKIP")]

        # The player has to play skip here as that is the only valid card
        game.play_turn()

        self.assertEqual(game.next_player, 0)

    # When a player plays reverse, the direction should change
    # and the next player should  be updated too
    def test_reverse_should_flip_direction_and_change_next_player(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("RED", action="REVERSE"), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", action="SKIP")]

        # Here the reverse card is the only valid play
        game.play_turn()

        self.assertFalse(game.is_clockwise)
        self.assertEqual(game.next_player, 0)

    # When a player plays a Wild card, they should set a color for that too
    def test_wild_cards_played_should_have_a_color_associated_with_them(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("RED", 5), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", action="SKIP"),
                            Card(wild="WILD")]

        # Here the wild card is the only valid play
        game.play_turn()

        self.assertTrue(game.top_card.is_wild_card)
        self.assertTrue(game.top_card.color)  # Shouldn't be None

    # When a player plays Draw 2 the next player should pick up two cards
    def test_on_playing_draw_2_next_player_takes_two_cards(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("RED", 5), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", action="SKIP"),
                            Card("BLUE", action="DRAW_TWO")]

        # Here the draw two card is the only valid play
        game.play_turn()
        self.assertTrue(game.top_card.is_d2)
        self.assertEqual(game.last_player_decision, "PLAY")

        game.current_player = 2  # Need to manually set it here for the tests

        # Next turn. This player should pick two cards
        game.play_turn()
        self.assertEqual(len(players[2].cards), 9)

    # WIld Draw four should be played only when there are no other valid cards
    def test_player_should_play_draw_four_only_if_no_other_valid_cards(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("YELLOW", action="REVERSE"),
                            Card("RED", 2), Card("GREEN", action="SKIP"),
                            Card(wild="WILD_DRAW_FOUR"),
                            Card("BLUE", action="DRAW_TWO")]
        # Blue Draw two -> value = 20
        # Yellow Reverse -> Value = 20
        # Wild Draw Four -> value = 50
        game.play_turn()

        # ALtghough Draw four is the card with the highest value but since we
        # can still play yellow reverse or blue draw two, draw four shouldn't be
        # played
        self.assertFalse(game.top_card.is_wild_card)
        self.assertFalse(game.top_card.is_d4)

    # The player when playing should play the card with the highest value
    def test_player_plays_the_card_with_the_highest_value(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("YELLOW", action="REVERSE"),
                            Card("RED", 2), Card("GREEN", action="SKIP"),
                            Card(wild="WILD"),
                            Card("BLUE", action="DRAW_TWO")]
        # Blue Draw two -> value = 20
        # Yellow Reverse -> Value = 20
        # Wild Draw Four -> value = 50l
        game.play_turn()
        self.assertTrue(game.top_card.is_wild_card)
        self.assertTrue(game.top_card.wild == "WILD")

    # When a player plays Draw 4, the next player should pick up four cards
    def test_on_playing_draw_4_next_player_takes_4_card(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]

        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("RED", 5), Card("YELLOW", 4),
                            Card("RED", 2), Card("GREEN", action="SKIP"),
                            Card(wild="WILD_DRAW_FOUR")]

        # Here the draw 4 card is the only valid play
        game.play_turn()
        self.assertTrue(game.top_card.is_d4)
        self.assertEqual(game.last_player_decision, "PLAY")

        game.current_player = 2  # Need to manually set it here for the tests

        # Next turn. This player should pick two cards
        game.play_turn()
        self.assertEqual(len(players[2].cards), 11)  # 7+4

    # When a player plays their last card, the game should end
    def test_game_ends_when_a_player_plays_last_card(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]
        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("BLUE", 5)]

        game.play_turn()
        self.assertEqual(game.status, "GAMEOVER")

    # When a game is over, the winner should be declared
    def test_winner_is_printed_when_a_game_ends(self):
        players = [Player(name="Naruto", cards=[]),
                   Player(name="Sasuke", cards=[]),
                   Player(name="Sakura", cards=[])]
        game = Game(players, deck, disable_output=True)

        # Overwriting variables for mocking
        game.top_card = Card("BLUE", action="REVERSE")
        game.discard_pile = [Card("BLUE", action="REVERSE")]

        players[1].cards = [Card("BLUE", 5)]

        game.play_turn()
        self.assertEqual(game.winner, 1)

