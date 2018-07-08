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
