def printBoard(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                print("X", end=" ")
            elif board[i][j] == 2:
                print("O", end=" ")
            else:
                print("*", end=" ")
        print("")

def printResult(result):
    if result == 1:
        print("Player 1 Wins!")
    elif result == 2:
        print("Player 2 Wins!")
    else:
        print("The game is a draw!")