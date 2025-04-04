import numpy as np


array1 = np.random.randint(0, 21, size=(3, 3))
array2 = np.random.randint(0, 21, size=(3, 3))


matrix_addition = array1 + array2


matrix_multiplication = np.dot(array1, array2)


transpose_of_product = np.transpose(matrix_multiplication)

# Print the results
print("Array 1:\n", array1)
print("Array 2:\n", array2)
print("\nMatrix Addition (Array 1 + Array 2):\n", matrix_addition)
print("\nMatrix Multiplication (Array 1 * Array 2):\n", matrix_multiplication)
print("\nTranspose of the Product Matrix:\n", transpose_of_product)
