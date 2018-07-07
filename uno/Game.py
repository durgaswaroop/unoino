# A Game needs Players and a Deck of cards
class Game:
    players = None
    cards = None

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
