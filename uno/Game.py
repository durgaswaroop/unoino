import random

CARDS_PER_PLAYER = 7


# A Game needs Players and a Deck of cards
class Game:
    players = None
    cards = None
    shuffled_deck = None
    num_players = None
    discard_pile = None
    dealer = None

    # Game starts with a non-zero set of players and
    def __init__(self, players, deck):
        if len(players) < 2 or len(players) > 10:
            raise ValueError(
                f"Can't have a game with {len(players)} Players. "
                f"Number of Players should be in 2 - 10. Go home.")

        if not deck:
            raise ValueError("Can't start a game without a deck of cards")

        self.players = players
        self.num_players = len(players)
        self.cards = deck
        self.discard_pile = []

    # Start the game
    def start(self):
        self.print_player_names()

        # Shuffle deck
        self.shuffled_deck = self.shuffle_deck()

        self.dealer = 0
        self.distribute_cards()

    def print_player_names(self):
        player_names = [p.name for p in self.players]
        names_joined = ', '.join(player_names)
        print(f"Players: {names_joined}")

    def shuffle_deck(self):
        return random.sample(self.cards, len(self.cards))

    def distribute_cards(self):
        print(f"Player {self.dealer} is the dealer")
        num_cards_to_distribute = (self.num_players * CARDS_PER_PLAYER)
        cards_to_distribute = self.shuffled_deck[:num_cards_to_distribute]

        # First Card in the remaining cards starts the discard pile
        self.discard_pile.append(self.shuffled_deck[num_cards_to_distribute])

        # Shuffled deck will be the rest of the cards
        self.shuffled_deck = self.shuffled_deck[num_cards_to_distribute + 1:]

        for i, player in enumerate(self.players):
            player.cards = cards_to_distribute[i:: self.num_players]

# from uno.Player import Player
# from uno.Deck import Deck
#
# game = Game([Player("DSP", []), Player("SPD", [])], Deck().cards)
# game.start()
