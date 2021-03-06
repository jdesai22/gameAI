from ticTacToe.Gameboards.gameLogic import gameLogic
from ticTacToe.Agents.RandomAgent import RandomAgent
from ticTacToe.Agents.MinimaxAgent import MinimaxAgent
from ticTacToe.Agents.BasicAgent import BasicAgent
from ticTacToe.Agents.PlayerAgent import PlayerAgent

class printGameTerminal(gameLogic):
    def __init__(self):
        self.terminalBoard = [[" ", " ", " "] for i in range(0, 3)]
        super(printGameTerminal, self).__init__()

    def turn(self, playerMove):
        super().turn(playerMove)
        self.draw()

    def convertBoard(self):
        for row in range(0, 3):
            for col in range(0, 3):
                if self.board[row][col] == 1:
                    self.terminalBoard[row][col] = "X"
                elif self.board[row][col] == 2:
                    self.terminalBoard[row][col] = "O"

    def draw(self):
        self.convertBoard()
        for i in range(0, 3):
            print(" " + self.terminalBoard[i][0] + " " + "|" + " " + self.terminalBoard[i][1] + " " + "|" + " " +
                  self.terminalBoard[i][2])
            if i != 2:
                self.printHorDiv()

        print("\n")


    def printHorDiv(self):
        print("-----------")


def printMoveKey():
    print(" " + "1" + " " + "|" + " " + "2" + " " + "|" + " " + "3")
    print("-----------")
    print(" " + "4" + " " + "|" + " " + "5" + " " + "|" + " " + "6")
    print("-----------")
    print(" " + "7" + " " + "|" + " " + "8" + " " + "|" + " " + "9")

    print("\n")


if __name__ == "__main__":
    printMoveKey()
    terminal = printGameTerminal()
    player1 = PlayerAgent(terminal.board, 1)
    player2 = RandomAgent(terminal.board, 2)

    while not terminal.gameFinished():
        desMove = player1.move(terminal.board)
        terminal.turn(desMove)
        if not terminal.gameFinished():
            terminal.turn(player2.move(terminal.board))

    if terminal.winner > 0:
        print("Winner is Player {}".format(int(terminal.winner)))
    else:
        print("No Winner")




