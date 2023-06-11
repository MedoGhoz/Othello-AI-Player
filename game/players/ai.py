from .player import Player
from .minimax import minimax
from ..utils import expand
from ..internals.node import Color

class AI (Player):
    def __init__(self, game, color, depth) -> None:
        self.depth = depth
        super().__init__(game, color)
    def play(self, x = None, y = None):
        opponent = Color.WHITE.value if self.COLOR == Color.BLACK else Color.BLACK.value

        expandedNode = expand(self.game.getCurrentNode(), self.COLOR.value, opponent, self.depth)
        bestNode = minimax(expandedNode)
        self.game.setCurrentNode(bestNode)
        