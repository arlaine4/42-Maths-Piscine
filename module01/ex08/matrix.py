import sys
import numpy as np
from copy import deepcopy

class Matrix:
    def __init__(self, m, nb_brackets):
        self.matrix = m
        self.nb_brackets = nb_brackets
        self.format_matrix()
        self.matrix_trace = 0
        self.transposed_m = None

    def format_matrix(self):
        if len(self.matrix) == 0:
            sys.exit("Invalid matrix {}".format(self.matrix))
        len_line = len(self.matrix) / self.nb_brackets
        if not len_line.is_integer():
            sys.exit("Invalid matrix {}".format(self.matrix))
        new_m = np.array(self.matrix)
        new_m = [float(elem) for elem in new_m]
        print("1 : \n\n",new_m)
#        new_m = np.reshape(new_m, (int(len_line), int(self.nb_brackets)))
        new_m = np.reshape(new_m, (int(self.nb_brackets), int(len_line)))
        print("2 : \n\n", new_m)
        self.matrix = new_m

    def __str__(self):
        return f'{self.matrix}'

    def clean_matrix_print(self):
        print('[', end='')
        for i in range(len(self.matrix)):
            if i < len(self.matrix) - 1:
                print(self.matrix[i])
            else:
                print(self.matrix[i], end='')
        print(']\n')

    def add(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other.matrix[i][j]
    
    def sub(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] -= other.matrix[i][j]

    def scale(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j] /= other.matrix[i][j]
                self.matrix[i][j] = round(self.matrix[i][j], 2)

    def trace(self):
        for i in range(0, self.matrix.shape[1], 1):
            self.matrix_trace += self.matrix[i][i]

    def transpose(self, mode='intern'):
        matrix_t = []
        columns = len(self.matrix[0])
        rows = len(self.matrix)
        for j in range(columns):
            row = []
            for i in range(rows):
                row.append(self.matrix[i][j])
            matrix_t.append(row)
        if mode == 'extern':
            return matrix_t
        elif mode == 'intern':
            self.matrix = matrix_t
