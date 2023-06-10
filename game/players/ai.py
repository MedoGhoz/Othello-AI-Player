from .player import Player

class AI (Player):
    
    def play(self, x = None, y = None):
        self.tree.setCurrentNode(self.tree.minMax())