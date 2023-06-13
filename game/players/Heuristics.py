import numpy as np
from collections import deque
from ..players.moves import availableMoves


# state = [ [0,1,0,0,0,0,0,2]
#          ,[1,2,0,0,0,0,2,2]
#          ,[0,0,1,1,0,0,0,0]
#          ,[0,0,0,0,0,0,0,0]
#          ,[0,0,0,1,0,0,0,0]
#          ,[0,0,0,0,1,0,0,0]
#          ,[0,1,0,0,0,0,1,1]
#          ,[1,0,0,0,0,0,2,1]]
# state = np.array(state)
# state = np.random.randint(low=0, high=3, size=(8,8))
# for row in state:
#     for item in row:
#         print(item,end='|')
#     print()



def countBlack(state):
    NoOfBlackCoins = 0
    #method 1
    # for row in state:
    #     for member in row:
    #         if(member==1):
    #             NoOfBlackCoins=NoOfBlackCoins+1
                
    #method 2
    (unique, counts) = np.unique(state, return_counts=True)
    frequencies = np.asarray((unique, counts)).T
    for row in frequencies:
        if row[0]==1:
            NoOfBlackCoins = row[1]
    return NoOfBlackCoins


def countWhite(state):
    NoOfWhiteCoins = 0
    # for row in state:
    #     for member in row:
    #         if(member==2):
    #             NoOfWhiteCoins=NoOfWhiteCoins+1
    #method 2
    (unique, counts) = np.unique(state, return_counts=True)
    frequencies = np.asarray((unique, counts)).T
    for row in frequencies:
        if row[0]==2:
            NoOfWhiteCoins = row[1]
            # print(NoOfWhiteCoins)
    return NoOfWhiteCoins
def Coin_Parity(state,maxPlayerColor):
    if (maxPlayerColor=='black'):
        Max_Player_Coins = countBlack(state)
        Min_Player_Coins = countWhite(state)
        # print(Max_Player_Coins,Min_Player_Coins)
        Coin_Parity = 100*((Max_Player_Coins - Min_Player_Coins ) / (Max_Player_Coins + Min_Player_Coins))
    else:
        Max_Player_Coins = countWhite(state)
        Min_Player_Coins = countBlack(state)
        Coin_Parity = 100*((Max_Player_Coins - Min_Player_Coins ) / (Max_Player_Coins + Min_Player_Coins))
    return Coin_Parity

#----------------------------------------------------------------------------------------------------------------
"""takes up the number of possible moves for the max_player and the min_player"""
def mobility(max_player_moves,min_player_moves):
    if((max_player_moves +min_player_moves) !=0):
        Actual_Mobility_Heuristic_Value =  100* (max_player_moves - min_player_moves)/(max_player_moves+ min_player_moves) 
    else:
        Actual_Mobility_Heuristic_Value = 0
    return Actual_Mobility_Heuristic_Value
#----------------------------------------------------------------------------------------------------------------
#potential corner:how many corners can be possessed in the next move
#unlikely corner:
"""
if i can capture it in next move it is => potential weight 0.75
if i can capture it after two-three moves it is unlikely weight 0.25
"""
def Corners_Captured_generator(current_state,max_player_color):
    # for row in current_state:
    #     for item in row:
    #         print(item,end='|')
    #     print()
    maximizer_potential_corner_value = 0
    minimizer_potential_corner_value = 0
    # if((state[0][1] |state[1][0] | state[1][1])==1):
    #     black_potential_corner_value+=1
    # if((state[0][6] |state[1][7] | state[1][6])==1):
    #     black_potential_corner_value+=1
    # if ((state[7][1] |state[6][0] | state[6][1])==1) :
    #     black_potential_corner_value+=1
    # if ((state[7][6] |state[6][6] | state[6][7])==1):
    #     black_potential_corner_value+=1
        
    # if(state[0][1]==2 or state[1][0]==2 or state[1][1]==2):
    #     white_potential_corner_value+=1
    # if(state[0][6]==2 or state[1][7]==2 or state[1][6]==2):
    #     white_potential_corner_value+=1
    # if (state[7][1]==2 or state[6][0]==2 or state[6][1]==2) :
    #     white_potential_corner_value+=1
    # if (state[7][6]==2 or state[6][6]==2 or state[6][7]==2):
    #     white_potential_corner_value+=1
    if max_player_color=='black':
        max_num = 1
        min_num = 2
    else:
        max_num = 2
        min_num = 1
    
    availableMovesMaximizer = availableMoves(state=current_state, playerNum=max_num, opponentNum=min_num)
    availableMovesMinimizer = availableMoves(state=current_state, playerNum=min_num, opponentNum=max_num)
    for corner in [(0,0),(7,0),(0,7),(7,7)]:
        if corner in availableMovesMaximizer['validMoves']:
            maximizer_potential_corner_value+=1
        if corner in availableMovesMinimizer['validMoves']:
            minimizer_potential_corner_value+=1

        
    # if (max_player_color=='black'):
        corner_Heuristic_Value = Corners_Captured(maximizer_potential_corner_value,0,minimizer_potential_corner_value,0)
    # else:
        # corner_Heuristic_Value = Corners_Captured(white_potential_corner_value,0,black_potential_corner_value,0)
    # print(maximizer_potential_corner_value,minimizer_potential_corner_value)
    return corner_Heuristic_Value


