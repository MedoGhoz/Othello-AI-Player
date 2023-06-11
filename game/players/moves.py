from copy import copy, deepcopy

#state is a 2d list that represents the board
# 0 => empty
# 1 => black
# 2 => white
# 3 => possible move

state = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 3, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 2, 3, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
        ]
#function takes the state of the board and the player context
#returns a new list representing possible moves for this specific player
def availableMoves(state, playerNum, opponentNum):
    state = deepcopy(state)
    #dictionary that containes the new state with possible moves and the indecies of these moves
    newState = {}
    #list of the indecies of possible moves
    validMoves = []
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
                        state[i][j + 1] = 3                  
                        validMoves.append((i, j + 1))
                    j +=1
                if(state[i][j] == opponentNum and state[i][j + 1] == 0):
                    state[i][j + 1] = 3
                    validMoves.append((i, j + 1))
                # check for moves to the left
                i = x
                j = y
                while(j > 1 and state[i][j - 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i][j -1] == 0):
                        state[i][j - 1] = 3
                        validMoves.append((i, j - 1))
                    j -=1
                if(state[i][j] == opponentNum and state[i][j - 1] == 0):
                    state[i][j - 1] = 3
                    validMoves.append((i, j - 1))
                # check for moves upwards
                i = x
                j = y
                while(i > 1 and state[i - 1][j] != playerNum):
                    if(state[i][j] == opponentNum and state[i - 1][j] == 0):
                        state[i - 1][j] = 3
                        validMoves.append((i - 1, j))
                    i -=1
                if(state[i][j] == opponentNum and state[i - 1][j] == 0):
                    state[i - 1][j] = 3
                    validMoves.append((i - 1, j))
                # check for moves downwards
                i = x
                j = y
                while(i < 6 and state[i + 1][j] != playerNum):
                    if(state[i][j] == opponentNum and state[i + 1][j] == 0):
                        state[i + 1][j] = 3
                        validMoves.append((i + 1, j))
                    i +=1
                if(state[i][j] == opponentNum and state[i + 1][j] == 0):
                    state[i + 1][j] = 3
                    validMoves.append((i + 1, j))
                # check for moves right-up diagonally
                i = x
                j = y
                while(i > 1 and j < 6 and state[i - 1][j + 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i - 1][j + 1] == 0):
                        state[i - 1][j + 1] = 3
                        validMoves.append((i - 1, j + 1))
                    i -=1
                    j +=1
                if(state[i][j] == opponentNum and state[i - 1][j + 1] == 0):
                    state[i - 1][j + 1] = 3
                    validMoves.append((i - 1, j + 1))
                # check for moves right-down diagonally
                i = x
                j = y
                while(i < 6 and j < 6 and state[i + 1][j + 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i + 1][j + 1] == 0):
                        state[i + 1][j + 1] = 3
                        validMoves.append((i + 1, j + 1))
                    i +=1
                    j +=1
                if(state[i][j] == opponentNum and state[i + 1][j + 1] == 0):
                    state[i + 1][j + 1] = 3
                    validMoves.append((i + 1, j + 1))
                # check for moves left-up diagonally
                i = x
                j = y
                while(i > 1 and j > 1 and state[i - 1][j - 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i - 1][j - 1] == 0):
                        state[i - 1][j - 1] = 3
                        validMoves.append((i - 1, j - 1))
                    i -=1
                    j -=1
                if(state[i][j] == opponentNum and state[i - 1][j - 1] == 0):
                    state[i - 1][j - 1] = 3
                    validMoves.append((i - 1, j - 1))
                # check for moves left-down diagonally
                i = x
                j = y
                while(i < 6 and j > 1 and state[i + 1][j - 1] != playerNum):
                    if(state[i][j] == opponentNum and state[i + 1][j - 1] == 0):
                        state[i + 1][j - 1] = 3
                        validMoves.append((i + 1, j - 1))
                    i +=1
                    j -=1
                if(state[i][j] == opponentNum and state[i + 1][j - 1] == 0):
                    state[i + 1][j - 1] = 3
                    validMoves.append((i + 1, j - 1))
            y += 1
        x += 1
        newState["state"] = state
        newState["validMoves"] = validMoves
    return newState


def updateState(state, x, y, playerNum, opponentNum):
    state[x][y] = playerNum
    newState = deepcopy(state)
    i = x
    j = y
    while(i < 7 and state[i + 1][j] == opponentNum):
        newState[i + 1][j] = playerNum
        i += 1
    if(i < 7 and newState[i + 1][j] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(i > 1 and state[i - 1][j] == opponentNum):
        newState[i - 1][j] = playerNum
        i -= 1
    if(i > 1 and newState[i - 1][j] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(j < 7 and state[i][j + 1] == opponentNum):
        newState[i][j + 1] = playerNum
        j += 1
    if(j < 7 and newState[i][j + 1] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(j > 1 and state[i][j - 1] == opponentNum):
        newState[i][j - 1] = playerNum
        j -= 1
    if(j > 1 and newState[i][j - 1] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(i < 7 and j < 7 and state[i + 1][j + 1] == opponentNum):
        newState[i + 1][j + 1] = playerNum
        i += 1
        j += 1
    if(i < 7 and j < 7 and newState[i + 1][j + 1] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(i < 7 and j > 1 and state[i + 1][j - 1] == opponentNum):
        newState[i + 1][j - 1] = playerNum
        i += 1
        j -= 1
    if(i < 7 and j > 1 and newState[i + 1][j - 1] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(i > 1 and j < 7 and state[i - 1][j + 1] == opponentNum):
        newState[i - 1][j + 1] = playerNum
        i -= 1
        j += 1
    if(i > 1 and j < 7 and newState[i - 1][j + 1] == playerNum):
        state = deepcopy(newState)

    i = x
    j = y
    newState = deepcopy(state)

    while(i > 1 and j > 1 and state[i - 1][j - 1] == opponentNum):
        newState[i - 1][j - 1] = playerNum
        i -= 1
        j -= 1
    if(i > 1 and j > 1 and newState[i - 1][j - 1] == playerNum):
        state = deepcopy(newState)

    return state


def printState(state):
    line = ""
    for row in state:
        for col in row:
            line += str(col) + " "
        line += "\n"
    print(line)

# printState(state)
# state = availableMoves(state, playerNum=2, opponentNum=1)
# newstate = updateState(state, 4, 2, 2, 1)
# printState(state["state"])
# printState(newstate)
# print(state["validMoves"])
