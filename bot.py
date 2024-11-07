import game
from game import isLegalMove

def botMove(board, turn):
    legalMoves = []
    for testMove in range(10):
        if isLegalMove(board, testMove):
            legalMoves.append(testMove)

    bestMove = legalMoves[0]
    bestOutcome = -1 # -1 loss, 0 draw, 1 win

    for testMove in legalMoves:
        localBoard = [row[:] for row in board]
        game.makeMove(localBoard, testMove, turn)

        adv = 0
        winner = game.checkWinner(localBoard, testMove)
        if winner == turn:
            adv = turn
        elif winner == 0:
            adv = evalPosition(localBoard, turn % 2 + 1)

        outcome = 0
        if adv == turn:
            outcome = 1
        elif adv == turn % 2 + 1:
            outcome = -1

        if outcome > bestOutcome:
            bestOutcome = outcome
            bestMove = testMove

    print("Player " + str(turn) + " Turn: " + str(bestMove))
    return bestMove

def evalPosition(board, turn):
    legalMoves = []
    for testMove in range(10):
        if isLegalMove(board, testMove):
            legalMoves.append(testMove)
    adv = 0
    for testMove in legalMoves:
        localBoard = [row[:] for row in board]
        game.makeMove(localBoard, testMove, turn)
        winner = game.checkWinner(localBoard, testMove)
        if winner == turn:
            adv = turn
            return adv
        elif winner == 0:
            adv = evalPosition(localBoard, turn % 2 + 1)
    return adv