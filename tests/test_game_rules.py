import unittest

from uno.Card import Card
from uno.GameRules import is_played_card_valid

# Zero cards
red_zero = Card("RED", 0)
blue_zero = Card("BLUE", 0)
green_zero = Card("GREEN", 0)
yellow_zero = Card("YELLOW", 0)

# Other numbered cards
red_nine = Card("RED", 9)
blue_five = Card("BLUE", 5)
green_one = Card("GREEN", 1)
yellow_three = Card("YELLOW", 3)

# Wilds
wild1 = Card(wild="WILD")
wild2 = Card(wild="WILD")

# Draw fours
df1 = Card(wild="WILD_DRAW_FOUR")
df2 = Card(wild="WILD_DRAW_FOUR")


class TestGameRules(unittest.TestCase):

    # If played card is  Red 9 and the top card is Red 0, it should be a match
    def test_same_color_should_be_valid(self):
        self.assertTrue(
            is_played_card_valid(played_card=red_nine, top_card=red_zero)
        )

    # If top card is Red 0 and played card is Blue 5, it shouldn't match
    def test_red_0_for_blue_5_should_be_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=red_zero, played_card=blue_five)
        )

    # If top card is Yellow 0 and played card is Green 1, it shouldn't match
    def test_green_1_for_yellow_0_should_be_invalid(self):
        self.assertFalse(
            is_played_card_valid(top_card=yellow_zero, played_card=green_one)
        )

    # If top card is Red 0 & played card is Green zero, it should match
    def test_green_0_for_red_0_should_be_valid(self):
        self.assertTrue(
            is_played_card_valid(top_card=red_zero, played_card=green_zero)
        )

    # Two wild cards should match
    def test_two_wild_cards_match(self):
        self.assertTrue(is_played_card_valid(top_card=wild1, played_card=wild2))
