from ticTacToe.Agents.BasicAgent import BasicAgent

from ticTacToe.Gameboards.gameLogic import gameLogic

# Constant Board Position Values
twoRow = 5
corner = 6
side = 3

class MinimaxAgent(BasicAgent):

    def __init__(self, board, player):
        super(MinimaxAgent, self).__init__(board, player)

    def move(self, board):
        maxDepth = self.maxDepth(board)

        genTree = self.createMoveTree(board, maxDepth)
        optimalMove = self.minimax(genTree, maxDepth)

        return {'x': self.oneDMove(optimalMove)[0], 'y': self.oneDMove(optimalMove)[1], 'player': self.player}

    def minimax(self, moveTree: dict, maxDepth):

        # make move agent that analyzes move tree and chooses move based on this

        if maxDepth > 2:
            for i in moveTree.keys():
                for s in moveTree[i].keys():
                    vals = [moveTree[i][s][k] for k in moveTree[i][s].keys()]
                    moveTree[i][s] = max(vals)

            for i in moveTree.keys():
                vals = [moveTree[i][s] for s in moveTree[i].keys()]
                moveTree[i] = min(vals)

        vals = [moveTree[i] for i in moveTree.keys()]
        bestScore = max(vals)
        bestMove = None

        for i in moveTree.keys():
            if moveTree[i] == bestScore:
                bestMove = i
                break

        return bestMove

    def createMoveTree(self, board, maxDepth):

        # 10/27 assume depth always 3 to make it easier

        tree = {}
        gameCopy = gameLogic()
        gameCopy.setBoard(board)
        for i in range(0, 9):
            if not gameCopy.spotFull1D(i):
                if maxDepth > 2:
                    tree[i] = {}
                else:
                    tree[i] = self.totalValue(gameCopy.board, self.player)


        values = [0, 0, 0]

        if maxDepth > 2:
            for i in tree.keys():
                gameCopy.move(self.oneDMove(i)[0], self.oneDMove(i)[1], self.player)
                values[0] = self.totalValue(gameCopy.board, self.player)
                for s in range(0, 9):
                    if not gameCopy.spotFull1D(s) and s != i:
                        tree[i][s] = {}

                for s in tree[i].keys():
                    gameCopy.move(self.oneDMove(s)[0], self.oneDMove(s)[1], self.oppoPlayer())
                    values[1] = - self.totalValue(gameCopy.board, self.oppoPlayer())

                    for k in range(0, 9):

                        if not gameCopy.spotFull1D(k) and k != s and k != i:
                            gameCopy.move(self.oneDMove(k)[0], self.oneDMove(k)[1], self.player)
                            values[2] = self.totalValue(gameCopy.board, self.player)

                            tree[i][s][k] = sum(values)

                            gameCopy.removeMove(self.oneDMove(k)[0], self.oneDMove(k)[1])

                    gameCopy.removeMove(self.oneDMove(s)[0], self.oneDMove(s)[1])

                gameCopy.removeMove(self.oneDMove(i)[0], self.oneDMove(i)[1])


        return tree

    def totalValue(self, board, player):
        return self.corners(board, player) + self.middle(board, player) + self.twoInARow(board, player) + self.win(board, player)

    def win(self, board, player):
        winner = False
        for i in range(0, 3):
            # horizontal
            if board[i][0] == player and board[i][0] == board[i][1] == board[i][2]:
                winner = True
                break
            # vertical
            if board[0][i] == player and board[0][i] == board[1][i] == board[2][i]:
                winner = True
                break

        # top left to bottom right diagonal
        if board[0][0] == player and board[0][0] == board[1][1] == board[2][2]:
            winner = True

        # top right to bottom left
        if board[2][0] == player and board[2][0] == self.board[1][1] == self.board[0][2]:
            winner = True

        if winner:
            return 1000
        else:
            return 0

    def corners(self, board, player):
        value = 0
        if board[0][0] == player:
            value += corner
        if board[0][2] == player:
            value += corner
        if board[2][0] == player:
            value += corner
        if board[2][2] == player:
            value += corner

        return value

    def middle(self, board, player):
        value = 0
        if board[0][1] == player:
            value += side
        if board[1][0] == player:
            value += side
        if board[1][2] == player:
            value += side
        if board[2][1] == player:
            value += side

        return value

    def twoInARow(self, board, player):
        value = 0

        # check horiz two in a rows
        for i in range(0, 3):
            playerCount = 0
            enemyCount = 0
            for s in board[i]:
                if s == player:
                    playerCount += 1
                elif s == self.oppoPlayer():
                    enemyCount += 1
                    break

            if playerCount == 2 and enemyCount == 0:
                value += twoRow

        # check vert two in a rows
        for i in range(0, 3):
            playerCount = 0
            enemyCount = 0
            for s in board:
                if s[i] == player:
                    playerCount += 1
                elif s[i] == self.oppoPlayer():
                    enemyCount += 1
                    break
            if playerCount == 2 and enemyCount == 0:
                value += twoRow

        # check diagonal two in a rows
        playerCount = 0
        enemyCount = 0
        for i in range(0, 3):
            if board[i][i] == player:
                playerCount += 1
            elif board[i][i] == self.oppoPlayer():
                enemyCount += 1
                break

        if playerCount == 2 and enemyCount == 0:
            value += twoRow

        playerCount = 0
        enemyCount = 0
        for i in range(0, 3):
            if board[2-i][i] == player:
                playerCount += 1
            elif board[2-i][i] == self.oppoPlayer():
                enemyCount += 1
                break

        if playerCount == 2 and enemyCount == 0:
            value += twoRow

        return value

    def maxDepth(self, initBoard):
        notFull = 0
        for i in range(0, 3):
            for s in range(0, 3):
                if initBoard[i][s] == 0:
                    notFull += 1
        return notFull

    def oppoPlayer(self):
        if self.player == 1:
            return 2
        else:
            return 1

    def oneDMove(self, num):
        col = num % 3
        row = int(num/3)

        return [row, col]


"""
    Minimax Strategy TODO
    
        - Possible Board Positions, represent each move in [0, 8]
            Move Chart:
                0   1   2 
                3   4   5
                6   7   8
         - Create a dict within a dict for each possible move
            Will Create Tree
        - At end of tree, will be points associated with best moves according to highest value
        - run minimax algorithm on this to find the best path to move down
        - repeat for each new board position

"""

if __name__ == "__main__":
    game = gameLogic()
    agent = MinimaxAgent(game.board, 1)
    game.move(1, 2, 1)
    game.move(0, 2, 1)
    game.move(0, 1, 2)
    game.move(1, 1, 2)

    # tree = agent.createMoveTree(game.board, 1)
    # print(game.board)
    #
    # agent.minimax(tree)

    print(agent.maxDepth(game.board))

    # game.test()
    # print(agent.oneDMove(3))
    # print(agent.oneDMove(1))
    # print(agent.oneDMove(7))


