import sys
import powerset as pwrset

def check_args(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")
    if len(args[1]) == 0:
        sys.exit("Empty set")

if __name__ == "__main__":
    check_args(sys.argv)
    pwrset.powerset(sys.argv[1])
