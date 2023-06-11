import enum

BOARDSIZE = 8

class Color(enum.Enum): 
  EMPTY = 0
  BLACK = 1
  WHITE = 2
  POSSIBLE = 3

class StateNode:
  state = None
  heuristic = None
  children = []
  def __init__(self, state = None) -> None:
    self.children = []
    if (state): 
      self.state = state
    else:
      self.state = [([Color.EMPTY.value] * BOARDSIZE).copy() for i in range(BOARDSIZE)]
      self.state[3][3] = Color.WHITE.value
      self.state[3][4] = Color.BLACK.value
      self.state[4][3] = Color.BLACK.value
      self.state[4][4] = Color.WHITE.value

  def setHeuristic(self, val): 
    self.heuristic = val
  
  def getHeuristic(self):
    return self.heuristic
  
  def addChild(self, child):
    self.children.append(child)

  def getChildren(self):
    return self.children
  
  def getScore(self):
    black = 0
    white = 0

    for i in range(8):
      for j in range(8):
        if (self.state[i][j] == Color.BLACK.value):
          black += 1
        elif (self.state[i][j] == Color.WHITE.value):
          white += 1
    return [black, white]