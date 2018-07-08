### Rules
# 1. Cards colors should match
# OR
# 2. Cards numbers should match
# OR
# 3. For actions cards:
#  -> SKIP: Any skip card or any card of that color
#  -> REVERSE: ANy reverse or anny card of that color
#  -> DRAW_TWO: (Assuming somebody already picked up the two cards) -
#   Other Draw two's or any card of that color
#
# For the first card after the cards are dealt
# 1. If it's a WILD_DRAW_FOUR, the card is placed at the back of the pile and
# a new card is taken
# 2. If it's a wild card, the first player picks the color and plays
# 3. If it's a DRAW_TWO card, first players draws two cards and their turn is skipped
# 4. If it's a reverse card, dealer goes first


# Checks if the played card is valid for the given top card
def is_played_card_valid(played_card, top_card):
    if played_card.is_wild_card:
        return True

    # Match two wild cards if they are the same wild
    if (played_card.is_wild_card and top_card.is_wild_card
            and played_card.wild == top_card.wild):
        return True

    # Match two action cards if they are the same action
    if (played_card.is_action_card and top_card.is_action_card
            and played_card.action == top_card.action):
        return True

    # Match the same numbered cards if they are the same number
    if (played_card.is_number_card and top_card.is_number_card
            and played_card.number == top_card.number):
        return True

    # Match two cards if they've the same color
    if (played_card.color and top_card.color
            and played_card.color == top_card.color):  # Same colors are ok
        return True

    return False
