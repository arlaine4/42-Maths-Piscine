class Vector:
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

    def dot(self, other):
        res = 0
        if len(self.vector) != len(other.vector):
            sys.exit("Different sizes betweens vectors, unable to do dot product.")
        for i in range(len(other.vector)):
            if res == 1 and self.vector[i] == 1 == other.vector[i]:
                continue
            else:
                res += self.vector[i] * other.vector[i]
        self.vector = res
