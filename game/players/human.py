from .player import Player
from ..utils import validMoves

class Human (Player):
  
  def play(self, x = None, y = None):
    if [x, y] in validMoves(self.tree.root):
      pass
    else:
      raise ValueError(f"({x}, {y}) is not a valid move")