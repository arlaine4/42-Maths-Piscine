def trace(m):
    res = 0
    for i in range(0, m.shape[1], 1):
        res += m[i][i]
    return res
