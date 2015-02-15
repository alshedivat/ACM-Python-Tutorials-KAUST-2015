"""
Construct a 1000x1000 lil_matrix and add some values to it, convert it
to CSC format and solve A x = b for x with a direct solver.
"""
%pylab inline --no-import-all
from matplotlib import pyplot as plt
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg.dsolve import linsolve
import time

rand = np.random.rand

A = sps.lil_matrix((10000, 10000), dtype=np.float64)
A[0::100, 2000:3000] = rand(1000)
A.setdiag(rand(10000))

A = A.tocsc() # Compressed Sparse Column format

# Spy matrix
plt.spy(mtx, marker='.', markersize=2)
plt.show()

b = rand(10000) # random rhs

t1 = time.time() # initial time
x = linsolve.spsolve(A, b) # solve system
t2 = time.time() # final time
print 'residual:', np.linalg.norm(A * x - rhs) 
print t2-t1
