import sys
import conjunctive_normal_form as cnf

def check_args(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")
    if len(args[1]) == 0:
        sys.exit("Emtpy rpn")


if __name__ == "__main__":
    check_args(sys.argv)
    cnf.convert_rpn_to_nnf(sys.argv[1])
