class Game:
    players = None
    cards = None

    # Game starts with a non-zero set of players and
    def __init__(self, players, deck=None):
        if players <= 0:
            raise ValueError(
                f"Can't have a game with {players} Players. Go home.")

        if not deck:
            raise ValueError(f"Can't start a game without a deck of cards")

        self.players = players
        self.cards = deck
