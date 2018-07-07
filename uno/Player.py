class Player:
    name = None
    cards = None

    def __init__(self, name="", cards=[]):
        self.name = name
        self.cards = cards

    def play(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Player({self.name}, {self.cards})"
