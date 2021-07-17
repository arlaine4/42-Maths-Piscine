import sys
import cardinal as cdl

def check_args(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")

if __name__ == "__main__":
    check_args(sys.argv)
    cdl.cardinal(sys.argv[1].split(' '))
