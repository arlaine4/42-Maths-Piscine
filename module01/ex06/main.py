import sys
from vector import Vector
from matrix import Matrix

def check_args(args):
    if len(args) != 3:
        sys.exit("Wrong number of arguments")
    for i in range(1, len(args)):
        if len(args[i]) == 0:
            sys.exit("Empty vector or matrix inside args")

def format_elem_for_matrix_creation(elem):
    elem = elem.split(' ')
    for i in range(len(elem)):
        elem[i] = elem[i].replace('[', '').replace(']', '')
    return elem

def unpack_args_from_argv(args):
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
            sys.exit("Please input a vector or matrix with bracket to define it")
    return lst_args[0], lst_args[1]

if __name__ == '__main__':
    check_args(sys.argv)
    elem1, elem2 = unpack_args_from_argv(sys.argv[1:])
    print(elem1,'\n\n', elem2)
