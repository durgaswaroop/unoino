from uno.Deck import Deck
from uno.Game import Game
from uno.Player import Player

cards = Deck().cards
players = [Player("DSP", []), Player("SPD", []), Player("NAR", [])]
game = Game(players, cards)
game.start()

print(game.players)
print()
print(game.discard_pile)
