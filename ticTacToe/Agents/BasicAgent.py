from ticTacToe.Gameboards.gameLogic import gameLogic
from ticTacToe.Agents.Agent import Agent


class BasicAgent(Agent):

    def __init__(self, board, player):
        super(BasicAgent, self).__init__(board, player)

    def move(self, board):
        blockMove = self.theyCanWin(board)
        if blockMove['x'] == -1:
            winMove = self.iCanWin(board)
            if winMove['x'] == -1:
                return self.randomMove()
            else:
                return winMove
        else:
            return blockMove

    def iCanWin(self, board):
        gameCopy = gameLogic()
        gameCopy.setBoard(board)

        for row in range(0, 3):
            for col in range(0, 3):
                if gameCopy.spotFull(row, col):
                    pass
                else:
                    gameCopy.move(row, col, self.player)
                    if gameCopy.gameFinished():
                        return {'x': row, 'y': col, 'player': self.player}
                    else:
                        gameCopy.removeMove(row, col)

        return {'x': -1, 'y': -1, 'player': self.player}

    def theyCanWin(self, board):
        gameCopy = gameLogic()
        gameCopy.setBoard(board)

        if self.player == 1:
            oppoPlayer = 2
        else:
            oppoPlayer = 1

        for row in range(0, 3):
            for col in range(0, 3):
                if not gameCopy.spotFull(row, col):
                    gameCopy.move(row, col, oppoPlayer)
                    if gameCopy.gameFinished():
                        return {'x': row, 'y': col, 'player': self.player}
                    else:
                        gameCopy.removeMove(row, col)

        return {'x': -1, 'y': -1, 'player': self.player}