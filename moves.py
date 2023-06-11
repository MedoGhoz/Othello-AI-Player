#state is a 2d list that represents the board
# 0 => empty
# 1 => black
# 2 => white
# 3 => possible move for black
# 4 => possible move for white

state = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
        ]
#function takes the state of the board and the player context
#returns a new list representing possible moves for this specific player
def availableMoves(state, playerNum, opponentNum):
    #the coordinates used to loop through player pieces to find the possible moves for each one
    x = 0
    y = 0
    for row in state:
        y = 0
        for cell in row:
            if (cell == playerNum):
                # check for moves to the right
                i = x
                j = y
                while(j < 6 and state[i][j + 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i][j + 1] == 0):
                        state[i][j + 1] = playerNum + 2                    
                    j +=1
                if(state[i][j] == opponentNum and state[i][j + 1] == 0):
                    state[i][j + 1] = playerNum + 2
                # check for moves to the left
                i = x
                j = y
                while(j > 1 and state[i][j - 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i][j -1] == 0):
                        state[i][j - 1] = playerNum + 2                    
                    j -=1
                if(state[i][j] == opponentNum and state[i][j - 1] == 0):
                    state[i][j - 1] = playerNum + 2
                # check for moves upwards
                i = x
                j = y
                while(i > 1 and state[i - 1][j] != playerNum):
                    if(state[i][j] == opponentNum and state[i - 1][j] == 0):
                        state[i - 1][j] = playerNum + 2                    
                    i -=1
                if(state[i][j] == opponentNum and state[i - 1][j] == 0):
                    state[i - 1][j] = playerNum + 2
                # check for moves downwards
                i = x
                j = y
                while(i < 6 and state[i + 1][j] != playerNum):
                    if(state[i][j] == opponentNum and state[i + 1][j] == 0):
                        state[i + 1][j] = playerNum + 2                    
                    i +=1
                if(state[i][j] == opponentNum and state[i + 1][j] == 0):
                    state[i + 1][j] = playerNum + 2
                # check for moves right-up diagonally
                i = x
                j = y
                while(i > 1 and j < 6 and state[i - 1][j + 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i - 1][j + 1] == 0):
                        state[i - 1][j + 1] = playerNum + 2                    
                    i -=1
                    j +=1
                if(state[i][j] == opponentNum and state[i - 1][j + 1] == 0):
                    state[i - 1][j + 1] = playerNum + 2
                # check for moves right-down diagonally
                i = x
                j = y
                while(i < 6 and j < 6 and state[i + 1][j + 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i + 1][j + 1] == 0):
                        state[i + 1][j + 1] = playerNum + 2                    
                    i +=1
                    j +=1
                if(state[i][j] == opponentNum and state[i + 1][j + 1] == 0):
                    state[i + 1][j + 1] = playerNum + 2
                # check for moves left-up diagonally
                i = x
                j = y
                while(i > 1 and j > 1 and state[i - 1][j - 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i - 1][j - 1] == 0):
                        state[i - 1][j - 1] = playerNum + 2                    
                    i -=1
                    j -=1
                if(state[i][j] == opponentNum and state[i - 1][j - 1] == 0):
                    state[i - 1][j - 1] = playerNum + 2
                # check for moves left-down diagonally
                i = x
                j = y
                while(i < 6 and j > 1 and state[i + 1][j - 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i + 1][j - 1] == 0):
                        state[i + 1][j - 1] = playerNum + 2                    
                    i +=1
                    j -=1
                if(state[i][j] == opponentNum and state[i + 1][j - 1] == 0):
                    state[i + 1][j - 1] = playerNum + 2
            y += 1
        x += 1
    return state


def printState(state):
    line = ""
    for row in state:
        for col in row:
            line += str(col) + " "
        line += "\n"
    print(line)

printState(state)
state = availableMoves(state, playerNum=1, opponentNum=2)
printState(state)