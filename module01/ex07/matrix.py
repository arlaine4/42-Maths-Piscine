import sys
import numpy as np
from copy import deepcopy

class Matrix:
    def __init__(self, m, nb_brackets):
        self.matrix = m
        self.nb_brackets = nb_brackets
        self.format_matrix()

    def format_matrix(self):
        if len(self.matrix) == 0:
            sys.exit("Invalid matrix {}".format(self.matrix))
        len_line = len(self.matrix) / self.nb_brackets
        if not len_line.is_integer():
            sys.exit("Invalid matrix {}".format(self.matrix))
        new_m = np.array(self.matrix)
        new_m = [float(elem) for elem in new_m]
        new_m = np.reshape(new_m, (int(len_line), int(self.nb_brackets)))
        self.matrix = new_m

    def __str__(self):
        return f'{self.matrix}'

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
