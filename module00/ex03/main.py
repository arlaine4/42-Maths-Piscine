import sys
import eval_formula as evl

def check_arg(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")
    else:
        if len(args[1]) == 0:
            sys.exit("Empty rpn")
        else:
            for elem in args[1]:
                if elem not in ['0', '1', '^', '|', '&', '>', '=', '!']:
                    sys.exit(f"Invalid '{elem}' inside rpn")

if __name__ == "__main__":
    check_arg(sys.argv)
    evl.parse_rpn(sys.argv[1])
