import sys
from cosine import cosin
from vector import Vector

def check_args(args):
    if len(args) != 3:
        sys.exit("Wrong number of arguments")
    if len(args) == 0:
        sys.exit("Empty vector")

def format_arg(arg):
    arg = arg.split(' ')
    try:
        lst = [float(elem) for elem in arg]
    except ValueError:
        sys.exit("Invalid content inside vector")
    return lst

if __name__ == "__main__":
    check_args(sys.argv)
    vec1 = Vector(format_arg(sys.argv[1]))
    vec2 = Vector(format_arg(sys.argv[2]))
    print(cosin(vec1, vec2))

