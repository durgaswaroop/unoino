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
    def test_deck_should_have_8_cards_of_each_number_in_1_to_9(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numbered_cards = [filter(lambda c: c.number == number, self.cards)
                          for number in numbers
                          ]
        occurrences = [len(list(nc)) for nc in numbered_cards]
        self.assertListEqual(occurrences, [8] * 9)

    # Each color should have 2 cards of numbers 1-9
    def test_deck_should_have_2_cards_of_a_number_in_each_color(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        colors = {"RED", "BLUE", "GREEN", "YELLOW"}
        # Cards of each number are separated
        numbered_cards = [list(filter(lambda c: c.number == number, self.cards))
                          for number in numbers
                          ]

        # From the cards of each number we get its color
        colors_of_each_number \
            = [set(map(lambda c: c.color, nc)) for nc in numbered_cards]
        for c in colors_of_each_number:
            self.assertSetEqual(c, colors)

    # There should be 24 actions cards in the deck
    def test_deck_should_have_24_action_cards(self):
        action_cards = list(filter(lambda c: c.is_action_card, self.cards))
        self.assertEqual(len(action_cards), 24)

    # There should be 8 skip cards in the deck
    def test_deck_should_have_8_skip_cards(self):
        skip_cards = [c for c in self.cards if
                      (c.is_action_card and c.action == "SKIP")]
        self.assertEqual(len(skip_cards), 8)

    # There should be 2 skip cards of each color in the deck
    def test_deck_has_2_skip_cards_of_each_color(self):
        skip_cards = [c for c in self.cards if c.action == "SKIP"]
        colors_of_those = {sc.color for sc in skip_cards}
        self.assertSetEqual(colors_of_those, {"RED", "BLUE", "GREEN", "YELLOW"})

    # There should be 8 Draw Two cards in the deck
    def test_deck_should_have_8_draw_two_cards(self):
        draw_2_cards = [c for c in self.cards if
                        (c.is_action_card and c.action == "DRAW_TWO")]
        self.assertEqual(len(draw_2_cards), 8)

    # There should be 2 Draw Two cards of each color in the deck
    def test_deck_has_2_draw_two_cards_of_each_color(self):
        draw_2_cards = [c for c in self.cards if c.action == "DRAW_TWO"]
        colors_of_those = {dc.color for dc in draw_2_cards}
        self.assertSetEqual(colors_of_those,
                            {"RED", "BLUE", "GREEN", "YELLOW"})

    # There should be 8 Reverse cards in the deck
    def test_deck_should_have_8_reverse_cards(self):
        reverse_cards = [c for c in self.cards if
                         (c.is_action_card and c.action == "REVERSE")]
        self.assertEqual(len(reverse_cards), 8)

    # There should be 2 Reverse cards of each color in the deck
    def test_deck_has_2_reverse_two_cards_of_each_color(self):
        reverse_cards = [c for c in self.cards if c.action == "REVERSE"]
        colors_of_those = {rc.color for rc in reverse_cards}
        self.assertSetEqual(colors_of_those,
                            {"RED", "BLUE", "GREEN", "YELLOW"})

    # There should be 6 actions cards in each color
    def test_deck_has_6_action_cards_in_each_color(self):
        colors = ["RED", "BLUE", "GREEN", "YELLOW"]
        for color in colors:
            cards_of_this_color = [c for c in self.cards if c.color == color]
            action_cards_here = [c for c in cards_of_this_color if
                                 c.is_action_card]
            self.assertEqual(len(action_cards_here), 6)
