import sys, copy, time
from decimal import Decimal
from DotsAndBoxes import *

i = 1

def alphabeta(node, alpha = Decimal("-Infinity"), beta = Decimal("Infinity"), isMax = True, player1 = "B" , player2 = "W", move = (0,0)):
	children = node.listMoves()

	if len(children) == 0:
		return [move, node.calculateScore()]

	if isMax:
		bestMove =  ()
		bestScore = Decimal("-Infinity")
		for x, y in children:
			current = copy.deepcopy(node)
			current.move(x, y, player1)
			temp = alphabeta(current, alpha, beta, False, player1, player2, (x, y))
			if temp[1] > bestScore:
				bestMove = temp[0]
				bestScore = temp[1]

			alpha = max(bestScore, alpha)
			if beta <= alpha:
				break

		return [bestMove, bestScore]
	else:
		worseMove = ()
		worseScore = Decimal("Infinity")
		for x, y in children:
			current = copy.deepcopy(node)
			current.move(x, y, player1)
			temp = alphabeta(current, alpha, beta, True, player1, player2, (x, y))
			if temp[1] < worseScore:
				worseMove = temp[0]
				worseScore = temp[1]

			beta = min(beta, worseScore)
			if beta <= alpha:
				break

		return [worseMove, worseScore]