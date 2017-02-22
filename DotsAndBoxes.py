class Board:

	def __init__(self, n = 0, m = 0):
		self.board = self.__createBoard(n, m)

	def __createBoard(self, n, m):
		board = []
		for i in xrange(n -1):
			board += [[]]
			for j in xrange(m - 1):
				board[-1].append(Box())


		upperEdges = []
		for j in range(m - 1):
			upperEdges.append(Edge((0, j), (0, j + 1)))

		for i in range(n -1):
			lowerEdges = []
			for j in range(m - 1):
				lowerEdges.append(Edge((i + 1, j), (i + 1, j + 1)))


			horizontalEdges = []
			## Horizontal Vertexes
			for j in range(m):
				horizontalEdges.append(Edge((i, j), (i + 1, j)))


			## Fill Boxes
			for j in range(m - 1):
				board[i][j].edges = [upperEdges[j], 
				horizontalEdges[j], horizontalEdges[j + 1], 
				lowerEdges[j]]


			upperEdges = lowerEdges

		return board

	def inputBoard(self, boardString):
		m = boardString.split("|")[0].count(".")
		n = boardString.count(".") / m
		
		boardString = boardString.upper().replace(".", "").split("|")
		self.board = self.__createBoard(n, m)
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				self.board[i][j].edges[0].marked = boardString[i * 2][j] == "X" 			   # UP
				self.board[i][j].edges[1].marked = boardString[i * 2 + 1][j * 2] == "X"        # LEFT
				self.board[i][j].edges[2].marked = boardString[i * 2 + 1][(j + 1) * 2] == "X"  # RIGHT
				self.board[i][j].edges[3].marked = boardString[(i + 1) * 2][j] == "X"  		   # DOWN

				self.board[i][j].player = boardString[i * 2 + 1][j * 2 + 1].replace("*","")    # Marked

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
		boardString = boardString.replace("..", ".").replace("xx", "x")
		return boardString

	def move(self, x, y, player):
		if (x % 2 == y % 2):
			return False

		if (x == 0):
			row = 0
			pos = 0
		elif (x % 2 == 0):
			col = y / 2
			pos = 3
		else:
			col = y / 2 - 1

		if (y == 0):
			col = 0
			pos = 1
		elif (y % 2 == 0):
			row = x / 2
			pos = 2
		else:
			row = x / 2 - 1

		self.board[row][col].move(pos , player)

		if (row - 1 >= 0 and self.board[row - 1][col].isComplete()):
			self.board[row - 1][col].player = player
		if (col - 1 >= 0 and self.board[row][col - 1].isComplete()):
			self.board[row][col - 1].player = player

		if (col + 1 < len(self.board[row]) and self.board[row][col + 1].isComplete()):
			self.board[row][col + 1].player = player
		if (row + 1 < len(self.board) and self.board[row + 1][col].isComplete()):
			self.board[row + 1][col].player = player
		
		return True


class Box:
	
	def __init__(self):
		self.edges = [] # UP LEFT RIGHT DOWN
		self.player = ""

	def listVertexes(self):

		vertexes = []
		for i in self.edges:
			vertexes += i.listVertexes()

		return vertexes

	def move(self, n, player):
		self.edges[n].marked = True
		if (self.isComplete()):
			self.player = player

	def isComplete(self):
		marked = True
		for edge in self.edges:
			marked = marked and edge.marked
		return marked

	def toString(self):
		string = "." + ("x" if self.edges[0].marked else "_") + ".|" + \
		("x" if self.edges[1].marked else "_") + \
		("*" if self.player == "" else self.player) + \
		("x" if self.edges[2].marked else "_") + "|." + \
		("x" if self.edges[3].marked else "_") + "."

		return string

class Edge:
	
	def __init__(self, vertex1 = (), vertex2 = ()):
		self.vertex1 = vertex1
		self.vertex2 = vertex2
		self.marked = False

	def listVertexes(self):
		return [self.vertex1, self.vertex2]