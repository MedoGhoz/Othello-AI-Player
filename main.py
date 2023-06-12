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

  # print("herere", game.getCurrentNode().state)
  # Get coordinates of all possible next moves

  difficulty = 2
  player2 = AI(game, Color.WHITE, 1)

  player1 = AI(game, Color.BLACK, 3)


  # player1 = Human(game, Color.BLACK)
  # player2 = Human(game, Color.WHITE)
  wasAvailablePrevTurn = False

  while True: 
    print("----------------------------------\n")
    # current state with next moves
    currentStateWithNextMoves = availableMoves(game.getCurrentNode().state, player1.COLOR.value, player2.COLOR.value)['state']

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in currentStateWithNextMoves]))
    
    # get black and white score
    currentScore = game.getCurrentNode().getScore()
    print("Current Score", currentScore)

    # Get current State (with possible moves)
    print("current moves", availableMoves(game.getCurrentNode().state, player1.COLOR.value, player2.COLOR.value)['validMoves'])
    # Get next possible moves
    ##
    ## function used to print current moves and next possible moves
    moves = availableMoves(game.getCurrentNode().state, player1.COLOR.value, player2.COLOR.value)['validMoves']
    if len(moves) != 0:
      if isinstance(player1, Human):
        x = int(input("X Move: "))
        y = int(input("Y Move: "))
        # if available moves
        player1.play(x, y)
      else:
        player1.play()

    if wasAvailablePrevTurn == 0 and len(moves) == 0:
      print("GAME IS OVER")
      break
    wasAvailablePrevTurn = len(moves)
    player1, player2 = player2, player1
