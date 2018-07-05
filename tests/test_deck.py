import unittest
from uno.Deck import Deck
from uno.Card import Card

FULL_DECK_SIZE = 108


class TestDeck(unittest.TestCase):
    game_deck = Deck()

    # Deck should have 108 cards
    def test_deck_should_have_all_cards(self):
        self.assertEqual(FULL_DECK_SIZE, len(self.game_deck.cards))

    # Deck should be a list
    def test_deck_should_be_a_list(self):
        self.assertIsInstance(self.game_deck.cards, list)

    # Any instance of the Deck should be a card
    def test_each_deck_instance_should_be_a_card(self):
        from random import randrange
        random_number = randrange(0, FULL_DECK_SIZE)
        self.assertIsInstance(self.game_deck.cards[random_number], Card)

    # There should be 25 red cards
    def test_deck_has_25_red_card(self):
        cards = self.game_deck.cards
        red_cards = list(filter(lambda card: card.color == "RED", cards))
        self.assertEqual(len(red_cards), 25)

    # There should be 25 blue cards
    def test_deck_has_25_blue_card(self):
        cards = self.game_deck.cards
        blue_cards = list(filter(lambda card: card.color == "BLUE", cards))
        self.assertEqual(len(blue_cards), 25)

    # There should be 25 green cards
    def test_deck_has_25_green_card(self):
        cards = self.game_deck.cards
        green_cards = list(filter(lambda card: card.color == "GREEN", cards))
        self.assertEqual(len(green_cards), 25)

    # There should be 25 yellow cards
    def test_deck_has_25_yellow_card(self):
        cards = self.game_deck.cards
        yellow_cards = list(filter(lambda card: card.color == "YELLOW", cards))
        self.assertEqual(len(yellow_cards), 25)
