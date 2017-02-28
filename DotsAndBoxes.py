class Board:

	def __init__(self, player = "B", n = 0, m = 0):
		self.player = player
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

	def convertMoveFormat(self, move): # From my representation to Pablo's
		x, y = 0, 0

		if move[2] == 0 or move[2] == 3:
			x = (move[0] + 1 * (move[2] == 3)) * 2
			y = (move[1] * 2) + 1
		else:
			x = (move[0] * 2) + 1
			y = (move[1] + 1 * (move[2] == 2)) * 2

		return (x, y)

	def listMoves(self):
		moves = []
		for i in range(len(self.board)):

			for j in range(len(self.board[i])):
				movesBox = map(lambda x : self.convertMoveFormat((i, j, x)), self.board[i][j].listMoves())
				for k in movesBox:
					if k not in moves:
						moves += [k]
				
		return moves

	def calculateScore(self):
		p1, p2 = 0, 0
		for row in self.board:
			for item in row:
				if item.player == "":
					continue
				elif item.player == self.player:
					p1 += 1
				else:
					p2 += 1

		return p1 - p2

	def isFinished(self):
		for row in self.board:
			for item in row:
				if item.player == "":
					return False
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

	def listMoves(self):
		moves = []
		for i in range(4):
			if not self.edges[i]:
				moves.append(i)
		return moves

	def toString(self):
		string = "." + ("x" if self.edges[0] else "_") + ".|" + \
		("x" if self.edges[1] else "_") + \
		("*" if self.player == "" else self.player) + \
		("x" if self.edges[2] else "_") + "|." + \
		("x" if self.edges[3] else "_") + "."

		return string