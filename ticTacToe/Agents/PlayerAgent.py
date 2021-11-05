from ticTacToe.Agents.Agent import Agent

class PlayerAgent(Agent):

    def __init__(self, board, player):
        super(PlayerAgent, self).__init__(board, player)


    def move(self, board):
        findMove = self.playerMove()

        return {'x': findMove[0], 'y': findMove[1], 'player': self.player}

    def playerMove(self):

        location = int(input("Place to Move: ")) - 1

        findMove = self.oneDMove(location)

        while location > 9 or location < 0 or self.spotFull(findMove[0], findMove[1]):
            if location > 9 or location < 0:
                print("Move Out of Range")
            else:
                print("Spot already filled")

            location = int(input("Place to Move: ")) - 1
            findMove = self.oneDMove(location)


        return findMove

    def oneDMove(self, num):
        col = num % 3
        row = int(num/3)

        return [row, col]

