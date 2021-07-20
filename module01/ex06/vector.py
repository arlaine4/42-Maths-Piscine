from copy import deepcopy

class Vector:
    def __init__(self, v):
        self.vector = v
        self.format_vector()
        self.cosin = None

    def format_vector(self):
        new_v = deepcopy(vector)
        for i in range(len(self.vector)):
            new_v[i] = float(self.vector[i])
        self.vector = new_v

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

    def dot(self, other, mode=None):
        res = 0
        if len(self.vector) != len(other.vector):
            sys.exit("Different sizes betweens vectors, unable to do dot product.")
        for i in range(len(other.vector)):
            if res == 1 and self.vector[i] == 1 == other.vector[i]:
                continue
            else:
                res += self.vector[i] * other.vector[i]
        if mode == 'cosinus':
            return res
        else:
            self.vector = res

    def cos(self, other, mode='intern'):
        self_magnitude = find_vector_magnitude(self)
        other_magnitude = find_vector_magnitude(other)
        prod = self.dot(other, 'cosinus')
        cosin = prod / (self_magnitude * other_magnitude)
        if mode == 'intern_call':
            self.cosin = cosin
        elif mode == 'extern_call':
            return cosin

def find_vector_magnitude(inst):
    magnitude = 0
    for elem in inst.vector:
        magnitude += elem ** 2
    return magnitude ** 0.5
