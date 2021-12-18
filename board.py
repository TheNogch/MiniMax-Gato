import os 
class Board():
    def __init__(self) -> None:
        self.initializeBoard()

    def initializeBoard(self):
        self.board = ["-" for _ in range(9)]
    
    def __str__(self) -> str:
        os.system("cls")
        printStr = "\n\n|-----|-----|-----|\n"
        for index, value in enumerate(self.board):
            char = value if value != "-" else index + 1
            printStr += f"|  {char}  "
            if( (index + 1) % 3 == 0): printStr += "|\n|-----|-----|-----|\n"
        return printStr
    
    def makeMove(self, position: int, playerLetter: str):
        self.board[position] = playerLetter
    
    def undoMove(self, position: int) -> None:
        self.board[position] = "-"

    def areMovesAvailable(self) -> bool:
        return "-" in self.board

    def getAvailableMoves(self):
        return [index for index, value in enumerate(self.board) if value == "-"]

    def checkWin(self, letter: str) -> bool:
        #Row Win
        for row in range(3):
            rowCheck = self.board[3*row:3*(row+1)]
            if (all(value == letter for value in rowCheck)): return True

        #Column Win
        for column in range(3):
            columnCheck = [self.board[column], self.board[column+3], self.board[column+6]]
            if (all(value == letter for value in columnCheck)): return True

        #Diagonal Win
        if (self.board[0] == self.board[4] == self.board[8] == letter): return True      
        if (self.board[2] == self.board[4] == self.board[6] == letter): return True      

        return False
        