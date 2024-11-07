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
        elif adv == 0:
            outcome = 0
        else:
            outcome = -1

        # Uncommenting this will show the evaluation for all possible moves before the bot move is made
        # print("Move: " + str(testMove) + ", Outcome: " + str(outcome))

        if outcome > bestOutcome:
            bestOutcome = outcome
            bestMove = testMove

    print("Player " + str(turn) + " Turn: " + str(bestMove))
    return bestMove

def evalPosition(board, turn):
    # Generate all legal moves
    legalMoves = []
    for testMove in range(10):
        if isLegalMove(board, testMove):
            legalMoves.append(testMove)
    adv = turn % 2 + 1 # Keeps track of who has the advantage, 0 is a draw, assumes worst case for start
    for testMove in legalMoves:
        # Iterating through the legal moves for this position
        localBoard = [row[:] for row in board]
        game.makeMove(localBoard, testMove, turn)
        winner = game.checkWinner(localBoard, testMove)  # 0 -> Game in Progress, 1 & 2 -> Winner, 3 -> Draw
        if winner == turn:
            # Player has advantage if it can win in one move
            return turn
        elif winner == 3:
            # If a move can force a draw, the worst case is now a draw
            if adv == turn % 2 + 1:
                adv = 0
        elif winner == 0:
            # If the game is ongoing, the position is evaluated further
            # Evaluation is updated if it is better
            nextEval = evalPosition(localBoard, turn % 2 + 1)
            if adv == turn % 2 + 1 or nextEval == turn:
                adv = nextEval
        # The other player cannot win on this turn, and if it's a draw adv can stay at 0
    return adv