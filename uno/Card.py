class Card:
    color = None
    number = None
    is_action_card = False
    action = None
    is_wild_card = False
    wild = None

    def __init__(self, color=None, number=None, action=None, wild=None):
        self.color = color
        self.number = number
        if action:  # If an action has been passed, set the action flag
            self.action = action
            self.is_action_card = True
        if wild:
            self.wild = wild
            self.is_wild_card = True

    def __repr__(self):
        return f"Card({self.color}, {self.number}, {self.is_action_card})"
