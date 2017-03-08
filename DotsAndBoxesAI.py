inf = float("inf")

def calculate_score(board, player):
    counter = 0
    i = board.dimensions[1] + 1
    while i < (board.dimensions[0] * board.dimensions[1]):
        if board.board[i] == player:
            counter += 1
        elif board.board[i] == (not player):
            counter -= 1
        i += 2 + board.dimensions[1] + 1 if i % board.dimensions[1] == board.dimensions[1] - 2 else 2
    return counter

def alphabeta(node, depth = 10, alpha = -inf, beta = inf, is_max = True, player = True, move = (0,0)):
    children = node.available_moves

    if len(children) == 0 or depth == 0:
        return [move, calculate_score(node, player)]

    if is_max:
        best_move =  ()
        best_score = -inf
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
        worse_score = inf
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