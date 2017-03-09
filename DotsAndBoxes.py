class DotsAndBoxes:

    def __init__(self, n = 0, m = 0):
        self.board = [None] * ((2 * n - 1) * (2 * m - 1))
        self.dimensions = (n * 2 - 1, m * 2 - 1)
        self.available_moves = self._list_moves()
        self.boxes = [0, 0] # Player False, Player True

    def input_board(self, board_string):
        m = board_string.split("|")[0].count(".")
        n = board_string.count(".") / m
        self.dimensions = (n * 2 - 1, m * 2 - 1)
        self.board = [None] * ((2 * n - 1) * (2 * m - 1))
        board_string = board_string.replace("|", "")
        for i in range(len(board_string)):
            if board_string[i] == ".":
                continue
            elif board_string[i].upper() == "B" or board_string[i].upper() == "W" or board_string[i].upper() == "X":
                self.board[i] = False if board_string[i].upper() == "B" else True
                if (board_string[i].upper() != "X" ):
                    self.boxes[board_string[i].upper() == "W"] += 1
        self.available_moves = self._list_moves()

    def to_string(self):
        board_string, i = "", 0
        for cel in self.board:
            x, y = i / self.dimensions[1], i % self.dimensions[1]
            if x % 2 == y % 2 == 0:
                board_string += "."
            elif x % 2 == y % 2 != 0:
                board_string += "W" if cel else ("B" if cel == False else "*")
            else:
                board_string += "x" if cel else "_"
            board_string += "|" if y == self.dimensions[1] - 1 else ""
            i += 1

        return board_string[:-1]

    def _close_box(self, x, y, player):
        completed = False
        if x % 2 == 1: # horizontal
            if y - 2 >= 0 and self.board[x * self.dimensions[1] + y] and self.board[x * self.dimensions[1] + y - 2] and self.board[(x - 1) * self.dimensions[1] + y - 1] and self.board[(x + 1) * self.dimensions[1] + y - 1]:
                completed = True
                self.boxes[player] += 1
                self.board[x * self.dimensions[1] + y - 1] = player
            if (y + 2 < self.dimensions[1]) and self.board[x * self.dimensions[1] + y] and self.board[x * self.dimensions[1] + y + 2] and self.board[(x - 1) * self.dimensions[1] + y + 1]  and self.board[(x + 1) * self.dimensions[1] + y + 1]:
                completed = True
                self.boxes[player] += 1
                self.board[x * self.dimensions[1] + y + 1] = player
        else:
            if x - 2 >= 0 and self.board[x * self.dimensions[1] + y] and self.board[(x - 2) * self.dimensions[1] + y] and self.board[(x - 1) * self.dimensions[1] + y - 1] and self.board[(x - 1) * self.dimensions[1] + y + 1]:
                completed = True
                self.boxes[player] += 1
                self.board[(x - 1) * self.dimensions[1] + y] = player
            if (x + 2 < self.dimensions[0]) and self.board[x * self.dimensions[1] + y] and self.board[(x + 2) * self.dimensions[1] + y] and self.board[(x + 1) * self.dimensions[1] + y - 1] and self.board[(x + 1) * self.dimensions[1] + y + 1]:
                completed = True
                self.boxes[player] += 1
                self.board[(x + 1) * self.dimensions[1] + y] = player
        return completed

    def move(self, x, y, player = True):
        self.board[x * self.dimensions[1] + y] = True
        self.available_moves.remove((x, y))
        return self._close_box(x, y, player)

    def _list_moves(self):
        moves, i = [], 1
        for cel in self.board[1::2]:
            if not cel:
                moves.append((i / self.dimensions[1], i % self.dimensions[1]))
            i += 2
        return moves

    def is_finished(self):
        i = self.dimensions[1] + 1
        while i < (self.dimensions[0] * self.dimensions[1]):
            if self.board[i] == None:
                return False
            i += self.dimensions[1] if i % self.dimensions[1] == self.dimensions[1] - 2 else 2
        return True

    def copy(self):
        dab = DotsAndBoxes()
        dab.dimensions = self.dimensions
        dab.board = self.board[:]
        dab.available_moves = self.available_moves[:]
        dab.boxes = self.boxes[:]
        return dab