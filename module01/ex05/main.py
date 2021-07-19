import sys
from vector import Vector
import cross_product as cross

def check_args(args):
    if len(args) != 3:
        sys.exit("Wrong number of arguments")
    if len(args[1]) == 0 or len(args[2]) == 0:
        sys.exit("Empty matrix")

def format_vector(v1, v2):
    try:
        v1 = [float(elem) for elem in v1]
        v2 = [float(elem) for elem in v2]
    except:
        sys.exit("Invalid content inside vectors")
    return v1, v2

if __name__ == "__main__":
    check_args(sys.argv)
    try:
        vec1 = sys.argv[1].split(' ')
        vec2 = sys.argv[2].split(' ')
    except ValueError:
        sys.exit("Invalid format inside matrix")
    vec1, vec2 = format_vector(vec1, vec2)
    v1 = Vector(vec1)
    v2 = Vector(vec2)
    cross.cross_product(v1.vector, v2.vector)
