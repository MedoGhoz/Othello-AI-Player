#Minmax function
from ..internals.node import StateNode
import copy
def minimax(state):
    def max_value(state):
        if(len(state.getChildren()) == 0):
            return [state.heuristic, state.state]
        score = float('-inf')
        new_state = copy.deepcopy(state)
        new_state = new_state.getChildren()

        for child in new_state:
            oldScore = score
            score = max(score, min_value(child)[0])
            if(score != oldScore):
                state = child
        return [score, state.state]

    def min_value(state):
        if(len(state.getChildren()) == 0):
            return [state.heuristic, state.state]
        score = float('inf')
        new_state = copy.deepcopy(state)
        new_state = new_state.getChildren()
        for child in new_state:
            oldScore = score
            score = min(score, max_value(child)[0])
            if(score != oldScore):
                state = child
        return [score, state.state]

    best_state = None
    best_score = float('-inf')
    for child in state.getChildren():
        new_state = copy.deepcopy(state)
        out= max_value(new_state)
        if(out[0] > best_score):
            best_score = out[0]
            # print(best_score)
            best_state = out[1]
            # print(best_state)
    return best_state