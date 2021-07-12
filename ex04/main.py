import sys
import print_truth_table as ptt

def	check_args(args):
	if len(args) != 2:
		sys.exit("Invalid number of arguments")
	elif len(args) == 2:
		if len(args[1]) == 0:
			sys.exit("Empty rpn")

if __name__ == "__main__":
	check_args(sys.argv)
	ptt.get_truth_table(sys.argv[1])
	
