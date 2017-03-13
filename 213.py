import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
import math
import numpy

A = scipy.array([ [4, 3], [6, 3]])
P, L, U = scipy.linalg.lu(A)

b = len(A)

x = 1
y = 1

for i in range (0,b):
    x = x*L[i][i]
    y = y*U[i][i]

z = x*y
print(z)

j = math.log(z)
print(j)

k = numpy.linalg.det(A)
print(k)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)