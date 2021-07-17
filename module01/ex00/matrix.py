class Matrix:
    def __init__(self, m):
        self.matrix = m

    def __str__(self):
        return f'{self.matrix}'

    def add(self, other):
        for i in range(len(other.matrix)):
            self.matrix[i] += other.matrix[i]
    
    def sub(self, other):
        for i in range(len(other.matrix)):
            self.matrix[i] -= other.matrix[i]

    def scale(self, other):
        for i in range(len(other.matrix)):
            self.matrix[i] /= other.matrix[i]
            self.matrix[i] = round(self.matrix[i], 2)
