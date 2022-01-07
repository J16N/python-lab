import numpy as np, random

matrix = np.random.randint(1, 100, 
    (random.randint(1, 5), random.randint(1, 5)))

print(matrix)
print(f"Row wise maximum = {np.amax(matrix)}")
print(f"Column wise minimum = {np.amin(matrix)}")