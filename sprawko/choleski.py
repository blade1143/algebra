from matrix import matrix_gen
from fractions import Fraction
import numpy as np
import sympy as sp

# A = matrix_gen(-10,10, 5,5)
# B = matrix_gen(-10,10, 5,1)

class Choleski:
    def __init__(self, array_A):
        self.array_A = array_A
        self.z = 0
        print(self.array_A)

    def det_checker(self):
        condition = self.array_A == self.array_A.transpose()
        if False in condition:
            print('macierz niesymetryczna')
            return False
        else:
            for i in range(1, self.array_A.shape[0] + 1):
                matrix = self.array_A[:i, :i]
                det = np.linalg.det(matrix)
                if det <= 0:
                    print('macierz niedodatnio okreslona')
                    return False
            print('macierz dodatnio okreslona i symetryczna')
            return '!'

    def choleski_part1(self):
        x, y = self.array_A.shape
        matrix_L = np.zeros((x, y), dtype='float')
        z = 0
        for i in range(x):
            for j in range(i+1):
                self.z += 1
                z+=1
                if i == j:
                    matrix_L[i][i] = np.sqrt(self.array_A[i][i] -
                    (np.sum([matrix_L[i][k] ** 2 for k in range(i)])))
                else:
                    a = np.sum([matrix_L[j][k]*matrix_L[i][k] for k in range(i)])
                    matrix_L[i][j] = (self.array_A[i][j] - a) / matrix_L[j][j]
        matrix_L = matrix_L.round(3)
        return matrix_L, matrix_L.transpose()

    def matrix_conc(self, ar_A, ar_B):
        return np.concatenate((ar_A, ar_B), axis = 1)

    def choleski_x(self, array):
        array = array.round(3)
        solution = []
        z = 0
        for i in range(1, array.shape[0] + 1):
            sum = 0
            for j in range(2, i+1):
                self.z += 1
                z += 1
                if i >= 2:
                    sum += array[-i][-j] * solution[j-2]
            x = (array[-i][-1] - sum) / array[-i][-i-1]
            solution.append(x)

        solution.reverse()
        for i in range(len(solution)):
            print('x',i+1,'=', solution[i])

    def choleski_y(self, array):
        array = array.round(3)

        solution = []
        z = 0
        for i in range(0, array.shape[0]):
            sum = 0
            for j in range(0, i):
                self.z += 1
                z += 1
                if i >= 1:
                    sum += array[i][j] * solution[j]
            y = (array[i][-1] - sum) / array[i][i]
            solution.append(y)

        for i in range(len(solution)):
            print('y',i+1,'=', solution[i])

        y = np.asarray(solution)
        y = y.reshape(y.shape[0],1)
        return y


from matrix import matrix_gen, vector_1, A

b = vector_1(A)
B = np.dot(A, b)

# x = '-'
# while x != '!':
#     A = matrix_gen(1, 10, 5)
#     ch1 = Choleski(A)
#     x = ch1.det_checker()
ch1 = Choleski(A)
ch1.det_checker()
L, Lt = ch1.choleski_part1()
print(L)
print(Lt)
l_new = ch1.matrix_conc(L, B)
print(l_new)
y_vector =  ch1.choleski_y(l_new)
lt_new = ch1.matrix_conc(Lt, y_vector)
print(lt_new.round(3))
ch1.choleski_x(lt_new)
