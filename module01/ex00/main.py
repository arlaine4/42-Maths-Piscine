import sys
import vector
import matrix

def convert_arg_to_list(arg):
    return [float(elem) for elem in arg]

if __name__ == "__main__":
    try:
        vector1 = sys.argv[1].split(' ')
        vector2 = sys.argv[2].split(' ')
    except:
        sys.exit("Invalid vectors")
    try:
        matrix1 = sys.argv[1].split(' ')
        matrix2 = sys.argv[2].split(' ')
    except:
        sys.exit("Invalid Matricies")

    print("\nVector tests : ", end='\n\n')
    v = vector.vector(convert_arg_to_list(vector1))
    v2 = vector.vector(convert_arg_to_list(vector2))

    #--------------------------------------------#
    #               Vector part                  #
    v.add(v2)
    print("Add :", v)
    v.sub(v2)
    print("Sub :",v)
    v.scale(v2)
    print("Scale :",v)
    #                                            #
    #--------------------------------------------#

    print("\nMatrix tests : ", end='\n\n')
    #--------------------------------------------#
    #               Matrix part                  #
    m = matrix.Matrix(convert_arg_to_list(matrix1))
    m2 = matrix.Matrix(convert_arg_to_list(matrix2))
    m.add(m2)
    print("Add :\n", m)
    m.sub(m2)
    print("\nSub :\n", m)
    m.scale(m2)
    print("\nScale :\n", m)

    #--------------------------------------------#
