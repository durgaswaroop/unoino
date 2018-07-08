import unittest

from uno.Card import Card
from uno.GameRules import is_played_card_valid

# Zero cards
red_zero = Card("RED", 0)
blue_zero = Card("BLUE", 0)
green_zero = Card("GREEN", 0)
yellow_zero = Card("YELLOW", 0)

# Action cards
green_skip = Card(color="GREEN", action="SKIP")
blue_skip = Card(color="BLUE", action="SKIP")
red_rev = Card(color="RED", action="REVERSE")

# Other numbered cards
red_nine = Card("RED", 9)
blue_five = Card("BLUE", 5)
green_one = Card("GREEN", 1)
yellow_three = Card("YELLOW", 3)

# Wilds
red_wild = Card(wild="WILD", color="RED")
blue_wild = Card(wild="WILD", color="BLUE")
green_wild = Card(wild="WILD", color="GREEN")

# Draw fours
red_wdf = Card(wild="WILD_DRAW_FOUR", color="RED")
blue_wdf = Card(wild="WILD_DRAW_FOUR", color="BLUE")


class TestGameRules(unittest.TestCase):

    # If played card is  Red 9 and the top card is Red 0, it should be a match
    def test_same_color_should_be_valid(self):
        self.assertTrue(
            is_played_card_valid(played_card=red_nine, top_card=red_zero))

    # If top card is Red 0 and played card is Blue 5, it shouldn't match
    def test_red_0_for_blue_5_should_be_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=red_zero, played_card=blue_five))

    # If top card is Yellow 0 and played card is Green 1, it shouldn't match
    def test_green_1_for_yellow_0_should_be_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=yellow_zero, played_card=green_one))

    # If top card is Red 0 & played card is Green zero, it should match
    def test_green_0_for_red_0_should_be_valid(self):
        self.assertTrue(
            is_played_card_valid(top_card=red_zero, played_card=green_zero))

    # Two wild cards should match
    def test_two_wild_cards_match(self):
        self.assertTrue(
            is_played_card_valid(top_card=red_wild, played_card=red_wild))

    # Two wild draw four cards should match
    def test_two_wild_draw_four_cards_match(self):
        self.assertTrue(
            is_played_card_valid(top_card=red_wdf, played_card=red_wdf))

    # A wild card and a wild draw four of different colors don't match
    def test_two_different_wild_cards_dont_match(self):
        self.assertFalse(
            is_played_card_valid(top_card=red_wdf, played_card=blue_wild))

    # A red card should match a red wild card
    def test_red_color_card_should_match_red_wild_card(self):
        self.assertTrue(
            is_played_card_valid(top_card=red_zero, played_card=red_wild))

    # Two skips can match even if they've different colors
    def test_two_skips_match(self):
        self.assertTrue(
            is_played_card_valid(top_card=blue_skip, played_card=green_skip))

    # A blue skip can match a blue card
    def test_colored_card_can_match_a_skip_of_that_color(self):
        self.assertTrue(
            is_played_card_valid(top_card=green_skip, played_card=green_zero))

    # A blue skip can match a blue wild draw four card
    def test_colored_card_can_wild_draw_four_of_that_color(self):
        self.assertTrue(
            is_played_card_valid(top_card=red_wdf, played_card=red_nine))

    # A blue skip on green wild is invalid
    def test_blue_skip_on_green_wild_is_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=green_wild, played_card=blue_skip))

    # A red reverse on a blue zero is invalid
    def test_red_reverse_on_blue_zero_is_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=blue_zero, played_card=red_rev))

    # A red wild on a blue wild draw four is invalid
    def test_red_wild_on_blue_wild_draw_four_is_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=blue_wdf, played_card=red_wild))

    # A red draw four on a blue skip is invalid
    def test_red_draw_four_on_blue_skip_is_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=blue_skip, played_card=red_wdf))
