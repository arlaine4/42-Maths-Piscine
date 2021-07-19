from vector import Vector
import sys
import norm

def check_args(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")
    if len(args[1]) == 0:
        sys.exit("Empty vector")

def print_res(res):
    for i in range(len(res)):
        if i < len(res) - 1:
            print(str(res[i]) + ', ', end='')
        else:
            print(str(res[i]))

def check_vector_validity(arg):
    arg = arg.split(' ')
    try:
        vec = [float(elem) for elem in arg]
    except:
        sys.exit("Invalid content inside vec")
    return vec

if __name__ == "__main__":
    check_args(sys.argv)
    v = check_vector_validity(sys.argv[1])
    vec = Vector(v)
    res = norm.norms(vec)
    print_res(res)
