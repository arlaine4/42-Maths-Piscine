import sys
from multiplier import multiplier

def	check_args(args):
	if len(args) != 3:
		sys.exit("Wrong number of arguments")
	else:
		try:
			nb1 = int(args[1])
			nb2 = int(args[2])
		except:
			sys.exit("Invalid parameters type")

if __name__ == "__main__":
	check_args(sys.argv)
	print(multiplier(int(sys.argv[1]), int(sys.argv[2])))
