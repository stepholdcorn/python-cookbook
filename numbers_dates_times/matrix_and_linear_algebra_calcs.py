import numpy as np 
import numpy.linalg

m = np.matrix([1, -2, 3], [0, 4, 5], [7, 8 -9])
v = np.matrix([[2], [3], [4]])

print(m)
print(m.T)
print(m * v)
print(numpy.linalg.det(m))
print(numpy.linalg.eigvals(m))