def Corners_Captured(Max_Player_potential_Corner_Value,Max_Player_unlikely_Corner_Value,Min_Player_potential_Corner_Value,Min_Player_unlikely_Corner_Value):
    Max_Player_Corner_Value = 0.75* Max_Player_potential_Corner_Value + 0.25 * Max_Player_unlikely_Corner_Value
    Min_Player_Corner_Value =0.75* Min_Player_potential_Corner_Value + 0.25 * Min_Player_unlikely_Corner_Value
    # print(Max_Player_Corner_Value,Min_Player_Corner_Value)
    if((Max_Player_Corner_Value +Min_Player_Corner_Value) !=0):
        corner_Heuristic_Value =  100* (Max_Player_Corner_Value - Min_Player_Corner_Value)/(Max_Player_Corner_Value+ Min_Player_Corner_Value) 
    else:
        corner_Heuristic_Value = 0
    return corner_Heuristic_Value
        
#----------------------------------------------------------------------------------------------------------------
#stable => corner coins and what is built on the corner WEIGHT EQUALS TO 1
#unstable=>can be flanked next move. WEIGHT EQUALS TO -1
#semi-stable=> can be flanked in next 3 - 4 moves say but not the next one. IGNORED

# Function to count the number of stable coins
def breadth_first_search(state, start_row, start_col,color):
    number_of_stable_coins = 0
    queue = deque([(start_row, start_col)])
    visited = set([(start_row, start_col)])
    
    while queue:
        row, col = queue.popleft()
        # Process the current position
        if(color=='black'and state[row][col]==1):
            number_of_stable_coins+=1
            # print(row,col)
        elif (color=='black'and state[row][col]!=1):
            break
        
        if (color=='white' and state[row][col]!=2):
            break
        elif(color=='white'and state[row][col]==2):
            number_of_stable_coins+=1
        # Explore neighboring positions
        for dr, dc in [(-1, 1) , (0, 1) , (1, 1),(-1, 0) , (0, 0) , (1, 0),(-1, -1), (0, -1), (1, -1)]:
            new_row = row + dr
            new_col = col + dc
            
            if (new_col>=0 and new_col<=7) and (new_row>=0 and new_row<=7)  and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
    # print(visited)
    return number_of_stable_coins
def Stability(max_player_color, state):
    max_player_stable_coins = 0
    min_player_stable_coins = 0
    max_player_unstable_coins = 0
    min_player_unstable_coins = 0
    for (row,col) in [(0,0),(0,7),(7,0),(7,7)]:
        if ( max_player_color=='black'):
            if  state[row][col] == 1:
                max_player_stable_coins+=breadth_first_search(color='black',start_col=col,start_row=row,state=state)
            if (state[row][col] == 2):
                min_player_stable_coins+=breadth_first_search(color='white',start_col=col,start_row=row,state=state)
        if ( max_player_color=='white'):
            if state[row][col] == 2:
                max_player_stable_coins+=breadth_first_search(color='white',start_col=col,start_row=row, state=state)
            if (state[row][col] == 1):
                min_player_stable_coins+=breadth_first_search(color='black',start_col=col,start_row=row, state=state)
    # print(min_player_stable_coins,max_player_stable_coins)
    max_player_stability = max_player_stable_coins - max_player_unstable_coins
    min_player_stability = min_player_stable_coins - min_player_unstable_coins
    if((max_player_stability +min_player_stability) !=0):
            Stability_Heuristic_Value =  100* (max_player_stability - min_player_stability)/(max_player_stability+ min_player_stability) 
    else:
        Stability_Heuristic_Value = 0
    return Stability_Heuristic_Value
        
def total_heuristic(current_state,max_player_color):
    corner_heuristic = Corners_Captured_generator(current_state=current_state,max_player_color=max_player_color)
    #getting availableMoves for each player
    if max_player_color=='black':
        max_num = 1
        min_num = 2
    else:
        max_num = 2
        min_num = 1
    
    avail_moves_max_player = availableMoves(state=current_state,playerNum=max_num,opponentNum=min_num)
    avail_moves_min_player = availableMoves(state=current_state,playerNum=min_num,opponentNum=max_num)
    max_player_number_of_possible_moves =len(avail_moves_max_player['validMoves'])
    min_player_number_of_possible_moves = len(avail_moves_min_player['validMoves'])
    #calling heirstics
    mobility_heuristic = mobility(max_player_number_of_possible_moves,min_player_number_of_possible_moves)
    coin_parity_heuristic = Coin_Parity(state = current_state,maxPlayerColor = max_player_color)
    stability_heuristic = Stability(max_player_color=max_player_color, state=current_state)
    
    # print(" corner:%f \n mobility:%f \n parity:%f \n stability:%f \n"%(corner_heuristic,mobility_heuristic, coin_parity_heuristic,stability_heuristic))
    total_heuristic =( 3*corner_heuristic+3*coin_parity_heuristic+stability_heuristic+3*mobility_heuristic) / 10
    # print(total_heuristic)
    return total_heuristic
    