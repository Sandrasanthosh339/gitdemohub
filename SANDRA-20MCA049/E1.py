import numpy as np

A = np.array([[1,4,5],[2,3,7]])
B = np.array([[2,4,6],[1,5,8]])

print("First Matrix:")
print(A)
print("Second Matrix:")
print(B)

print("Addition Of matrices:")
print(np.add(A,B))

#C = A + B
#print(C)

print("Transpose of Matrix A:")
print(np.transpose(A))

print("Transpose of Matrix B:")
print(np.transpose(B))