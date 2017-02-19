import sys

"""

.   .   .   .
             
.   .   .   .
             
.   .   .   . 


"""

## Classes

class Board:

	def __init__(self, n = 0, m = 0):
		self.board = []

		for i in xrange(n -1):
			self.board += [[]]
			for j in xrange(m - 1):
				self.board[-1].append(Box())


		upperVertexes = []
		for j in range(m - 1):
			# print (j, j + 1)
			upperVertexes.append(Vertex((0, j), (0, j + 1)))

		for i in range(n -1):
			lowerVertexes = []
			for j in range(m - 1):
				lowerVertexes.append(Vertex((i + 1, j), (i + 1, j + 1)))


			horizontalVertexes = []
			## Horizontal Vertexes
			for j in range(m):
				horizontalVertexes.append(Vertex((i, j), (i + 1, j)))


			## Fill Boxes
			for j in range(m - 1):
				self.board[i][j].vertexes = [upperVertexes[j], 
				horizontalVertexes[j], horizontalVertexes[j + 1], 
				lowerVertexes[j]]


			## End
			upperVertexes = lowerVertexes



	@staticmethod
	def convertStringToBoard(stringBoard):
		stringBoard = stringBoard.split("|")


		return ""

class Box:
	
	def __init__(self):
		self.vertexes = [] # UP LEFT RIGHT DOWN

class Vertex:
	
	def __init__(self, edge1 = (), edge2 = ()):
		self.edge1 = edge1
		self.edge2 = edge2

## Functions
		
def nextMove():
	x, y = 0, 0
	return (x, y)


## Input

if __name__ == "__main__":
	args = sys.argv[1:]

	if (len(args) != 2):
		raise ValueError("Invalid Arguments")

	b =  Board(2, 3)
	for i in b.board:
		print i


	print "\n\n"
	print b.board[0][0].vertexes[2].edge1
	print b.board[0][1].vertexes[1].edge1
	b.board[0][0].vertexes[2].edge1 = "a"
	print b.board[0][1].vertexes[1].edge1