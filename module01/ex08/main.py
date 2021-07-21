import sys
from matrix import Matrix

def check_args(args):
    if len(args) != 2:
        sys.exit("Wrong number of arguments")
    if len(args[1]) == 0:
        sys.exit("Empty matrix")

def format_elem_for_matrix_creation(elem):
    nb_brackets = elem.count('[') - 1
    elem = elem.split(' ')
    for i in range(len(elem)):
        elem[i] = elem[i].replace('[', '').replace(']', '')
    if nb_brackets > 1:
        return elem, nb_brackets
    else:
        return elem, _

if __name__ == "__main__":
    check_args(sys.argv)
    elem, nb_brackets = format_elem_for_matrix_creation(sys.argv[1])
    try:
        m = Matrix(elem, nb_brackets)
    except:
        sys.exit("Error occured during matrix creation")
    m.clean_matrix_print()
    m.transpose()
    m.clean_matrix_print()
