from decimal import Decimal
from DotsAndBoxes import *

def calculate_score(board, player):
    counter = 0
    i = board.dimentions[1] * 2
    while i < ((2 * board.dimentions[0] - 1) * (2 * board.dimentions[1] - 1)):
        if board.board[i] == player:
            counter += 1
        elif board.board[i] == (not player):
            counter -= 1
        i += 2 + board.dimentions[1] * 2 if i % (board.dimentions[1] * 2 - 1) == (board.dimentions[1] * 2 - 1) - 2 else 2
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