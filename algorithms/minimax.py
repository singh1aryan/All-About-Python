'''
minimax algo for a tic tac toe game
2nd part would have the alpha beta pruning
'''

player = 'x'
opponent = 'o'

class Move:
    def __init__(self):
        self.row = None
        self.column = None

def minimax(board, depth, isMaxPlayer):
    ''' if the maximizer or the minimizer wins the game '''
    
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    
    if isMovesLeft(board) == False:
        return 0
    
    ''' If the max condition is true, its AI's turn'''
    if isMaxPlayer == True:
        bestVal = -1000
        for r in range(0,3):
            for c in range(0,3):
                if board[r][c] == '_':
                    board[r][c] = player
                    bestVal = max(bestVal, minimax(board, depth+1, False))
                    board[r][c] = '_'
                
        return bestVal
    
    ''' if the max player is false // its the opponent's turn'''
    if isMaxPlayer == False:
        bestVal = 1000
        for r in range(0,3):
            for c in range(0,3):            
                if board[r][c] == '_':
                    board[r][c] = opponent
                    bestVal = min(bestVal, minimax(board, depth+1, True))
                    board[r][c] = '_'
                    
        return bestVal

''' return true if there are moves left, otherwise false'''
def isMovesLeft(board):
    for r in board:
        if '_' in r:
            return True
    return False

''' 
Evaluate the score for the position of the board
This can be improved/written differently - recursive or using direction arrays   
'''
def evaluate(board):
    for i in range(0,3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == player:
                return 10
            elif board[i][0] == opponent:
                return -10
    
    for i in range(0,3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == player:
                return 10
            elif board[0][i] == opponent:
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10
    

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10
    
    return -1

def findBestMove(board):
    print(5)
    bestVal = -1000
    move = Move()
    for r in range(0,3):
        for c in range(0,3):
            if board[r][c] == '_':
                board[r][c] = player
                val = minimax(board, 0, False)
                board[r][c] = '_'
                if val>bestVal:
                    move.row = r
                    move.column = c
                    bestVal = val

    print('move row: ', move.row)
    print('move column: ',move.column)
    print('previous board: ',board)
    board[move.row][move.column] = player
    print('new board: ',board)


               
    
board = [
        [ 'x', 'o', 'x' ], 
        [ 'o', 'o', 'x' ], 
        [ '_', '_', '_']
        ]
    
findBestMove(board)
