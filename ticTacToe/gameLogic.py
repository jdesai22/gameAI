import numpy as np

class gameLogic():
    def __init__(self):
        self.board = np.zeros(shape=(3,3))

        self.p1Turn = True
        self.gameOver = False
        self.winner = 0
        self.boardFull = False

    def turn(self, playerMove):
        self.move(playerMove["x"], playerMove["y"], playerMove["player"])

    def move(self, row, col, player):
        # if self.spotFull(row, col):
        #     raise Exception("moved on already full spot")
        # else:
        self.board[row][col] = player

    def removeMove(self, row, col):
        self.board[row][col] = 0

    def gameFinished(self):
        for i in range(0, 3):
            # horizontal
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                self.gameOver = True
                self.winner = self.board[i][0]
                break
            # vertical
            if self.board[0][i] != 0 and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                self.gameOver = True
                self.winner = self.board[0][i]
                break
        # top left to bottom right diagonal
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.gameOver = True
            self.winner = self.board[i][i]

        # top right to bottom left
        if self.board[2][0] != 0 and self.board[2][0] == self.board[1][1] == self.board[0][2]:
            self.gameOver = True
            self.winner = self.board[2][0]

        if self.isBoardFull():
            self.gameOver = True

        return self.gameOver

    def isBoardFull(self):
        dimOne = np.ravel(self.board)
        check = np.all(dimOne != 0)
        return check

    def spotFull(self, row, col):
        return bool(self.board[row][col])

    def spotFull1D(self, num):
        return bool(np.ravel(self.board)[num])

    def setBoard(self, board):
        self.board = board

    def test(self):
        print(self.board)


if __name__ == "__main__":
    game = gameLogic()

    game.test()
    game.isGameWon()
    game.isBoardFull()
    game.test()
