from .node import StateNode, Color
class Game:
  root = None

  def __init__(self): 
    self.root = StateNode()

    pass

  def getCurrentNode(self):
    return self.root

  def setCurrentNode(self, node):
    self.root = node

  def setCurrentState(self, state):
      self.root.state = state
      self.root.children = []