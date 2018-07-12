import unittest

from uno.Card import Card
from uno.Player import Player


class TestPlayer(unittest.TestCase):
    # Player should decide to Draw from the deck when there are no valid cards
    def test_player_decides_to_draw_when_there_Are_no_valid_cards(self):
        player = Player("S", [Card("RED", 1)] * 7)
        top_card = Card("BLUE", 4)
        self.assertEqual(player.decide_action(top_card), "TAKE")

    # Player should decide to PLAY when there are valid cards
    def test_player_should_play_when_there_are_valid_cards(self):
        player = Player("S", [Card("RED", 1)] * 7)
        top_card = Card("RED", 1)
        self.assertEqual(player.decide_action(top_card), "PLAY")

    # Player's total value should be the sum of values of all of his cards
    def test_players_total_value_is_sum_of_values_of_his_cards(self):
        cards = [Card("RED", 2), Card("BLUE", 8), Card("RED", action="SKIP"),
                 Card("YELLOW", action="REVERSE"), Card(wild="WILD"),
                 Card(wild="WILD_DRAW_FOUR")]
        player = Player(name="DSP", cards=cards)
        self.assertEqual(player.get_total_value(), 150)

    # Players total value should be zero when he has no cards
    def test_player_with_no_cards_should_have_zero_value(self):
        cards = []
        player = Player(name="", cards=cards)
        self.assertEqual(player.get_total_value(), 0)
