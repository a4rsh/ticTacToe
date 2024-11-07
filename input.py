from game import isLegalMove


def askMove(board, player):
    validMove = False
    while not validMove:
        move = input("Player " + str(player) + " Turn: ")
        try:
            move = int(move)
        except ValueError:
            print("You must enter an integer number!")
            continue
        if isLegalMove(board, move):
            validMove = True
        else:
            print("Invalid Move!")
    return move