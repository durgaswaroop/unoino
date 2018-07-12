class Card:
    color = None
    is_number_card = False
    number = None
    is_action_card = False
    action = None
    is_skip = False
    is_d2 = False
    is_d4 = False
    is_rev = False
    is_wild_card = False
    wild = None
    value = None

    def __init__(self, color=None, number=None, action=None, wild=None):
        if not color and not wild:
            raise ValueError("Either 'color' or 'wild' parameters should be"
                             "passed when creating a Card object")

        self.color = color

        if number is not None:  # Explicitly doing this because number can be 0
            self.number = number
            self.is_number_card = True
        elif action:
            self.action = action
            self.is_action_card = True
            if action == "SKIP":
                self.is_skip = True
            elif action == "DRAW_TWO":
                self.is_d2 = True
            else:  # reverse
                self.is_rev = True
        else:  # Wild
            self.wild = wild
            self.is_wild_card = True
            if wild == "WILD_DRAW_FOUR":
                self.is_d4 = True

        self.value = self.card_value()

    def card_value(self):
        if self.is_wild_card:
            return 50
        elif self.is_action_card:
            return 20
        else:
            return self.number

    def __repr__(self):
        if self.wild:
            if self.color:
                return f"Card({self.wild}, {self.color})"
            else:
                return f"Card({self.wild})"
        elif self.action:
            return f"Card({self.color}, {self.action})"
        else:
            return f"Card({self.color}, {self.number})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
