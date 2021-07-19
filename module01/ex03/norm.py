from math import sqrt

def manhattan_norm(vec):
    res = 0
    for elem in vec.vector:
        res += elem
    return res

def euclidian_norm(vec):
    res = 0
    for elem in vec.vector:
        res += elem ** 2
    res = res ** 0.5
    return round(res, 9)

def infinite_norm(vec):
    return max(vec.vector)

def norms(vec):
    res_norms = [0, 0, 0]
    res_norms[0] = manhattan_norm(vec)
    res_norms[1] = euclidian_norm(vec)
    res_norms[2] = infinite_norm(vec)
    return res_norms

