from ..internals.game import Game

class Player:
    game: Game
    def __init__(self, game, color) -> None:
        self.COLOR = color
        self.game = game
    
    def play(self, x = None, y = None):
        pass