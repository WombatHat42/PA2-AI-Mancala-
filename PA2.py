"""
PA2
"""
#determines if game is over - no moves left. returns t/f
def isLeaf(state):
    if getMoves(state):
        return False
    else:
        return True 
#determines what the score is and returns the value that represents the score
def evaluate(isMax):
    if isMax:
        return -1
    else:
        return 1
#detemines player 1 & 2 moves, return legal moves. index of moves you can make from the current board
def getMoves(state):
    possible_moves = []

    for index in range(len(state)):
        if state[0] != 0:
            possible_moves.append(index)
    return possible_moves  
#determines score for each move. determines which legal move is going to be the move that will make player win
def miniMax(prevState, move, isMax): 
    state = updateState(prevState, move)  
    if isLeaf(state):
        return evaluate(isMax)    
    if isMax:
        highest = float('-inf')
        for position in getMoves(state):
            temp = miniMax(state,position, not isMax)
            if temp[1]>highest:
                highest = temp[1]
                move = position                
        return (move, highest)
    else:
        lowest = float('inf')
        for position in getMoves(state):
            temp = miniMax(state, position, not isMax)
            if temp[1]<lowest:
                lowest = temp[1]
                move = position
        return (move, lowest)   
##loop to iterate thru copyState to incrase value of the pits by 1. 
def updateState(state, move):
    copyState = state.copy()
    marbles = state[move] ##variable that equals the number of beads in that pit. to be placed in the right pit
    pit = 0
    try:
        for i in range(copyState):
            pit +=1
    except:
        pass
    print(pit)
    print(copyState)
    return copyState

def search(state):
    state = list(state)
    for element in range(len(state)):
        state[element] = int(state[element])
    possible_moves = getMoves(state)
    for move in possible_moves:
        win_lose = miniMax(state, move, True)
        for position in win_lose:
            if position == -1:
                ##results = "Win"
                return moves, "Win"
    ##print(state)
    ##updateState(state, 0)
    print(move,results)
    
    return (move,results)
#print(search("3222"))
#updateState([2,2,2],0)
search("3222")
#updateState is given event 0 so it should return "0333"
