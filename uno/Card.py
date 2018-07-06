class Card:
    color = None
    number = None
    is_action_card = False
    action = None
    is_wild_card = False
    wild = None

    def __init__(self, color=None, number=None, action=None, wild=None):
        if not color and not wild:
            raise ValueError("Either 'color' or 'wild' parameters should be"
                             "passed when creating a Card object")

        self.color = color
        self.number = number
        if action:  # If an action has been passed, set the action flag
            self.action = action
            self.is_action_card = True
        if wild:
            self.wild = wild
            self.is_wild_card = True

    def __repr__(self):
        if self.wild:
            return f"Card({self.wild})"
        elif self.action:
            return f"Card({self.color}, {self.action})"
        else:
            return f"Card({self.color}, {self.number})"
