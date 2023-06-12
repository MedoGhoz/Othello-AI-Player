# Othello-AI-Player

## Table of Contents

- [Introduction](#introduction)
- [Minimax Algorithm](#minimax-algorithm)
- [References](#references)

## Introduction

Othello game that allows human vs. human, human vs. computer and computer vs. computer using AI search algorithms and heuristics techniques.

## Minimax Algorithm

### General Description:

- The minimax algorithm is a decision-making algorithm used in game theory, specifically in turn-based games where two players take alternating turns. The algorithm aims to find the best move for the player currently making a move, assuming that the opponent will make the best possible move in response.

- The algorithm operates by recursively evaluating the scores of all possible moves from the current state of the game. It uses a tree-like structure to represent the possible moves and their outcomes. At each level of the tree, the algorithm alternates between two players: one player (Max) tries to maximize the score of their move, while the other player (Min) tries to minimize the score of Max's moves.

- The algorithm assumes that both players play optimally, always choosing the move that leads to the best possible outcome for them.

- To evaluate the score of each possible move, the algorithm utilizes a heuristic function that assigns a score to each state of the game. The heuristic function estimates how good a particular state is for the player who is currently making a move, based on factors such as the position of the pieces on the board and the number of pieces captured.

### Description in Project:

- The `minimax` function is an implementation of the minimax algorithm for finding the best move for a player in a turn-based game. It takes a `state` parameter, which is an instance of a `StateNode` class representing the current state of the game.

- The `minimax` function consists of two nested functions: `max_value` and `min_value`, representing the two players in the game: Max (the player trying to maximize their score) and Min (the opponent player trying to minimize Max's score). The `max_value` and `min_value` functions recursively evaluate the score of each possible move and return the best score and the corresponding state.

- The `max_value` function first checks if the current state is a leaf node (i.e., there are no more possible moves). In this case, it returns the heuristic score of the state. If the current state is not a leaf node, the function creates a copy of the state and retrieves its children. For each child of the state, the function recursively calls the `min_value` function to get the minimum score that the opponent can achieve in response to Max's move. The function returns the maximum score and the corresponding state.

- The `min_value` function is similar to the `max_value` function, except that it aims to minimize the score of Max's moves by retrieving the maximum score that Max can achieve in response to Min's move.

- The `minimax` function initializes the variables `best_state` and `best_score` to `None` and negative infinity, respectively. It then iterates through each child of the current state and calls the `max_value` function to obtain the best score and the corresponding state that Max can achieve. If the score is greater than the current best score, the function updates `best_state` and `best_score` with the new values.

- Finally, the `minimax` function returns the best state that Max can achieve. This state represents the best move that Max can make in the current state of the game.

## References

1. Rosenbloom, P., A world-championship-level Othello program, Artificial Intelligence, 19, pp 279-320, 1982.
2. Buro, M., Improving heurisitic minimax search by supervised learning, Artificial Intelligence 134, pp 85-99, 2002.
3. Utgoff, E. P. Feature Construction for Game Playing, Technical Report, University of Massachutes, Amherst,MA.
