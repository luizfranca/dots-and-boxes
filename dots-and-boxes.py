import sys







if __name__ == "__main__":
	args = sys.argv[1:]

	# print args

	if (len(args) != 2):
		raise ValueError("Invalid Arguments")


	print args[1]