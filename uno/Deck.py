from uno.Card import Card

FULL_DECK_SIZE = 108


# A deck will have 108 Cards
class Deck:
    cards = None

    # Generates the full deck when the Deck object is created
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        colors = ["RED", "BLUE", "GREEN", "YELLOW"]  # No Pink Ranger :(
        numbers = list(range(10)) + list(range(1, 10))
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        actions = ["SKIP", None, None]

        # cards = [Card(color) for color, number in zip(colors, numbers, actions)]

        # colored_cards = []

        # cards = [Card("") for i in range(FULL_DECK_SIZE)]

        reds = [Card("RED") for _ in range(25)]
        blues = [Card("BLUE") for _ in range(25)]
        greens = [Card("GREEN") for _ in range(25)]
        yellows = [Card("YELLOW") for _ in range(25)]

        # Add numbers
        for i, number in enumerate(numbers):
            reds[i].number = number
            blues[i].number = number
            greens[i].number = number
            yellows[i].number = number

        # Add action cards
        # There will be 6 action cards of each color
        for i in range(len(reds) - 1, len(reds) - 7, -1):
            reds[i].is_action_card = True
            blues[i].is_action_card = True
            greens[i].is_action_card = True
            yellows[i].is_action_card = True

        for colored_cards in [reds, blues, greens, yellows]:
            colored_cards[19].action = "SKIP"
            colored_cards[20].action = "SKIP"
            colored_cards[21].action = "DRAW_TWO"
            colored_cards[22].action = "DRAW_TWO"
            colored_cards[23].action = "REVERSE"
            colored_cards[24].action = "REVERSE"

        others = [Card("")] * (FULL_DECK_SIZE - 25 * 4)
        return reds + blues + greens + yellows + others

# cards = Deck().cards
