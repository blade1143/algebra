import numpy as np
from matrix import vector_1, A


b = vector_1(A)
B = np.dot(A, b)

a = np.linalg.inv(A)
x = np.dot(a, B)
print(A)
print(x)