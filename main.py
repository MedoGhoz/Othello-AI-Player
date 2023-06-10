from game.internals.node import StateNode, Color
from game.internals.tree import StateTree
from game.utils import validMoves, nextStates
from game.players.ai import AI
from game.players.human import Human

if __name__ == "__main__":


  
  tree = StateTree()
  print(tree.root.state)
  # Get coordinates of all possible next moves
  print(validMoves(tree.getCurrentNode()))

  # get black and white score
  print(tree.root.getScore())

  player1 = Human(tree, Color.BLACK)
  player2 = Human(tree, Color.WHITE)
