import unittest
from uno.Deck import Deck
from uno.Card import Card

FULL_DECK_SIZE = 108


class TestDeck(unittest.TestCase):
    game_deck = Deck()
    cards = game_deck.cards

    # Deck should have 108 cards
    def test_deck_should_have_all_cards(self):
        self.assertEqual(FULL_DECK_SIZE, len(self.cards))

    # Deck should be a list
    def test_deck_should_be_a_list(self):
        self.assertIsInstance(self.cards, list)

    # Any instance of the Deck should be a card
    def test_each_deck_instance_should_be_a_card(self):
        from random import randrange
        random_number = randrange(0, FULL_DECK_SIZE)
        self.assertIsInstance(self.cards[random_number], Card)

    # There should be 25 red cards
    def test_deck_has_25_red_card(self):
        reds = list(filter(lambda card: card.color == "RED", self.cards))
        self.assertEqual(len(reds), 25)

    # There should be 25 blue cards
    def test_deck_has_25_blue_card(self):
        blues = list(filter(lambda card: card.color == "BLUE", self.cards))
        self.assertEqual(len(blues), 25)

    # There should be 25 green cards
    def test_deck_has_25_green_card(self):
        greens = list(filter(lambda card: card.color == "GREEN", self.cards))
        self.assertEqual(len(greens), 25)

    # There should be 25 yellow cards
    def test_deck_has_25_yellow_card(self):
        yellows = list(filter(lambda card: card.color == "YELLOW", self.cards))
        self.assertEqual(len(yellows), 25)

    # There should be 4 Zero cards
    def test_deck_has_4_zero_Cards(self):
        zero_cards = list(filter(lambda card: card.number == 0, self.cards))
        self.assertEqual(len(zero_cards), 4)

    # All the 4 zero cards should be of different colors
    def test_deck_zero_cards_should_be_of_4_different_colors(self):
        zero_cards = list(filter(lambda card: card.number == 0, self.cards))
        colors = {card.color for card in zero_cards}
        self.assertEqual(colors, {"RED", "BLUE", "GREEN", "YELLOW"})

    # There should be 8 cards each of numbers 1-9
    def test_deck_should_have_2_cards_of_each_number_in_1_to_9(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numbered_cards = [filter(lambda c: c.number == number, self.cards)
                          for number in numbers
                          ]
        occurrences = [len(list(nc)) for nc in numbered_cards]
        self.assertListEqual(occurrences, [8] * 9)
