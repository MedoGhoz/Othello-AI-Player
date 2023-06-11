from .player import Player
from .moves import availableMoves, updateState
from ..internals.node import Color

class Human (Player):
  
  def play(self, x = None, y = None):
    opponent = Color.WHITE.value if self.COLOR == Color.BLACK else Color.BLACK.value
    print(opponent)
    moves = availableMoves(self.game.getCurrentNode().state, self.COLOR.value, opponent)
    if (x, y) in moves['validMoves']:
      self.game.setCurrentState(updateState(self.game.getCurrentNode().state, x, y, self.COLOR.value, opponent))
    else:
      raise ValueError(f"({x}, {y}) is not a valid move")