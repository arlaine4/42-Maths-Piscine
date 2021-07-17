import sys
import matrix

def convert_arg_to_list(arg):
    return [float(elem) for elem in arg]

if __name__ == "__main__":
    elems1 = sys.argv[1].split(' ')
    elems2 = sys.argv[2].split(' ')
    m = matrix.Matrix(convert_arg_to_list(elems1))
    m2 = matrix.Matrix(convert_arg_to_list(elems2))
    m.add(m2)
    print(m)
    m.sub(m2)
    print(m)
    m.scale(m2)
    print(m)
