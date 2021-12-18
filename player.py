import math
import random
from board import Board

class Player():
    def __init__(self, letter: str) -> None:
        self.letter = letter
    
    def makeMove(self, board: Board) -> None:
        pass

class HumanPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)
    
    def makeMove(self, board: Board) -> None:
        position = int(input(f"\nTurno de {self.letter}. Ingresa movimiento(1-9): ")) - 1
        while position not in board.getAvailableMoves():
            position = int(input("Movimiento invalido, ingrese nuevo movimiento: "))
        board.makeMove(position, self.letter)

class RandomPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)
    
    def makeMove(self, board: Board) -> None:
        board.makeMove(random.choice(board.getAvailableMoves()), self.letter)
    
class MiniMaxPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)
    
    def makeMove(self, board: Board) -> None:
        if(len(board.getAvailableMoves()) == 9):
            board.makeMove(random.choice(board.getAvailableMoves()), self.letter)
            return
        bestScore = -math.inf
        bestMove = None
        for move in board.getAvailableMoves():
            board.makeMove(move, self.letter)
            score = self.minimax(board, False)
            board.undoMove(move)
            if score > bestScore:
                bestScore = score
                bestMove = move
        board.makeMove(bestMove, self.letter)

    def minimax(self, board: Board, isMaximizing: bool):
        otherPlayer = "O" if self.letter == "X" else "X"

        if board.checkWin(self.letter): return 1
        elif board.checkWin(otherPlayer): return -1
        elif not board.areMovesAvailable(): return 0

        scores = []
        for move in board.getAvailableMoves():
            board.makeMove(move, self.letter if isMaximizing else otherPlayer)
            scores.append(self.minimax(board, not isMaximizing)) # 1 ; 0 ; -1 dependiendo del tablero resultante
            board.undoMove(move)
        return max(scores) if isMaximizing else min(scores)


