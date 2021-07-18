import sys
from vector import Vector
from matrix import Matrix

def try_convert_float(u, v, t, mode):
    try:
        t = float(t)
    except ValueError:
        sys.exit("Invalid type for t")
    if mode == 'simple':
        try:
            u = float(u)
        except ValueError:
            sys.exit("Invalid type for u")
        try:
            v = float(v)
        except ValueError:
            sys.exit("Invalid type for v")
    elif mode == 'vector':
        try:
            new_u = [float(elem) for elem in u.vector]
            u = new_u
        except ValueError:
            sys.exit("Invalid vector for u")
        try:
            new_v = [float(elem) for elem in v.vector]
            v = new_v
        except ValueError:
            sys.exit("Invalid vector for v")
    return u, v, t


def lerp_vector(u, v, t):
    res = []
    return res


def lerp_matrix(u, v, t):
    res = []
    return res


def lerp(u, v, t):
    if type(u) is Vector and type(v) is Vector:
        mode = 'vector'
    elif type(u) is Matrix and type(v) is Matrix:
        mode = 'matrix'
    elif type(u) is Matrix and type(v) is Vector or\
            type(u) is Vector and type(v) is Matrix:
                sys.exit("Conflicting types between u and v")
    else:
        mode = 'simple'
    if mode == 'simple':
        u, v, t = try_convert_float(u, v, t, mode)
        if t == 0:
            return min([u, v])
        elif t == 1:
            return max([u, v])
        elif t == 0.5:
            return (max([u, v]) - min([u, v])) * 0.5
        else:
            res = max([u, v]) - min([u, v])
            res = res + (res * t)
        return res
    elif mode == 'vector':
        u, v, t = try_convert_float(u, v, t, mode)
        res = lerp_vector(u, v, t)
    elif mode == 'matrix':
        res = lerp_matrix(u, v, t)
    return res
