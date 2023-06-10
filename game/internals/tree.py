from .node import StateNode, Color
class StateTree:
  root = None

  def __init__(self): 
    self.root = StateNode()

    pass

  def getCurrentNode(self):
    return self.root

  def setCurrentNode(self, node):
    self.root = node

  def expand(self, node, depth):
    pass

  def minMax(self):
    pass
  