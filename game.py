def checkWinner(board, move): # 0 -> Game in Progress, 1 & 2 -> Winner, 3 -> Draw
    i = (move - 1) // 3
    j = (move - 1) % 3
    potentialWinner = board[i][j]

    rowWin = True
    for row in range(3):
         if board[row][j] != potentialWinner:
             rowWin = False
    colWin = True
    for column in range(3):
        if board[i][column] != potentialWinner:
            colWin = False
    diagOneWin = True
    diagTwoWin = True
    if move % 2 == 0:
        diagOneWin = False
        diagTwoWin = False
    else:
        if move % 4 == 1: # 1, 5, or 9
            for k in range(3):
                if board[k][k] != potentialWinner:
                    diagOneWin = False
        else:
            diagOneWin = False
        if 2 < move < 8: # 3, 5, or 7
            for k in range(3):
                if board[k][2-k] != potentialWinner:
                    diagTwoWin = False
        else:
            diagTwoWin = False

    if rowWin or colWin or diagOneWin or diagTwoWin:
        return potentialWinner
    elif any(0 in row for row in board):
        return 0
    else:
        return 3

def isLegalMove(board, move):
    i = (move - 1) // 3
    j = (move - 1) % 3
    if 10 > move > 0 == board[i][j]:
        return True
    return False

def makeMove(board, move, player):
    i = (move - 1) // 3
    j = (move - 1) % 3
    board[i][j] = player