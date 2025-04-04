import numpy as np

a = np.array([[3, 5, 7], [2, 6, 8], [1, 4, 9]])
b = np.array([[4, 2, 6], [8, 5, 3], [7, 9, 1]])

c = a + b
d = c.T

print("Matrix a:")
print(a)

print("\n Matrix b:")
print(b)

print("\n Sum of matrices (c):")
print(c)

print("\n Transpose of the sum (d):")
print(d)