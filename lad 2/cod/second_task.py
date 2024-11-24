import os.path

import numpy as np

matrix = np.load("E:/pythonProject/lad 2/data/second_task.npy")

x = []
y = []
z = []

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i][j]>573:
            x.append(i)
            y.append(j)
            x.append(matrix[i][j])

np.savez("E:/pythonProject/lad 2/result/second_task.npz", x=x, y=y, z=z)
np.savez_compressed("E:/pythonProject/lad 2/result/second_task_compress.npz",  x=x, y=y, z=z)

first_size = os.path.getsize('E:/pythonProject/lad 2/result/second_task.npz')
second_size = os.path.getsize('E:/pythonProject/lad 2/result/second_task_compress.npz')

print(f"savez = {first_size} ")
print(f"savez_compressed = {second_size} ")
print(f"diff = {first_size - second_size}")