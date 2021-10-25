from Agent import Agent

class RandomAgent(Agent):

    def __init__(self, board, player):
        super(RandomAgent, self).__init__(board, player)

    def move(self, board):
        return self.randomMove()
