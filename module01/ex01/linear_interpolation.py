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


def interpol_calcul(_max, _min, t):
    res = (float(_max) * t) + ((1 - t) * float(_min))
    return round(res, 1)

def lerp_vector(u, v, t):
    res = [None for i in range(len(u))]
    for i in range(len(u)):
        res[i] = interpol_calcul(max([u[i], v[i]]), min([u[i], v[i]]), t)
    return res


def lerp_matrix(u, v, t):
    res = []
    for i in range(len(u)):
        res.append([])
        for j in range(len(v)):
            print(u[i][j], v[i][j],t,  float(v[i][j]) * t)
            res[i].append(interpol_calcul(u[i][j], v[i][j], t))
    return res


def lerp(u, v, t):
    mode = 'simple'
    if type(u) is Vector and type(v) is Vector:
        mode = 'vector'
    elif type(u) is Matrix and type(v) is Matrix:
        mode = 'matrix'
    elif type(u) is Matrix and type(v) is Vector or\
            type(u) is Vector and type(v) is Matrix:
                sys.exit("Conflicting types between u and v")
    if mode == 'simple':
        u, v, t = try_convert_float(u, v, t, mode)
        res = interpol_calcul(max([u, v]), min([u, v]), t)
    elif mode == 'vector':
        u, v, t = try_convert_float(u, v, t, mode)
        res = lerp_vector(u, v, t)
    elif mode == 'matrix':
        res = lerp_matrix(u.matrix, v.matrix, t)
    return res
