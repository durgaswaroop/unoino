from uno.Card import Card

FULL_DECK_SIZE = 108


# A deck will have 108 Cards
class Deck:
    cards = None

    # Generates the full deck when the Deck object is created
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        reds = [Card("RED")] * 25
        blues = [Card("BLUE")] * 25
        greens = [Card("GREEN")] * 25
        yellows = [Card("YELLOW")] * 25
        others = [Card("")] * (FULL_DECK_SIZE - 25 * 4)
        return reds + blues + greens + yellows + others
