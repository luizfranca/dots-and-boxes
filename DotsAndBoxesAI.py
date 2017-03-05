from decimal import Decimal
from DotsAndBoxes import *

def calculate_score(board, player):
    counter = 0
    for row in board.board:
        for item in row:
            if item.player == player:
                counter += 1
            if item.player == (not player):
                counter -= 1
    return counter

def alphabeta(node, depth = 10, alpha = Decimal("-Infinity"), beta = Decimal("Infinity"), is_max = True, player = True, move = (0,0)):
    children = node.list_moves()

    if len(children) == 0 or depth == 0:
        return [move, calculate_score(node, player)]

    if is_max:
        best_move =  ()
        best_score = Decimal("-Infinity")
        for x, y in children:
            current = node.copy()
            turn = current.move(x, y, player)
            temp = alphabeta(current, depth - 1, alpha, beta, turn, player, (x, y))
            if temp[1] > best_score:
                best_move = (x, y)
                best_score = temp[1]
            alpha = max(best_score, alpha)
            if beta <= alpha:
                break
        return [best_move, best_score]
    else:
        worse_move = ()
        worse_score = Decimal("Infinity")
        for x, y in children:
            current = node.copy()
            turn = current.move(x, y, not player)
            temp = alphabeta(current, depth - 1, alpha, beta, not turn, player, (x, y))
            if temp[1] < worse_score:
                worse_move = (x, y)
                worse_score = temp[1]
            beta = min(beta, worse_score)
            if beta <= alpha:
                break
        return [worse_move, worse_score]