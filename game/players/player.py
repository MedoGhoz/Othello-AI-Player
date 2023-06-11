from ..internals.tree import StateTree

class Player:
    tree: StateTree
    def __init__(self, tree, color) -> None:
        self.COLOR = color
        self.tree = tree
    
    def play(self, x = None, y = None):
        pass