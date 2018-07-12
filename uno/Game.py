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
    status = None
    winner = None

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
        # for i in range(20):
        self.play_turn()
        self.current_player = self.get_next_player()
        # self.discard_pile.append(player_card)

    def play_turn(self):
        self.printer('-' * 40)
        current_player = self.players[self.current_player]
        self.printer(f"Current Player : {current_player.name}")
        self.printer(f"Top card : {self.top_card}")

        # If the current top card is either a +2 or +4 and the last player
        # decision was PLAY, it means that the current player has to pick either
        # two or 4 cards
        if self.last_player_decision == "PLAY" and (
                self.top_card.is_d2 or self.top_card.is_d4):
            if self.top_card.is_d2:
                [current_player.cards.append(self.shuffled_deck.pop())
                 for _ in range(2)]
                self.printer(f"{current_player.name} took 2 cards")
            else:
                [current_player.cards.append(self.shuffled_deck.pop())
                 for _ in range(4)]
                self.printer(f"{current_player.name} took 4 cards")
            self.last_player_decision = "TAKE"
            self.printer('-' * 40)
            return

            # Get players decision
        decision = current_player.decide_action(self.top_card)
        self.last_player_decision = decision

        if decision == "PLAY":
            played_card = current_player.play(self.top_card)
            self.printer(f"{current_player.name} played {played_card}, "
                         f"{len(current_player.cards)}")
            self.discard_pile.append(played_card)
            self.top_card = played_card

            if played_card.is_skip:
                # If played card is "skip", update the next player
                self.next_player = self.get_next_player(with_skip=True)
            elif played_card.is_rev:
                # If reverse, change direction and update next player
                self.is_clockwise = not self.is_clockwise
                self.next_player = self.get_next_player()
            elif played_card.is_wild_card and played_card.wild == "WILD":
                self.next_player = self.get_next_player()

            if len(current_player.cards) == 0:
                self.status = "GAMEOVER"
                self.winner = self.current_player
                self.players[
                    self.current_player].score = self.get_current_player_score()
        else:  # TAKE
            self.printer(f"{current_player.name} will take a card")
            card_to_take = self.shuffled_deck.pop()
            current_player.cards.append(card_to_take)
        self.printer('-' * 40)

    def get_current_player_score(self):
        other_players = [p for i, p in enumerate(self.players) if
                         i != self.current_player]
        other_players_values = [p.get_total_value() for p in other_players]
        return sum(other_players_values)
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
# from uno.Card import Card
# from uno.Deck import Deck
#
# deck = Deck().cards
# game = Game([Player("DSP", []), Player("SPD", [])], Deck().cards)
# game.start()
