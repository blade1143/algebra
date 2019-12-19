import numpy as np

def matrix_gen(min, max, x):
    b = np.random.randint(min, max, size=(x, x))
    b_symm = (b + b.T) / 2
    return b_symm

def vector_1(array):
    matrix = np.zeros((array.shape[0], 1))
    for i in range(len(matrix)):
        matrix[i] = 1
    return matrix

# A = np.array([[4, -2, 2],
#               [-2, 2, 2],
#               [2, 2, 14]], dtype='float')
# A = np.array([[1, 2, 3 ,4],
#               [2, 10, 5, 6],
#               [3, 5, 20, 7],
#               [4, 6, 7, 30]], dtype='float')
# A = np.array([[4. , 4. , 3. , 4. , 3. ],
#                [4. , 8. , 5.5, 6.5, 5. ],
#                [3. , 5.5, 8. , 3. , 1.5],
#                [4. , 6.5, 3. , 9. , 6. ],
#                [3. , 5. , 1.5, 6. , 8. ]])
A = np.array([[9. , 4. , 6.5, 5. , 7. , 6.5, 6.5],
               [4. , 8. , 6. , 5.5, 5.5, 4.5, 2.5],
               [6.5, 6. , 9. , 4. , 7. , 3.5, 5.5],
               [5. , 5.5, 4. , 9. , 4.5, 3.5, 2.5],
               [7. , 5.5, 7. , 4.5, 7. , 5.5, 4.5],
               [6.5, 4.5, 3.5, 3.5, 5.5, 9. , 5. ],
               [6.5, 2.5, 5.5, 2.5, 4.5, 5. , 8. ]])