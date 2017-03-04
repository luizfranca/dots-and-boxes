class Board:

	def __init__(self, n = 0, m = 0):
		self.board = [[Box() for j in xrange(m - 1)] for i in xrange(n - 1)]

	def input_board(self, board_string):
		m = board_string.split("|")[0].count(".")
		n = board_string.count(".") / m

		self.board = [[Box() for j in xrange(m - 1)] for i in xrange(n - 1)]

		board_list = board_string.upper().split("|")

		for i in range(len(board_list)):
			for j in range(len(board_list[i])):
				if board_list[i][j] == "X":
					self.move(i, j, None)

		for i in range(len(board_list)):
			for j in range(len(board_list[i])):
				if board_list[i][j] == "B" or board_list[i][j] == "W":
					self.board[i / 2][j / 2].player = True if board_list[i][j] == "W" else False

	def to_string(self):
		board_string = ""

		for row in self.board:
			row1, row2, row3 = "", "", ""

			for box in row:
				box_string = box.to_string().split("|")
				row1 += box_string[0]
				row2 += box_string[1]
				row3 += box_string[2]

			board_string += row1 + "|" + row2 + "|"
			
		board_string += row3
		board_string = board_string.replace("..", ".").replace("xx", "x").replace("__", "_")
		return board_string

	def move(self, x, y, player):
		if (x == 0 or y == 0):
			row = x / 2
			col = y / 2
			pos = y == 0
		elif (x % 2 == 0):
			row = x / 2 - 1
			col = y / 2
			pos = 3
		else:
			row = x / 2
			col = y / 2 - 1
			pos = 2

		completed = self.board[row][col].move(pos, player)
		comp = False

		if (row - 1 >= 0 and pos == 0):
			comp = self.board[row - 1][col].move(3, player)
		elif (col - 1 >= 0 and pos == 1):
			comp = self.board[row][col - 1].move(2, player)
		elif (col + 1 < len(self.board[row]) and pos == 2):
			comp = self.board[row][col + 1].move (1, player)
		elif (row + 1 < len(self.board) and pos == 3):
			comp = self.board[row + 1][col].move(0, player)
		
		return completed or comp

	def _convert_move_format(self, move): # From my representation to Pablo's
		x, y = 0, 0

		if move[2] == 0 or move[2] == 3:
			x = (move[0] + 1 * (move[2] == 3)) * 2
			y = (move[1] * 2) + 1
		else:
			x = (move[0] * 2) + 1
			y = (move[1] + 1 * (move[2] == 2)) * 2

		return (x, y)

	def list_moves(self):
		moves = []
		for i in range(len(self.board)):

			for j in range(len(self.board[i])):
				moves_box = map(lambda x : self._convert_move_format((i, j, x)), self.board[i][j].list_moves())
				for k in moves_box:
					if k not in moves:
						moves += [k]
				
		return moves

	def is_finished(self):
		for row in self.board:
			for item in row:
				if item.player == None:
					return False
		return True

class Box:
	
	def __init__(self):
		self.edges = [False, False, False, False] # UP LEFT RIGHT DOWN
		self.player = None  # True represents your box and False the other box

	def move(self, n, player):
		self.edges[n] = True
		if (self.is_complete()):
			self.player = player
		return self.is_complete()

	def is_complete(self):
		return sum(self.edges) == 4

	def list_moves(self):
		moves = []
		for i in range(4):
			if not self.edges[i]:
				moves.append(i)
		return moves

	def to_string(self): # parameter player represents the main player
		string = "." + ("x" if self.edges[0] else "_") + ".|" + \
		("x" if self.edges[1] else "_") + \
		("*" if self.player == None else ("W" if self.player else "B")) + \
		("x" if self.edges[2] else "_") + "|." + \
		("x" if self.edges[3] else "_") + "."

		return string