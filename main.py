from game.internals.node import StateNode, Color
from game.internals.game import Game
from game.players.ai import AI
from game.players.human import Human
from game.players.moves import availableMoves


def driver(color, row = None, col = None):
  if player1.COLOR.value == color:
    player1.play(x, y)
  else:
    player2.play(x, y)

if __name__ == "__main__":

  
  game = Game()
  print(game.getCurrentNode())
  # Get coordinates of all possible next moves

  difficulty = 214

  player1 = Human(game, Color.BLACK)
  # player1 = AI(game, Color.BLACK, difficulty)
  player2 = Human(game, Color.WHITE)

  while True: 
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in game.getCurrentNode().state]))
    # get black and white score
    print("Current Score", game.getCurrentNode().getScore())

    # Get current State (with possible moves)
    print("current moves", availableMoves(game.getCurrentNode().state, player1.COLOR.value, player2.COLOR.value)['state'])
    # Get next possible moves
    print("current moves", availableMoves(game.getCurrentNode().state, player1.COLOR.value, player2.COLOR.value)['validMoves'])

    x = int(input("X Move: "))
    y = int(input("Y Move: "))
    player1.play(x, y)
    player1, player2 = player2, player1
