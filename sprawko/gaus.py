import numpy as np
import sympy as sp
import copy
from fractions import Fraction

class Gaus:
    def __init__(self, array_A, array_B):
        self.array_A = array_A
        self.array_B = array_B
        self.array_C = np.concatenate((self.array_A, self.array_B), axis = 1)
        print(self.array_C)
        self.z = 0
        # self.array_C = self.array_C + Fraction()

    def returned(self):
        return self.array_C

    def gaus_part1(self):
        for i in range(0, self.array_C.shape[0]- 1):
            for j in range(i + 1, self.array_C.shape[0]):
                self.z += 1
                if self.array_C[j][i] == 0:
                    continue
                m = self.array_C[j][i] / self.array_C[i][i]
                self.array_C[j] = self.array_C[j] - m * self.array_C[i]
        self.array_C = self.array_C.round(3)
        print()
        print(self.returned())

    def gaus_part2(self):
        x_values = []
        for i in range(1, self.array_C.shape[0] + 1):
            sum = 0
            for j in range(2, i+1):
                self.z += 1
                if i >= 2:
                    sum += self.array_C[-i][-j] * x_values[j-2]
            x = (self.array_C[-i][-1] - sum) / self.array_C[-i][-i-1]
            x_values.append(x)
        print()
        x_values.reverse()
        for i in range(len(x_values)):
            print('x',i+1,'=', x_values[i])


from matrix import matrix_gen, vector_1, A
b = vector_1(A)
B = np.dot(A, b)

g1 = Gaus(A, B)
# g1.pprint()
g1.gaus_part1()
g1.gaus_part2()