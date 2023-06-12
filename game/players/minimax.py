#Minimax function to find the best move 
from ..internals.node import StateNode
import copy
def minimax(state):
    #represent the player who is trying to maximize their score
    def max_value(state):
        if(len(state.getChildren()) == 0):    #checking if the current state is a leaf node 
            return [state.heuristic, state.state]
        score = float('-inf')
        new_state = copy.deepcopy(state)
        new_state = new_state.getChildren()
        
#for each child of the state, the function recursively calls the min_value function to get
#the minimum score that the opponent can achieve in response to Max's move.
        for child in new_state:
            oldScore = score
            score = max(score, min_value(child)[0])
            if(score != oldScore):
                state = child
        return [score, state.state]   #The function returns the maximum score and the corresponding state

#represent the opponent player who is trying to minimize Max's score
    def min_value(state):
        if(len(state.getChildren()) == 0):    #checking if the current state is a leaf node 
            return [state.heuristic, state.state]
        score = float('inf')
        new_state = copy.deepcopy(state)
        new_state = new_state.getChildren()
        for child in new_state:
            oldScore = score
            score = min(score, max_value(child)[0])  #tries to minimize the score of Max's moves by getting the maximum score that Max can achieve in response to Min's move.
            if(score != oldScore):
                state = child
        return [score, state.state]

#iterates through each child of the current state and calls the max_value function to get the best score and the corresponding state that Max can achieve.
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
    return best_state           #Finally, the minimax function returns the best state that Max can achieve



