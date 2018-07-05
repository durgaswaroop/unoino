import unittest
from uno.Deck import Deck
from uno.Card import Card

FULL_DECK_SIZE = 108


class TestDeck(unittest.TestCase):
    game_deck = Deck()

    # Deck should have 108 cards
    def test_deck_should_have_all_cards(self):
        self.assertEqual(FULL_DECK_SIZE, len(self.game_deck.deck))

    # Deck should be a list
    def test_deck_should_be_a_list(self):
        self.assertIsInstance(self.game_deck.deck, list)

    # Any instance of the Deck should be a card
    def test_each_deck_instance_should_be_a_card(self):
        from random import randrange
        random_number = randrange(0, FULL_DECK_SIZE)
        self.assertIsInstance(self.game_deck.deck[random_number], Card)
