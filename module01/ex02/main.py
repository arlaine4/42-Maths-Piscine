import dot_product_vector as dot_vec
import sys

def convert_arg_to_list(arg):
    try:
        return [float(elem) for elem in arg]
    except:
        sys.exit("Invalid content inside {}".format(arg))

if __name__ == "__main__":
    try:
        vec1 = sys.argv[1].split(' ')
        vec2 = sys.argv[2].split(' ')
    except:
        sys.exit("Invalid vector parameters")
    v = dot_vec.Vector(convert_arg_to_list(vec1))
    v2 = dot_vec.Vector(convert_arg_to_list(vec2))
    print(v, v2)
    v.dot(v2)
    print(v)
