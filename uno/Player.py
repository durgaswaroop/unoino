from uno.GameRules import is_played_card_valid


class Player:
    name = None
    cards = None

    def __init__(self, name="", cards=[]):
        self.name = name
        self.cards = cards

    def play(self, topcard):
        valid_cards = [card for card in self.cards
                       if is_played_card_valid(card, topcard)]
        card_to_play = valid_cards[0]

        # Have to say which color this wild card should be
        if card_to_play.is_wild_card:
            card_to_play.color = "RED"

        self.cards.remove(card_to_play)
        return card_to_play

    def decide_action(self, top_card):
        """Returns either TAKE or PLAY depending on the cards present"""
        valid_cards = [card for card in self.cards
                       if is_played_card_valid(card, top_card)]

        return "TAKE" if len(valid_cards) == 0 else "PLAY"

    def __repr__(self):
        return f"Player({self.name}, {self.cards})"
