from .internals.node import StateNode
from .players.moves import availableMoves
from .players.moves import updateState
from .players.moves import printState
from .players.minimax import minimax
from copy import deepcopy
from utils import expand, printState


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
i = 20
tree = expand(state, 1, 2, 2)
for firstChild in tree.getChildren():
    printState(firstChild.state)
    for child in firstChild.getChildren():
        child.heuristic = 10.0 * i
        i += 1

move = minimax(tree)
printState(move)
# print(tree.getChildren())
# printState(tree.getChildren())
# for firstChild in tree.getChildren():
#     for child in firstChild.getChildren():
#         printState(child.state)

def setHeuristics(state: StateNode):
    if len(state.getChildren()) == 0:
        state.setHeuristic(dummyFunction(state.state))
        return
    for child in state.getChildren():
        setHeuristics(child)
    return state

def dummyFunction(state):
    return 20

setHeuristics(tree)

for firstChild in tree.getChildren():
    printState(firstChild.state)
    print("Heuristic value = ", firstChild.getHeuristic())
    for child in firstChild.getChildren():
        printState(child.state)
        print("Heuristic value = ", child.getHeuristic())
