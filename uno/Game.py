import random

CARDS_PER_PLAYER = 7


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

        self.distribute_cards()

    def shuffle_deck(self):
        return random.sample(self.cards, len(self.cards))

    def distribute_cards(self):
        num_players = len(self.players)
        cards_to_distribute = \
            self.shuffled_deck[:(num_players * CARDS_PER_PLAYER)]

        for i, player in enumerate(self.players):
            player.cards = cards_to_distribute[i:: num_players]


# from uno.Player import Player
# from uno.Deck import Deck
#
# game = Game([Player("DSP", []), Player("SPD", [])], Deck().cards)
# game.start()