# RANK-OF-A-MATRIX
## Aim:
To write a python program to find the rank of a matrix
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step 1: 
Import the numpy module to use the built-in functions for calculation
### Step 2: 
Prepare the lists from each linear equations and assign in np.array()
### Step 3:
Using the np.linalg.matrix_rank(), we can find the rank of the given matrix.
### Step 4: 
End the program
## Program:
```
#Developed by: Rohith S
#RegisterNumber: 25008317
import numpy as np
a = np.array([[3,2,5],[1,1,2],[3,3,6]])
b = np.linalg.matrix_rank(a)
print(b)
```
## Output:
<img width="278" height="158" alt="image" src="https://github.com/user-attachments/assets/f42c24d1-fed0-48c0-8ceb-acb4683b7d87" />

## Result:
Thus the rank for the given matrix is successfully solved by  using a python program.
