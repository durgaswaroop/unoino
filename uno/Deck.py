from uno.Card import Card
import itertools

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

        # Generate all combinations of colors and numbers
        numbered_cards = [Card(col, num) for col, num in
                          itertools.product(colors, numbers)]

        # Twice because each action is present twice in a color
        actions = ["SKIP", "DRAW_TWO", "REVERSE"] * 2

        action_cards = [Card(col, action=action) for col, action in
                        itertools.product(colors, actions)]

        regular_wild_cards = [Card(wild="WILD")] * 4
        wild_draw_4_cards = [Card(wild="WILD_DRAW_FOUR")] * 4

        return numbered_cards + action_cards + regular_wild_cards + wild_draw_4_cards

# cards = Deck().cards
