class DotsAndBoxes:

    def __init__(self, n = 0, m = 0):
        self.board = [None] * ((2 * n - 1) * (2 * m - 1))
        self.dimensions = (n, m)

    def _get_position(self, x, y):
        return self.board[x * (self.dimensions[0] * 2 - 1) + y]

    def _set_position(self, x, y, value):
        self.board[x * (self.dimensions[0] * 2 - 1) + y] = value

    def input_board(self, board_string):
        m = board_string.split("|")[0].count(".")
        n = board_string.count(".") / m
        self.dimensions = (n, m)
        self.board = [None] * ((2 * n - 1) * (2 * m - 1))
        board_string = board_string.replace("|", "")
        for i in range(len(board_string)):
            if board_string[i] == ".":
                continue
            elif board_string[i].upper() == "B" or board_string[i].upper()== "W" or board_string[i].upper() == "X":
                self.board[i] = False if board_string[i].upper() == "B" else True

    def to_string(self):
        board_string = ""
        i, j = 0, 0
        for cel in self.board:
            if i % 2 == j % 2 == 0:
                board_string += "."
            elif i % 2 == j % 2 != 0:
                board_string += "W" if cel else ("B" if cel == False else "*")
            else:
                board_string += "x" if cel else "_"

            j += 1
            if (j == self.dimensions[1] * 2 - 1):
                j = 0
                i += 1
                board_string += "|"

        return board_string[:-1]

    def _close_box(self, x, y, player):
        completed = False
        if x % 2 == 1: # horizontal
            if y - 2 >= 0 and self._get_position(x, y) and self._get_position(x, y - 2) and self._get_position(x - 1, y - 1) and self._get_position(x + 1, y - 1):
                completed = True
                self._set_position(x, y - 1, player)
            if (y + 2 < self.dimensions[1] * 2 - 1) and self._get_position(x, y) and self._get_position(x, y + 2) and self._get_position(x - 1, y + 1) and self._get_position(x + 1, y + 1):
                completed = True
                self._set_position(x, y + 1, player)
        else:
            if x - 2 >= 0 and self._get_position(x, y) and self._get_position(x - 2, y) and self._get_position(x - 1, y - 1) and self._get_position(x - 1, y + 1):
                completed = True
                self._set_position(x - 1, y, player)
            if (x + 2 < self.dimensions[0] * 2 - 1) and self._get_position(x, y) and self._get_position(x + 2, y) and self._get_position(x + 1, y - 1) and self._get_position(x + 1, y + 1):
                completed = True
                self._set_position(x + 1, y, player)
        return completed

    def move(self, x, y, player):
        self._set_position(x, y, True)
        return self._close_box(x, y, player)

    def list_moves(self):
        moves, i, j = [], 0, 0
        for cel in self.board:
            if i % 2 != j % 2 and not cel:
                moves.append((i, j))
            j += 1
            if (j == self.dimensions[1] * 2 - 1):
                j = 0
                i += 1
        return moves

    def is_finished(self):
        i = self.dimensions[1] * 2
        while i < ((2 * self.dimensions[0] - 1) * (2 * self.dimensions[1] - 1)):
            if self.board[i] == None:
                return False
            i += 2 + self.dimensions[1] * 2 if i % (self.dimensions[1] * 2 - 1) == (self.dimensions[1] * 2 - 1) - 2 else 2
        return True

    def copy(self):
        dab = DotsAndBoxes()
        dab.dimensions = self.dimensions
        dab.board = self.board[:]
        return dab