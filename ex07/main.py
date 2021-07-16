import sys
import sat as satis

def check_args(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")
    if len(args[1]) == 0:
        sys.exit("Empty rpn")


if __name__ == "__main__":
    check_args(sys.argv)
    satis.sat(sys.argv[1])
