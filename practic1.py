import numpy as np
from scipy import sparse

vector_row = np.array([1,2,3])
vector_column = np.array([[1],[2],[3]])
matrix = np.array([[1,2],[1,2],[1,2]])
print(vector_row)
print(vector_column)
print(matrix)

matrix = np.array([[0,0],[0,1],[3,0]])
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)

matrix_large = np.array([[0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[3,0,0,0,0,0,0,0,0,0]])
matrix_large_sparse = sparse.csr_matrix(matrix_large)
print(matrix_large_sparse)

vector1 = np.array([1,2,3,4,5,6])
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(vector1[2])
print(matrix1[1,1])