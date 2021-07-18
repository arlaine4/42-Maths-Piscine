import sys
import linear_interpolation
from vector import Vector
from matrix import Matrix

def format_elem_for_matrix_creation(elem):
    elem = elem.split(' ')
    for i in range(len(elem)):
        elem[i] = elem[i].replace('[', '').replace(']', '')
    return elem

def unpack_args_from_argv(args):
    if len(args) == 2:
        return args[1].split(' ')
    else:
        lst_args = []
        for elem in args:
            if '[' in elem:
                if elem.count('[') > 1:
                    elem = format_elem_for_matrix_creation(elem)
                    lst_args.append(Matrix(elem))
                elif elem.count('[') == 1:
                    elem = format_elem_for_matrix_creation(elem)
                    lst_args.append(Vector(elem))
            else:
                try:
                    lst_args.append(float(elem))
                except ValueError:
                    sys.exit("Invalid type for t")
    return lst_args[0], lst_args[1], lst_args[2]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        u, v, t = unpack_args_from_argv(sys.argv)
    else:
        u, v, t = unpack_args_from_argv(sys.argv[1:])
    print(linear_interpolation.lerp(u, v, t))
