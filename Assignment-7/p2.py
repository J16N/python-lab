import numpy as np

matrix = np.random.randint(1, 100, (3, 3))
print(matrix)
print(f"Diagonal Sum = {np.trace(matrix)}")