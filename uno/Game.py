# A Game needs Players and a Deck of cards
class Game:
    players = None
    cards = None

    # Game starts with a non-zero set of players and
    def __init__(self, players, deck):
        if not players:
            raise ValueError("Can't have a game with no Players. Go home.")

        if not deck:
            raise ValueError("Can't start a game without a deck of cards")

        self.players = players
        self.cards = deck
