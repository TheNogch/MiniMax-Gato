from progress.bar import Bar
from board import Board
from player import HumanPlayer, MiniMaxPlayer, Player, RandomPlayer

def play(board: Board, xPlayer: Player, oPlayer: Player, shouldPrint = True):
    if shouldPrint: print(board)
    currentPlayer = xPlayer.letter
    while board.areMovesAvailable():
        if currentPlayer == xPlayer.letter: xPlayer.makeMove(board)
        else: oPlayer.makeMove(board)
        if shouldPrint: print(board)
        if board.checkWin(currentPlayer): 
            if shouldPrint: print(f"\nJugador {currentPlayer} ha ganado")
            return currentPlayer
        currentPlayer = oPlayer.letter if currentPlayer == xPlayer.letter else xPlayer.letter
    if shouldPrint: print("\nEmpate")
    return "-"

if __name__ == '__main__':
    board = Board()
    xPlayer = HumanPlayer("X")
    oPlayer = MiniMaxPlayer("O")
    play(board, xPlayer, oPlayer, True)

    # winners = {
    #     xPlayer.letter: 0,
    #     oPlayer.letter: 0,
    #     "-": 0
    # }

    # CANTIDAD_JUEGOS = 1000
    # bar = Bar("Juegos", max=CANTIDAD_JUEGOS)
    # for _ in range(CANTIDAD_JUEGOS):
    #     board = Board()
    #     winners[play(board, xPlayer, oPlayer, False)] += 1
    #     bar.next()
    # bar.finish()
    # print(winners)