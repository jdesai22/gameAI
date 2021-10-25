import random

class Agent():

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def move(self, board):
        pass

    def randomMove(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        while self.spotFull(x, y):
            x = random.randint(0, 2)
            y = random.randint(0, 2)

        return {'x': x, 'y': y, 'player': self.player}

    def spotFull(self, row, col):
        return bool(self.board[row][col])

