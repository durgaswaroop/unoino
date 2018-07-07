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
