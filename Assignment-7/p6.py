import numpy as np, random

matrix = np.random.randint(1, 100, 
    (random.randint(1, 5), random.randint(1, 5)))
    
print(matrix)
print(f"Rank = {np.linalg.matrix_rank(matrix)}")