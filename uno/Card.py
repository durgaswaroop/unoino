class Card:
    color = None
    number = None  # Start with -100 as the default is already 0
    is_action_card = None
    action = None

    def __init__(self, color):
        self.color = color
        # self.number = number

    def __repr__(self):
        return f"Card({self.color}, {self.number}, {self.is_action_card})"
