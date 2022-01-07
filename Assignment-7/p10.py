import numpy as np

matrix = np.random.randint(1, 100, (1, 20))
v, c = np.unique(matrix, return_counts=True)
print(matrix)

print(f"Mean = {np.mean(matrix)}")
print(f"Median = {np.median(matrix)}")
print(f"Mode = {v[np.argmax(c)]}")