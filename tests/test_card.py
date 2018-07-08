import unittest

from uno.Card import Card


class TestCard(unittest.TestCase):
    # A numbered card should have a value of that number
    def test_numbered_card_has_same_value_as_number(self):
        self.assertEqual(Card("RED", 5).value, 5)
        self.assertEqual(Card("BLUE", 2).value, 2)
        self.assertEqual(Card("GREEN", 3).value, 3)

    # An action card should have a value of 20 points
    def test_action_card_has_value_20(self):
        self.assertEqual(Card(color="RED", action="SKIP").value, 20)
        self.assertEqual(Card(color="BLUE", action="REVERSE").value, 20)
        self.assertEqual(Card(color="YELLOW", action="DRAW_TWO").value, 20)

    # A wild card should have a value of 50 points
    def test_wild_card_has_value_50(self):
        self.assertEqual(Card(wild="WILD").value, 50)
        self.assertEqual(Card(wild="WILD_DRAW_FOUR").value, 50)

    # Two numbered cards with same color and same number should be equal
    def test_number_cards_with_same_color_and_number_are_equal(self):
        card1 = Card("BLUE", 5)
        card2 = Card("BLUE", 5)
        self.assertEqual(card1, card2)

    # Two actions cards with same color and same action should be equal
    def test_action_cards_with_same_color_and_action_are_equal(self):
        card1 = Card("BLUE", action="SKIP")
        card2 = Card("BLUE", action="SKIP")
        self.assertEqual(card1, card2)

    # Two wild cards with same color and same action should be equal
    def test_wild_cards_with_same_wildness_are_equal(self):
        card1 = Card(wild="WILD")
        card2 = Card(wild="WILD")
        self.assertEqual(card1, card2)

        card3 = Card(wild="WILD_DRAW_FOUR", color="RED")
        card4 = Card(wild="WILD_DRAW_FOUR", color="RED")
        self.assertEqual(card3, card4)

    # A Skip card should return true for "is_skip"
    def test_that_is_skip_is_true_for_skip_cards(self):
        card1 = Card("BLUE", action="SKIP")
        card2 = Card("RED", action="SKIP")
        self.assertTrue(card1.is_skip)
        self.assertTrue(card2.is_skip)

    # A draw two should return true for "is_d2"
    def test_that_is_d2_is_true_for_draw_two_cards(self):
        card1 = Card("BLUE", action="DRAW_TWO")
        card2 = Card("GREEN", action="DRAW_TWO")
        self.assertTrue(card1.is_d2)
        self.assertTrue(card2.is_d2)

    # A reverse card should return true for "is_rev"
    def test_that_is_rev_on_reverse_card_is_true(self):
        card1 = Card("BLUE", action="REVERSE")
        card2 = Card("RED", action="REVERSE")
        self.assertTrue(card1.is_rev)
        self.assertTrue(card2.is_rev)

    # A Draw four card should have the flag "is_d4" set
    def test_draw_four_card_should_have_is_d4_flag_set(self):
        card1 = Card(wild="WILD_DRAW_FOUR")
        self.assertTrue(card1.is_d4)
