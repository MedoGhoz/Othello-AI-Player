from .internals.node import StateNode
from .players.moves import availableMoves
from .players.moves import updateState
from .players.moves import printState
from .players.minimax import minimax
from .players.Heuristics import total_heuristic
from copy import deepcopy


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
        node.state = updateState(
            loopingState.state, move[0], move[1], playerNum, opponentNum
        )
        states.append(node)
    return states


def expand(state: StateNode, playerNum, opponentNum, depth):
    if depth == 0:
        return
    children = nextStates(state, playerNum, opponentNum)
    # print(children)
    for child in children:
        state.addChild(child)
    for child in state.getChildren():
        expand(child, opponentNum, playerNum, depth - 1)
    return state
    # statesQueue = []
    # statesQueue.append(state)
    # i = 0
    # while(len(statesQueue) != 0 and i < depth):
    #     currentState = statesQueue.pop(0)
    #     children = nextStates(state, playerNum, opponentNum)
    #     for child in children:
    #         currentState.addChild(child)
    #         statesQueue.append(child)
    #     i += 1
    # return state

def setHeuristics(state: StateNode, playerNum):
    color = ""
    if(playerNum == 1):
        color = 'black'
    else:
        color = 'white'
    if len(state.getChildren()) == 0:
        state.setHeuristic(total_heuristic(state.state,color))
        return
    for child in state.getChildren():
        setHeuristics(child, playerNum)
    return state


state = StateNode()
state.state = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
# print(validMoves(state, 1, 2))

tree = expand(state, 1, 2, 2)
setHeuristics(tree, 1)

move = minimax(tree)
printState(move)


# for firstChild in tree.getChildren():
#     printState(firstChild.state)
#     print("Heuristic value = ", firstChild.getHeuristic())
#     for child in firstChild.getChildren():
#         printState(child.state)
#         print("Heuristic value = ", child.getHeuristic())
