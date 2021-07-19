from vector import Vector

def cross_product(v1, v2, mode=None):
    res = [0, 0, 0]
    res[0] = v1[1] * v2[2] - v1[2] * v2[1]
    res[1] = v1[2] * v2[0] - v1[0] * v2[2]
    res[2] = v1[0] * v2[1] - v1[1] * v2[0]
    if mode == 'return':
        return res
    for i in range(len(res)):
        print(f'[{res[i]}]')
