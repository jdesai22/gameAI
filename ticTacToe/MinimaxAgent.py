from BasicAgent import BasicAgent

from gameLogic import gameLogic

class MinimaxAgent(BasicAgent):


    def __init__(self, board, player):
        super(MinimaxAgent, self).__init__(board, player)

    def move(self, board):

        return {'x': -1, 'y': -1, 'player': self.player}


    def createMoveTree(self, board, depth):
        tree = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}

        gameCopy = gameLogic()
        gameCopy.setBoard(board)



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

# if __name__ == "__main__":
#     game = gameLogic()
#     agent = MinimaxAgent(game.board, 1)
#     game.move(1, 2, 1)
#     game.move(0, 2, 1)
#     print(game.spotFull1D(2))
#     print(game.spotFull1D(5))
#     print(game.spotFull1D(0))



