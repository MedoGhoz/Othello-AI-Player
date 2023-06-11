from internals.node import StateNode
from players.moves import availableMoves
from players.moves import updateState
from players.moves import printState
from copy import copy, deepcopy

def validMoves(state: StateNode, playerNum, opponentNum):
    nextState = availableMoves(state.state, playerNum, opponentNum)
    return nextState["validMoves"]

def nextStates(state: StateNode, playerNum, opponentNum):
    loopingState = deepcopy(state)
    states = []
    nextState = availableMoves(state.state, playerNum, opponentNum)
    for move in nextState["validMoves"]:
        loopingState = deepcopy(state)
        node = StateNode()
        node.state = updateState(loopingState.state, move[0], move[1], playerNum, opponentNum)
        states.append(node)
    return states

def expand(state: StateNode, playerNum, opponentNum, depth):
    # if(depth == 0):
    #     return
    # children = nextStates(state, playerNum, opponentNum)
    # # print(children)
    # for child in children:
    #     state.addChild(child)
    # for child in newState.getChildren():
    #     expand(child, opponentNum, playerNum, depth - 1)
    statesQueue = []
    statesQueue.append(state)
    i = 0
    while(len(statesQueue) != 0 and i < depth):
        currentState = statesQueue.pop(0)
        children = nextStates(state, playerNum, opponentNum)
        print(currentState)
        print(children)
        for child in children:
            currentState.addChild(child)
            statesQueue.append(child)
        i += 1   
    return state

# state = StateNode()
# state.state =[  [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 2, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 2, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#             ]
# print(validMoves(state, 1, 2))
# tree = expand(state, 1, 2, 0)
# print(tree.getChildren())
# printState(tree.getChildren())
# for child in tree.getChildren():
#     printState(child.state)