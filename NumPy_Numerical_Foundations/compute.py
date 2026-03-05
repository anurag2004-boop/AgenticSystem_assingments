import numpy as np
# Element-wise Operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
# Addition
result_add = array_a + array_b
print("Addition:", result_add)  # Output: [5 7 9]
# Subtraction
result_sub = array_a - array_b
print("Subtraction:", result_sub)  # Output: [-3 -3 -3]
# Multiplication
result_mul = array_a * array_b
print("Multiplication:", result_mul)  # Output: [4 10 18]
# Division
result_div = array_a / array_b
print("Division:", result_div)  # Output: [0.25 0.4 0.5]
# Matrix Operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
# Matrix Addition   
result_matrix_add = matrix_a + matrix_b
print("Matrix Addition:\n", result_matrix_add)
# Matrix Multiplication
result_matrix_mul = np.dot(matrix_a, matrix_b)
print("Matrix Multiplication:\n", result_matrix_mul)





