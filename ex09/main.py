import sys
import set_eq as s_eq

def check_args(args):
    if len(args) != 3:
        sys.exit("Wrong number of arguments")


if __name__ == "__main__":
    check_args(sys.argv)
    print(s_eq.set_eq(sys.argv[1].split(' '), sys.argv[2].split(' ')))

