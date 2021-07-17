import sys
import numpy as np

class Matrix:
    def __init__(self, m):
        self.matrix = m
        self.format_matrix()

    def format_matrix(self):
        if len(self.matrix) % 2 != 0 or len(self.matrix) == 0:
            sys.exit("Invalid matrix {}".format(self.matrix))
        len_line = int(len(self.matrix)**0.5)
        new_m = np.array(self.matrix)
        new_m = np.reshape(new_m, (len_line, len_line))
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
