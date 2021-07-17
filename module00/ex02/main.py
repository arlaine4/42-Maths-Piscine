import sys
from gray_code import gray_code

def	check_arg(args):
	if len(args) != 2:
		sys.exit("Wrong number of parameters")
	else:
		try:
			int(args[1])
		except:
			sys.exit("Invalid parameter type")

if __name__ == "__main__":
	check_arg(sys.argv)
	print(gray_code(int(sys.argv[1])))
