import sys
from DotsAndBoxes import *

if __name__ == "__main__":
	args = sys.argv[1:]

	if (len(args) != 2):
		raise ValueError("Invalid Arguments")

	b =  Board()

	print "\n\n"

	b.inputBoard(args[1])
	b.move(1, 0, "B")
	print b.toString()
	