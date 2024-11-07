import game, input, display, bot

board = [[0 for i in range(3)] for j in range(3)]
gameStatus = 0
turn = 1

while gameStatus == 0:
    display.printBoard(board)
    if turn == 1: # 1: Human plays first, 2: Bot plays first
        move = input.askMove(board, turn)
    else:
        move = bot.botMove(board, turn)
    game.makeMove(board, move, turn)
    gameStatus = game.checkWinner(board, move)
    turn = turn % 2 + 1

display.printBoard(board)
display.printResult(gameStatus)