from vector import Vector
from matrix import Matrix
import sys
import numpy as np


def multiply_matrix_by_vec(vec, matrix):
    if matrix.shape[1] != len(vec):
        sys.exit("Can't multiply {} dimension matrix by {} elems vector".format(matrix.shape, len(vec)))
    res = [0 for elem in range(matrix.shape[0])]
    for i in range(matrix.shape[0]):
        for j in range(len(vec)):
            if j == 0:
                res[i] = int(matrix[i][j]) * int(vec[j])
            else:
                res[i] += int(matrix[i][j]) * int(vec[j])
    return res

def multiply_matrix_matrix(m1, m2):
    if m1.shape[1] != m2.shape[0]:
        sys.exit(f"Can't multiply matrix of dimensions {m1.shape} by another matrix of dimensions {m2.shape}")
    shape = (m1.shape[1], m2.shape[0])
    res = np.zeros((shape[0], shape[1]))
    m2 = m2.T
    for i in range(shape[0]):
        for j in range(shape[1]):
            res[i][j] = mini_mult(m1[i], m2[j])
    return res

def mini_mult(elem1, elem2):
    res = 0
    for i in range(len(elem1)):
        res += elem1[i] * elem2[i]
    return res


def mul_vec(elem1, elem2):
    res = None
    if type(elem1) is Vector and type(elem2) is Matrix: 
        res = multiply_matrix_by_vec(elem1.vector, elem2.matrix)
    elif type(elem1) is Matrix and type(elem2) is Vector:
        res = multiply_matrix_by_vec(elem2.vector, elem1.matrix)
    elif type(elem1) is Matrix and type(elem2) is Matrix:
        res = multiply_matrix_matrix(elem1.matrix, elem2.matrix)
    else:
        sys.exit("Vector by Vector multiplication not supported for this exercice")
    return res
