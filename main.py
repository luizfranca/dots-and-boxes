import sys
import DotsAndBoxes as dab
import DotsAndBoxesAI as ai

player = sys.argv[1] == "B"
board = sys.argv[2]

game = dab.DotsAndBoxes()
game.input_board(board)

print ai.alphabeta(game, 7, player = player)[0]