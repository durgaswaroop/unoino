import os
import sys

module_path = os.path.abspath(os.getcwd())
sys.path.append(module_path)

from uno.Game import Game
from uno.Deck import Deck
from uno.Player import Player

cards = Deck().cards
# cards = [Card("RED", 5), Card("RED", 5), Card("RED", 5), Card("RED", 5),
#          Card("RED", 5), Card("RED", 5), Card("RED", 5), Card("RED", 5),
#          Card("RED", 5), Card("RED", 5), Card("RED", 5), Card("RED", 5),
#          Card("RED", 5), Card("RED", 5), Card("BLUE", 4)]
players = [Player("DSP", []), Player("SPD", [])]

# with mock.patch.object(Game, "shuffle_deck") as mock_shuffle:
#     mock_shuffle.return_value = cards
#     game = Game(players, cards)

game = Game(players, cards)

print(players[1].cards)
print(game.top_card)

game.start()
