#Program to find the rank of a matrix.
#Developed by: Rohith S
#RegisterNumber: 25008317
import numpy as np
a = np.array([[3,2,5],[1,1,2],[3,3,6]])
b = np.linalg.matrix_rank(a)
print(b)