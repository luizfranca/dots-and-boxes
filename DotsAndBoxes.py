class Board:

	def __init__(self, n = 0, m = 0):
		self.board = []
		for i in xrange(n - 1):
			self.board += [[]]
			for j in xrange(m - 1):
				self.board[i].append(Box())

	def inputBoard(self, boardString):
		m = boardString.split("|")[0].count(".")
		n = boardString.count(".") / m

		self.board = board = [[Box() for j in xrange(m - 1)] for i in xrange(n - 1)]

		boardList = boardString.upper().split("|")

		for i in range(len(boardList)):
			for j in range(len(boardList[i])):
				if boardList[i][j] == "X":
					self.move(i, j, "")

		for i in range(len(boardList)):
			for j in range(len(boardList[i])):
				if boardList[i][j] == "B" or boardList[i][j] == "W":
					self.board[i / 2][j / 2].player = boardList[i][j]

	def toString(self):
		boardString = ""

		for row in self.board:
			row1, row2, row3 = "", "", ""

			for box in row:
				boxString = box.toString().split("|")
				row1 += boxString[0]
				row2 += boxString[1]
				row3 += boxString[2]

			boardString += row1 + "|" + row2 + "|"
			
		boardString += row3
		boardString = boardString.replace("..", ".").replace("xx", "x").replace("__", "_")
		return boardString

	def move(self, x, y, player):
		if (x % 2 == y % 2):
			return False

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

		self.board[row][col].move(pos , player)

		if (row - 1 >= 0 and pos == 0):
			self.board[row - 1][col].move(3, player)
		elif (col - 1 >= 0 and pos == 1):
			self.board[row][col - 1].move(2, player)
		elif (col + 1 < len(self.board[row]) and pos == 2):
			self.board[row][col + 1].move (1, player)
		elif (row + 1 < len(self.board) and pos == 3):
			self.board[row + 1][col].move(0, player)
		
		return True


class Box:
	
	def __init__(self):
		self.edges = [False, False, False, False] # UP LEFT RIGHT DOWN
		self.player = ""

	def move(self, n, player):
		self.edges[n] = True
		if (self.isComplete()):
			self.player = player

	def isComplete(self):
		return sum(self.edges) == 4

	def toString(self):
		string = "." + ("x" if self.edges[0] else "_") + ".|" + \
		("x" if self.edges[1] else "_") + \
		("*" if self.player == "" else self.player) + \
		("x" if self.edges[2] else "_") + "|." + \
		("x" if self.edges[3] else "_") + "."

		return string