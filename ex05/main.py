import sys
import negation_normal_form as nnf

def	check_args(args):
    if len(args) != 2:
        sys.exit("Invalid argument numbers")
    elif len(args[1]) == 0:
        sys.exit("Empty rpn, please enter a valid input")


if __name__ == "__main__":
    check_args(sys.argv)
    nnf.parse_rpn(sys.argv[1])
    
