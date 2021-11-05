from ticTacToe.Gameboards.gameLogic import gameLogic
from ticTacToe.Agents.BasicAgent import BasicAgent
from ticTacToe.Agents.MinimaxAgent import MinimaxAgent

sims = 100
simResults = [0, 0, 0]

if __name__ == "__main__":
    for i in range(0, sims):
        game = gameLogic()

        # See progression in each algorithm:

        # Random Move
        # player1 = RandomAgent(game.board, 1)
        # player2 = RandomAgent(game.board, 2)

        # Basic Agent
        # player1 = BasicAgent(game.board, 1)
        # player2 = RandomAgent(game.board, 2)

        # Complex Agent
        player1 = MinimaxAgent(game.board, 1)
        player2 = BasicAgent(game.board, 2)

        while not game.gameFinished():
            game.turn(player1.move(game.board))
            if not game.gameFinished():
                game.turn(player2.move(game.board))

        index = int(game.winner)
        simResults[index] += 1

        print(game.winner)

    for i in range(0, len(simResults)):
        if i == 0:
            print("No Winner: {}".format(simResults[i]))
        else:
            print("Player {}: {}".format(i, simResults[i]))

