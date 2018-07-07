import random


# A Game needs Players and a Deck of cards
class Game:
    players = None
    cards = None
    shuffled_deck = None

    # Game starts with a non-zero set of players and
    def __init__(self, players, deck):
        if len(players) < 2:
            raise ValueError(
                f"Can't have a game with {len(players)} Players. Minimum is 2."
                f"Go home.")

        if not deck:
            raise ValueError("Can't start a game without a deck of cards")

        self.players = players
        self.cards = deck

    # Start the game
    def start(self):
        # Print players
        player_names = [p.name for p in self.players]
        names_joined = ', '.join(player_names)
        print(f"Players: {names_joined}")

        # Shuffle deck
        self.shuffled_deck = self.shuffle_deck()

    def shuffle_deck(self):
        return random.sample(self.cards, len(self.cards))
