from uno.GameRules import is_played_card_valid


class Player:
    name = None
    cards = None
    score = None

    def __init__(self, name="", cards=[]):
        self.name = name
        self.cards = cards

    def play(self, topcard):
        valid_cards = [card for card in self.cards
                       if is_played_card_valid(card, topcard)]

        # In descending order
        sorted_by_value = sorted(valid_cards,
                                 key=lambda c: c.value,
                                 reverse=True)
        card_to_play = self.pick_card_to_play(sorted_by_value)

        # Have to say which color this wild card should be
        if card_to_play.is_wild_card:
            card_to_play.color = "RED"

        self.cards.remove(card_to_play)
        return card_to_play

    def pick_card_to_play(self, value_sorted_cards):
        if len(value_sorted_cards) == 1:
            return value_sorted_cards[0]
        else:
            non_d4_cards = [c for c in value_sorted_cards if not c.is_d4]
            return non_d4_cards[0]

    def decide_action(self, top_card):
        """Returns either TAKE or PLAY depending on the cards present"""
        valid_cards = [card for card in self.cards
                       if is_played_card_valid(card, top_card)]

        return "TAKE" if len(valid_cards) == 0 else "PLAY"

    def get_total_value(self):
        return sum([card.value for card in self.cards])

    def __repr__(self):
        return f"Player({self.name}, {self.cards})"
