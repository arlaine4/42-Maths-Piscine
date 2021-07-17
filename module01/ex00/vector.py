class vector:
    def __init__(self, v):
        self.vector = v

    def __str__(self):
        return f'{self.vector}'

    def add(self, other):
        for i in range(len(other.vector)):
            self.vector[i] += other.vector[i]
    
    def sub(self, other):
        for i in range(len(other.vector)):
            self.vector[i] -= other.vector[i]

    def scale(self, other):
        for i in range(len(other.vector)):
            self.vector[i] /= other.vector[i]
            self.vector[i] = round(self.vector[i], 2)
