class Game:
    players = None

    # Game starts with a non-zero set of players and
    def __init__(self, players):
        if players <= 0:
            raise ValueError(f"Can't have a game with {players} Players. Go home.")
        self.players = players