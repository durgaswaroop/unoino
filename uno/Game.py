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
    top_card = None
    is_clockwise = None
    current_player = None
    output_disabled = False
    last_player_decision = None
    next_player = None

    # Game starts with a non-zero set of players and
    def __init__(self, players, deck, disable_output=False):
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
        self.is_clockwise = True
        self.output_disabled = disable_output

        self.setup()

    # Set the game
    def setup(self):
        self.print_player_names()

        # Shuffle deck
        self.shuffled_deck = self.shuffle_deck()

        self.dealer = 0
        self.current_player = self.dealer + 1
        self.distribute_cards()

    # Start the game
    def start(self):
        self.play_turn()
        # self.discard_pile.append(player_card)

    def play_turn(self):
        self.printer('-' * 40)
        current_player = self.players[self.current_player]
        self.printer(f"Current Player : {current_player.name}")

        # Get players decision
        decision = current_player.decide_action(self.top_card)
        self.last_player_decision = decision

        if decision == "PLAY":
            played_card = current_player.play(self.top_card)
            self.printer(f"{current_player.name} played {played_card}")
            self.discard_pile.append(played_card)
            self.top_card = played_card

            # If played card is "skip", update the next player
            if played_card.is_action_card and played_card.action == "SKIP":
                self.next_player = self.get_next_player(with_skip=True)

        else:  # TAKE
            self.printer(f"{current_player.name} will take a card")
            card_to_take = self.shuffled_deck.pop()
            current_player.cards.append(card_to_take)
        self.printer('-' * 40)

    def print_player_names(self):
        player_names = [p.name for p in self.players]
        names_joined = ', '.join(player_names)
        self.printer(f"Players: {names_joined}")

    def shuffle_deck(self):
        # return self.cards
        return random.sample(self.cards, len(self.cards))

    def get_next_player(self, with_skip=False):
        if self.is_clockwise:
            return ((self.current_player + 2) if with_skip
                    else (self.current_player + 1)) % self.num_players
        else:
            return ((self.current_player - 2) if with_skip
                    else (self.current_player - 1)) % (self.num_players)

    def distribute_cards(self):
        self.printer(f"Dealer:  {self.players[self.dealer].name}")
        num_cards_to_distribute = (self.num_players * CARDS_PER_PLAYER)
        cards_to_distribute = self.shuffled_deck[:num_cards_to_distribute]

        self.shuffled_deck = self.shuffled_deck[num_cards_to_distribute:]

        # First Card in the remaining cards starts the discard pile
        top_card_in_deck = self.shuffled_deck.pop()
        self.discard_pile.append(top_card_in_deck)
        self.top_card = top_card_in_deck

        # Shuffled deck will be the rest of the cards
        self.shuffled_deck = self.shuffled_deck[num_cards_to_distribute + 1:]

        for i, player in enumerate(self.players):
            player.cards = cards_to_distribute[i:: self.num_players]

    def printer(self, stuff):
        if not self.output_disabled:
            print(stuff)

# from uno.Player import Player
# from uno.Deck import Deck
#
# game = Game([Player("DSP", []), Player("SPD", [])], Deck().cards)
# game.start()
