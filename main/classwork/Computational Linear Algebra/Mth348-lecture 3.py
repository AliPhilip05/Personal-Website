import numpy as np

markovChain = np.array([[0.90, 0.07,0.02,0.01], 
               [0.,0.93,0.05,0.02],
               [0.,0.,0.85,0.15],
               [0.,0.,0.,1.]])
'''for num in markovChain:
    for num in num:
     print(num)'''

A = markovChain 
B = np.array([[0.85],[0.10],[0.05],[0]])

'A.T = take the transpose of A, @ = matrix multiplication'
A = A.T
C = A @ B

'''
if you start with a 2 × 3 matrix,
 transposing it turns it into a 3 × 2 matrix:
'''

print(A)
print(C)