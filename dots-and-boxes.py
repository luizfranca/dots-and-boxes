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


		upperEdges = []
		for j in range(m - 1):
			# print (j, j + 1)
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
				self.board[i][j].edges = [upperEdges[j], 
				horizontalEdges[j], horizontalEdges[j + 1], 
				lowerEdges[j]]


			## End
			upperEdges = lowerEdges



	@staticmethod
	def convertStringToBoard(stringBoard):
		stringBoard = stringBoard.split("|")


		return ""

class Box:
	
	def __init__(self):
		self.edges = [] # UP LEFT RIGHT DOWN

class Edge:
	
	def __init__(self, vertex1 = (), vertex2 = ()):
		self.vertex1 = vertex1
		self.vertex2 = vertex2

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
	print b.board[0][0].edges[2].vertex1
	print b.board[0][1].edges[1].vertex1
	b.board[0][0].edges[2].vertex1 = "a"
	print b.board[0][1].edges[1].vertex1