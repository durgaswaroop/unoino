from uno.Card import Card

FULL_DECK_SIZE = 108


# A deck will have 108 Cards
class Deck:
    cards = None

    # Generates the full deck when the Deck object is created
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        # colors = ["RED", "BLUE", "GREEN", "YELLOW"]  # No Pink Ranger :(
        numbers = list(range(10)) + list(range(1, 10))
        # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # cards = [Card(color, number) for color, number in zip(colors, numbers)]

        # colored_cards = []

        # cards = [Card("") for i in range(FULL_DECK_SIZE)]

        reds = [Card("RED") for i in range(25)]
        blues = [Card("BLUE") for i in range(25)]
        greens = [Card("GREEN") for i in range(25)]
        yellows = [Card("YELLOW") for i in range(25)]

        # Add zero card to all the four colored sets
        for unicolored_cards in [reds, blues, greens, yellows]:
            unicolored_cards[0].number = 0

        # Add numbers
        for id, number in enumerate(numbers):
            reds[id].number = number
            blues[id].number = number
            greens[id].number = number
            yellows[id].number = number

        others = [Card("")] * (FULL_DECK_SIZE - 25 * 4)
        return reds + blues + greens + yellows + others

# cards = Deck().cards
